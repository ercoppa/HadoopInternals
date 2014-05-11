import glob
import re
import os
import sys
import urllib2
import multiprocessing 
import sys
import os
import traceback


image_save_dir = 'public/images/'

def worker(args):
    
    callback, args = args
    
    try: 
        r = callback(*args)
        return r
    except Exception as e:
        sys.stderr.write('Error worker ' + str(callback) + ' on input: ' + str(args) + '\nReason: ' + str(e) + '\n')
        traceback.print_exc()
        return None

def run(callback, input):

    #ncpu = 1 # debug
    ncpu = len(input)
    pool = multiprocessing.Pool(processes=ncpu)
    
    data = []
    for i in input:
        data.append((callback, i))
    
    r = None
    error = False
    try:
        r = pool.map(worker, iterable=data)
        count = 0
        for v in r:
            if v == None: 
                sys.stderr.write('Fatal error on worker: #' + str(count) + '\n')
                error = True
            count += 1
    except Exception as e:
        sys.stderr.write("Fatal error:" + str(e))
    finally:
        pool.terminate()
        pool.close()
        
    if error:
        return None
    else:
        return r

def get_unshort_url(short_url):
    
    unshort_url = None
    stream = os.popen("curl -sIL " + short_url)
    for line in stream:
        line = line.rstrip('\n')
        if line.startswith('Location'):
            unshort_url = line[10:-1]
            
    return unshort_url

def get_short_url(url):
    
    short_url = None
    
    cmd  = 'curl https://www.googleapis.com/urlshortener/v1/url'
    cmd += ' -H \'Content-Type: application/json\' '
    cmd += ' -d \'{"longUrl": "' + str(url) + '"}\' 2>/dev/null'  
    stream = os.popen(cmd)
    for line in stream:
        line = line.rstrip()
        if line.startswith(' "id": "'):
            short_url = line[8:-2]
            
    return short_url
    
def refresh_url(url):
    
    new_url = None
    if url.endswith('image.png'):
        index =  url[url.rfind('/') + 1:-10]
        if index == "":
            new_url = url.replace('/image.png', '/0_image.png') 
        else:
            new_url = url.replace(  '/' + index + '_image.png', 
                                    '/' + str(int(index) + 1) + '_image.png')
            
    return new_url

def check_and_parse(line, page):
    
    # parse url
    m = re.split('[^!]\[([^\[]*)\]\(([^\)]+)\)', line)
    nindex = 3
    gindex = 0
    images = []
    while len(m) > (gindex + 1) * nindex:
        
        meta = m[gindex * nindex + 1]
        url = m[gindex * nindex + 2]
        
        if '#' in url:
            idx = url.index('#')
            new_url = url[:idx] + '.html' + re.sub('-+', '-', url[idx:]).lower().replace('_', '-')
        else:
            new_url = url + '.html'
        line = line.replace('[' + meta + '](' + url +')',
                                '[' + meta + '](' + new_url +')')
        gindex += 1
    
    # parse images
    m = re.split('!\[([^\[]*)\]\(([^\)]+)\)', line)
    nindex = 3
    gindex = 0
    images = []
    while len(m) > (gindex + 1) * nindex:
        
        meta = m[gindex * nindex + 1]
        url = m[gindex * nindex + 2]
            
        #new_url = refresh_url(url)
        new_url = fetch_image(url, page, meta)
        if new_url == None:
            return None, None

        if new_url != None:
            line = line.replace('![' + meta + '](' + url +')',
                                '![' + meta + '](' + new_url +')')
            images.append(new_url)
            
        gindex += 1
        
    return line, images

def lucidchart_url(url, local):
    lc_url_begin = 'https://www.lucidchart.com/publicSegments/view/'
    if url[:len(lc_url_begin)] == lc_url_begin:
        return url
    else:
        if local in url:
            if '_' not in url:
                return lc_url_begin + url.replace(local, '').replace('.png', '') + '/image.png'
            else:
                assert False
                a = lc_url_begin + url.replace(local, '') 
                a = a[a.index('_') + 1:-4]
                return a + '/image.png'
        else:
            return lc_url_begin + url.replace('public/images', '').replace('.png', '') + '/image.png'

def lucidchart_id(url):
    lc_url_begin = 'https://www.lucidchart.com/publicSegments/view/'
    assert url[:len(lc_url_begin)] == lc_url_begin
    name = url.replace(lc_url_begin, '')
    name = name[:name.rfind('/')]
    return name


def clean(name):
    
    if len(name) == 0:
        name = 'hadoop_internals'
    
    ids = ''
    i = 0
    while i < len(name):
        if name[i].isalpha() or name[i].isdigit():
            ids += name[i]
        else:
            ids += '-'    
        
        i += 1
    
    ids = re.sub('-+', '-', ids).lower()
    if ids[0] == '-': ids = ids[1:]
    if ids[len(ids) - 1] == '-': ids = ids[:len(ids) - 1]
    
    return ids

def fetch_image(url, page, meta):
    
    global image_save_dir
    
    #print "Fetching image: " + url
    save_dir = image_save_dir
    url = lucidchart_url(url, save_dir)
    
    #print url
    response = urllib2.urlopen(url)
    img_content = response.read()
    id = lucidchart_id(url)
    #print id
    name = save_dir + clean(meta) + '_' + id + '.png'
    
    with open(name, 'wb') as o:
        o.write(img_content)

    return name

def generate_sitemap(site_url, pages = []):
    
    header = '''<?xml version="1.0" encoding="UTF-8"?>
 <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
'''
    print header
    for i in range(len(pages)):
        
        p = pages[i][0]
        images = pages[i][1]
        
        if p == '_Header': continue
        if p == 'AllFiles': continue
        if p == 'Home': p = ''
        
        print '<url>'
        if len(p) > 0:
            print '\t<loc>' + site_url + p + '.html</loc>'
        else:
            print '\t<loc>' + site_url + '</loc>'
        for im in images:
            im = im.replace(site_url, '')
            print '\t<image:image><image:loc>' + site_url + im + '</image:loc></image:image>'
        print '\t<priority>0.5</priority>'
        print '\t<changefreq>weekly</changefreq>'
        print '</url>'
        
    print '</urlset>'

def process_page(f, out_dir):
    #print "Processing: " + f
    content = ""
    images = []
    with open(f, 'rb') as i:
        for line in i:
            result, i = check_and_parse(line, f)
            if result == None:
                print "Failed to process: " + f
                print "At line: " + line
                sys.exit(1)
                
            images += i
            content += result
    
    with open(out_dir + '/' + os.path.basename(f), 'wb') as o:
        o.write(content)
    
    return (os.path.basename(f[2:-3]), images)

def refresh_images(in_dir, out_dir):

    site_url = 'http://ercoppa.github.io/HadoopInternals/'
    data = []
    os.system('rm ' + image_save_dir + '/*.png 2>/dev/null')
    os.system('mkdir ' + image_save_dir + ' 2>/dev/null')

    for f in glob.glob(in_dir + '/*.md'):
        data.append((f, out_dir))
        
    pages = run(process_page, data)
    if pages != None:
        #print pages
        #print "Generating sitemap"
        with open('public/sitemap.xml', 'wb') as o:
            sys.stdout = o
            generate_sitemap(site_url, pages)
            sys.stdout = sys.__stdout__
