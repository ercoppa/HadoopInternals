import sys
import re
import os
import glob
import refresh_image_cache

def clean(name):
    
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

def add_toc(content, urls):
    if len(urls) > 0 and '[toc]\n' in content:
        
        #print urls
        toc  = '#### Table of contents:\n'
        for url in urls:
            #print url
            toc += ' * [' + url[0] + '](#' + url[1] + ')\n'
        
        content = content.replace('[toc]\n', toc)

    return content        

def add_anchor(line_o):
    line = line_o.rstrip()
    
    url = ""
    i = 0
    bspace = 0
    sharp = 0
    
    while i < len(line):
        if line[i] == ' ':
            bspace += 1
            url += ' '
        else:
            break
        i += 1
    
    while i < len(line):
        if line[i] == '#':
            url += '#'
            sharp += 1
        else:
            break
        i += 1
    
    if sharp == 0: return line_o, []
    if line[i] != ' ': return line_o, []
    else: i += 1
    
    url += ' '
    name = str(line_o[i:])
    
    m = re.split('<a href="[^\"]+" id="[^\"]+">(.+)</a>', name)
    if len(m) > 1:
        name = m[1]
    elif len(m) == 1:
        pass
    else:
        sys.stderr.write('Invalid input: ' + line_o)
        sys.exit(1)
    
    ids = clean(name)
    url += '<a href="#' + str(ids) + '" id="' + str(ids) + '">' + name + '</a>'
    
    return url, [name, ids]

def get_header(f, title):
    
    if title == '': 
        title = os.path.basename(f).replace('.md', '')
    
    title = title.replace(':', ' -')
    
    h  = '---\n'
    h += 'layout: post\n'
    h += 'title: ' + title + '\n'
    h += '---\n'
    return h

def process_md(finput, foutput):

    title = ''
    urls = []
    with open(finput, 'rb') as i:

        content = ''
        
        j = 0
        header = False    
        for line in i:
            line = line.strip('\n').strip('\r')
            
            if j == 0 and len(line) > 0 and line[0] == '#':
                title = line.replace('#', '').strip(' ')
                #print title
                #content += line + '\n'
            else:
                if len(line) > 0:
                    c, url = add_anchor(line)
                    content += c + '\n'
                    if len(url) > 0:
                        urls.append(url)
                else:
                    content += line + '\n'
                    
            j += 1
                
    
    content = add_toc(content, urls)
    
    with open(foutput, 'wb+') as o:
        content = get_header(finput, title) + content
        o.write(content)

def get_post_name(finput):
    name = os.path.basename(f)
    if name == 'Home.md':
        return '2014-04-01-' + name 
    else:
        return '2014-04-02-' + name

in_dir = '_sources'
out_dir = '_posts'
os.system('rm ' + out_dir + '/*.md 2>/dev/null')

refresh_image_cache.refresh_images(in_dir, out_dir)

for f in glob.glob(out_dir + '/*.md'):
    fname = get_post_name(f)
    process_md(f, out_dir + '/' + fname)
    os.system('rm ' + f)
