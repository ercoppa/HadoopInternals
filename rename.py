import glob
import os

for f in glob.glob("*.md"):
    if f[0] != "2":
        print f
        os.system("mv " + f + " 2014-04-05-" + f)
