import os
import re
import glob

pages_dir = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages'

CSS_BLOCK = """
    <link rel="stylesheet" href="../assets/critical-css.css">
    <link rel="stylesheet" href="../assets/theme.css">
    <link rel="stylesheet" href="../assets/style.css">
    <link rel="stylesheet" href="../assets/new-custom-style.css">
"""

count = 0
for fpath in glob.glob(os.path.join(pages_dir, '*.html')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content

    # Remove ALL broken stylesheet links (href="#")
    content = re.sub(r'<link[^>]*href="#"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*href=\'#\'[^>]*>', '', content)

    # Find </head> and insert CSS before it
    head_close = content.find('</head>')
    if head_close != -1:
        # Check if CSS is already there
        if '../assets/theme.css' not in content and 'assets/theme.css' not in content:
            content = content[:head_close] + CSS_BLOCK + content[head_close:]
    
    # Also handle files that had no </head> (unlikely but safe)
    if '</head>' not in content and '<head>' in content:
        head_open = content.find('<head>') + 6
        if '../assets/theme.css' not in content:
            content = content[:head_open] + CSS_BLOCK + content[head_open:]

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Injected CSS: {os.path.basename(fpath)}')

print(f'\nTotal files fixed: {count}')
