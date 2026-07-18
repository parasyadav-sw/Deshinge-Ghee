import re
import os

fpath = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages\home.html'

with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Fix CSS to local
content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/theme.css', 'assets/theme.css')
content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/style.css', 'assets/style.css')
content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/new-custom-style.css', 'assets/new-custom-style.css')
content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/critical-css.css', 'assets/critical-css.css')
content = content.replace('//twobrothersindiashop.com/cdn/shop/t/795/assets/', 'assets/')
content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/', 'assets/')

# Fix image CDN refs
content = content.replace('//twobrothersindiashop.com/cdn/shop/', 'https://twobrothersindiashop.com/cdn/shop/')
content = content.replace('https://twobrothersindiashop.com/cdn/shop/files/', 'https://twobrothersindiashop.com/cdn/shop/files/')
content = content.replace('https://twobrothersindiashop.com/cdn/shop/products/', 'https://twobrothersindiashop.com/cdn/shop/products/')

# Remove blocking external scripts
script_patterns = [
    r'<script[^>]*src="[^"]*googletagmanager[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*shopflo[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*twobrothersindiashop\.com[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*cdn\.shopify\.com[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*bonb\.io[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*hextom[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*gstatic[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*jquery[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*nitrocommerce[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*google[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*bridge\.shopflo[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*buckscc[^"]*"[^>]*></script>',
    r'<script[^>]*src="[^"]*merchantwidget[^"]*"[^>]*></script>',
]
for p in script_patterns:
    content = re.sub(p, '', content)

# Remove GTM blocks
content = re.sub(r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->', '', content, flags=re.DOTALL)

# Remove preload for scripts
content = re.sub(r'<link[^>]*rel="preload"[^>]*as="script"[^>]*>', '', content)
content = re.sub(r'<link[^>]*rel="preconnect"[^>]*>', '', content)
content = re.sub(r'<link[^>]*rel="dns-prefetch"[^>]*>', '', content)

# Remove verification meta
content = re.sub(r'<meta[^>]*google-site-verification[^>]*>', '', content)
content = re.sub(r'<meta[^>]*facebook-domain-verification[^>]*>', '', content)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Fixed: {fpath}')
print(f'File size: {os.path.getsize(fpath) / 1024:.1f} KB')
