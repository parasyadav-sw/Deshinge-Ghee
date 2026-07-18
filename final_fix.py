import os
import re
import glob

pages_dir = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages'

count = 0
for fpath in glob.glob(os.path.join(pages_dir, '*.html')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content

    # Fix broken double/triple https: patterns
    while 'https:https:' in content:
        content = content.replace('https:https:', 'https:')
    while 'https:assets/' in content:
        content = content.replace('https:assets/', '../assets/')
    while 'https://assets/' in content:
        content = content.replace('https://assets/', '../assets/')
    while 'http:assets/' in content:
        content = content.replace('http:assets/', '../assets/')

    # Remove ALL broken href="#" stylesheet links
    content = re.sub(r'<link[^>]*href="#"[^>]*/?\s*>', '', content)

    # Ensure CSS block exists before </head>
    if '../assets/theme.css' not in content:
        head_close = content.find('</head>')
        if head_close != -1:
            css_block = (
                '\n    <link rel="stylesheet" href="../assets/critical-css.css">\n'
                '    <link rel="stylesheet" href="../assets/theme.css">\n'
                '    <link rel="stylesheet" href="../assets/style.css">\n'
                '    <link rel="stylesheet" href="../assets/new-custom-style.css">\n'
            )
            content = content[:head_close] + css_block + content[head_close:]

    # Remove blocking external scripts  
    script_removals = [
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
    for p in script_removals:
        content = re.sub(p, '', content)
    
    content = re.sub(r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->', '', content, flags=re.DOTALL)
    content = re.sub(r'<link[^>]*rel="preload"[^>]*as="script"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="preconnect"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="dns-prefetch"[^>]*>', '', content)
    content = re.sub(r'<meta[^>]*google-site-verification[^>]*>', '', content)
    content = re.sub(r'<meta[^>]*facebook-domain-verification[^>]*>', '', content)

    # Fix remaining external link patterns
    content = content.replace('href="//twobrothersindiashop.com/', 'href="')
    content = content.replace("href='//twobrothersindiashop.com/", "href='")

    # Fix all internal links
    link_map = {
        '/': 'home.html',
        '/collections/ghee': 'collections_ghee.html',
        '/collections/all': 'collections_all.html',
        '/collections/atta': 'collections_atta.html',
        '/collections/wood-pressed-oils': 'collections_wood-pressed-oils.html',
        '/collections/natural-sweetners': 'collections_natural-sweetners.html',
        '/collections/spices': 'collections_spices.html',
        '/collections/immunity': 'collections_immunity.html',
        '/collections/new-launches': 'collections_new-launches.html',
        '/collections/rice': 'collections_rice.html',
        '/collections/breakfast-spreads': 'collections_breakfast-spreads.html',
        '/collections/pulses': 'collections_pulses.html',
        '/collections/diabetes-care': 'collections_diabetes-care.html',
        '/collections/gluten-free-gut-health': 'collections_gluten-free-gut-health.html',
        '/collections/weight-loss': 'collections_weight-loss.html',
        '/collections/pantry-essentials': 'collections_pantry-essentials.html',
        '/collections/our-best-sellers': 'collections_our-best-sellers.html',
        '/collections/value-combos': 'collections_value-combos.html',
        '/collections/under-999': 'collections_under-999.html',
        '/collections/monsoon-special': 'collections_monsoon-special.html',
        '/collections/price-drop': 'collections_price-drop.html',
        '/collections/summer': 'collections_summer.html',
        '/collections/handmade-pickles': 'collections_handmade-pickles.html',
        '/collections/healthy-snacks': 'collections_healthy-snacks.html',
        '/pages/our-philosophy': 'pages_our-philosophy.html',
        '/pages/contact-us': 'pages_contact-us.html',
        '/pages/about-us': 'pages_about-us.html',
        '/pages/farm-visit': 'pages_farm-visit.html',
        '/pages/membership': 'pages_membership.html',
        '/pages/shipping-and-delivery-policy': 'pages_shipping-and-delivery-policy.html',
        '/pages/shop-by-concern': 'pages_shop-by-concern.html',
        '/pages/founders-and-team': 'pages_founders-and-team.html',
        '/pages/awards': 'pages_awards.html',
        '/pages/tbof-traceability': 'pages_tbof-traceability.html',
        '/pages/health-of-people-and-planet': 'pages_health-of-people-and-planet.html',
        '/pages/team-on-ground': 'pages_team-on-ground.html',
        '/pages/events': 'pages_events.html',
        '/pages/quality-assurance': 'pages_quality-assurance.html',
        '/pages/tbof-testimonials': 'pages_tbof-testimonials.html',
        '/pages/our-team': 'pages_our-team.html',
        '/pages/csr-activities': 'pages_csr-activities.html',
        '/pages/farmers-markets': 'pages_farmers-markets.html',
        '/pages/contact': 'pages_contact.html',
        '/pages/career': 'pages_career.html',
        '/pages/customer-feedback-1': 'pages_customer-feedback-1.html',
        '/pages/international-orders': 'pages_international-orders.html',
        '/pages/work-with-farmers': 'pages_work-with-farmers.html',
        '/pages/workshops-lectures': 'pages_workshops-lectures.html',
        '/pages/collaborations': 'pages_collaborations.html',
        '/pages/soil-health': 'pages_soil-health.html',
        '/pages/conscious-cattle-rearing': 'pages_conscious-cattle-rearing.html',
        '/pages/impact-recognition': 'pages_impact-recognition.html',
        '/pages/our-community': 'pages_our-community.html',
        '/pages/gifting': 'pages_gifting.html',
        '/policies/refund-policy': 'policies_refund-policy.html',
        '/blogs/all-blogs': 'blogs_all-blogs.html',
    }
    for old, new in link_map.items():
        content = content.replace(f'href="{old}"', f'href="{new}"')
        content = content.replace(f"href='{old}'", f"href='{new}'")

    content = re.sub(r'href="/collections/([^"]+?)(?:\?[^"]*)?"', r'href="collections_\1.html"', content)
    content = re.sub(r'href="/pages/([^"]+?)(?:\?[^"]*)?"', r'href="pages_\1.html"', content)
    content = re.sub(r'href="/products/([^"]+?)(?:\?[^"]*)?"', r'href="product_\1.html"', content)
    content = re.sub(r"href='/collections/([^']+?)(?:\?[^']*)?'", r"href='collections_\1.html'", content)
    content = re.sub(r"href='/pages/([^']+?)(?:\?[^']*)?'", r"href='pages_\1.html'", content)
    content = re.sub(r"href='/products/([^']+?)(?:\?[^']*)?'", r"href='product_\1.html'", content)
    content = content.replace('href="/"', 'href="home.html"')

    content = content.replace('action="/cart/add"', 'action="#"')
    content = content.replace('action="/cart/change"', 'action="#"')

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Final fix: {count} files processed')
print(f'Total files: {len(glob.glob(os.path.join(pages_dir, "*.html")))}')
