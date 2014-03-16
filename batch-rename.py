import glob
import os

for file in glob.glob('./sources/png/*New*Page.png'):
    f = file.replace(' - New Page', '')
    os.rename(file, f)

for file in glob.glob('./sources/png/*.png'):
    f = file.replace(' ', '_')
    os.rename(file, f)

for file in glob.glob('./sources/vdx/*.vdx'):
    f = file.replace(' ', '_')
    os.rename(file, f)
