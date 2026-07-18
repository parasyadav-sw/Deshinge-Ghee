import re
import os

files = [
    r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages\index.html',
    r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages\collections_all.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/theme.css', 'assets/theme.css')
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/style.css', 'assets/style.css')
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/new-custom-style.css', 'assets/new-custom-style.css')
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/critical-css.css', 'assets/critical-css.css')
    content = content.replace('//twobrothersindiashop.com/cdn/shop/t/795/assets/', 'assets/')
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/', 'assets/')
    
    content = re.sub(r'<script[^>]*src="[^"]*googletagmanager[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*shopflo[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*twobrothersindiashop[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*cdn\.shopify[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*bonb\.io[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*hextom[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*gstatic[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*jquery[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*nitrocommerce[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*google[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*bridge\.shopflo[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*buckscc[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<script[^>]*src="[^"]*merchantwidget[^"]*"[^>]*></script>', '', content)
    content = re.sub(r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->', '', content, flags=re.DOTALL)
    content = re.sub(r'<link[^>]*rel="preload"[^>]*as="script"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="preconnect"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="dns-prefetch"[^>]*>', '', content)
    content = re.sub(r'<meta[^>]*google-site-verification[^>]*>', '', content)
    content = re.sub(r'<meta[^>]*facebook-domain-verification[^>]*>', '', content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Fixed: {os.path.basename(fpath)}')
