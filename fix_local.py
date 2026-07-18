import os
import glob
import re

pages_dir = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages'
count = 0

for fpath in glob.glob(os.path.join(pages_dir, '*.html')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content

    # Replace CSS links with local paths
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/theme.css', 'assets/theme.css')
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/style.css', 'assets/style.css')
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/new-custom-style.css', 'assets/new-custom-style.css')
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/critical-css.css', 'assets/critical-css.css')

    # Replace remaining external asset references
    content = content.replace('https://twobrothersindiashop.com/cdn/shop/t/795/assets/', 'assets/')
    content = content.replace('//twobrothersindiashop.com/cdn/shop/t/795/assets/', 'assets/')

    # Remove blocking external scripts
    patterns = [
        r'<script[^>]*src="[^"]*googletagmanager[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*google-analytics[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*shopflo[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*support\.js[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*rewards\.js[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*whatsapp\.js[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*eventpromotionbar[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*nitrocommerce[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*buckscc[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*merchantwidget[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*twobrothersindiashop\.com[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*cdn\.shopify\.com[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*google\.com[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*jquery[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*bonb\.io[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*gstatic\.com[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*bridge\.shopflo\.com[^"]*"[^>]*></script>',
        r'<script[^>]*src="[^"]*hextom\.com[^"]*"[^>]*></script>',
    ]
    for p in patterns:
        content = re.sub(p, '', content)

    # Remove GTM inline blocks
    content = re.sub(r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->', '', content, flags=re.DOTALL)

    # Remove preconnect/dns-prefetch
    content = re.sub(r'<link[^>]*rel="preconnect"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="dns-prefetch"[^>]*>', '', content)

    # Remove meta verification tags
    content = re.sub(r'<meta[^>]*google-site-verification[^>]*>', '', content)
    content = re.sub(r'<meta[^>]*facebook-domain-verification[^>]*>', '', content)

    # Remove preload for external scripts
    content = re.sub(r'<link[^>]*rel="preload"[^>]*as="script"[^>]*>', '', content)

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Cleaned: {os.path.basename(fpath)}')

print(f'\nTotal files cleaned: {count}')
