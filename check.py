import os
import re

fpath = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages\collections_ghee.html'
with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

links = re.findall(r'<link[^>]*stylesheet[^>]*>', content)
for l in links:
    print(l[:300])

print('---')
print('File size:', len(content), 'bytes')
print('Has theme.css:', 'theme.css' in content)
print('Has style.css:', 'style.css' in content)
print('Has stylesheet:', 'stylesheet' in content)
