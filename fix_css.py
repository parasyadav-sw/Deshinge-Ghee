import os
import glob

pages_dir = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages'
count = 0

for fpath in glob.glob(os.path.join(pages_dir, '*.html')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content
    
    # Global replace: //twobrothersindiashop.com -> https://twobrothersindiashop.com
    content = content.replace('//twobrothersindiashop.com', 'https://twobrothersindiashop.com')
    
    # Global replace: //cdn.shopify.com -> https://cdn.shopify.com
    content = content.replace('//cdn.shopify.com', 'https://cdn.shopify.com')
    
    # Fix any remaining double https://https://
    content = content.replace('https://https://', 'https://')
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Fixed: {os.path.basename(fpath)}')

print(f'\nTotal files fixed: {count}')
