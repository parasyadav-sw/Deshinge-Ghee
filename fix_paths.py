import re
import os

pages_dir = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages'

for fname in os.listdir(pages_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content
    
    # Fix CSS paths: assets/ -> ../assets/
    content = content.replace('href="assets/', 'href="../assets/')
    content = content.replace("href='assets/", "href='../assets/")
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed CSS paths: {fname}')

print('Done')
