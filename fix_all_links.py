import re
import os

pages_dir = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages'

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
    '/policies/refund-policy': 'policies_refund-policy.html',
    '/blogs/all-blogs': 'blogs_all-blogs.html',
}

product_slugs = [
    'amorearth-desi-cow-a2-ghee', 'khapli-emmer-long-wheat-atta-stoneground-2kg',
    'wood-pressed-organic-groundnut-peanut-oil-1litre-bottle', 'protein-atta',
    'khapli-multigrain-atta', 'date-palm-jaggery-solid-pure-date-palm-sap-1-kg',
    'two-brothers-organic-farms-amorearth-jaggery', 'crushed-organic-jaggery-500-gms-pack-granular-form',
    'black-mustard-oil', 'sunflower-oil', 'virgin-coconut-oil-cold-pressed-single-filtered',
    'coconut-oil-wood-pressed-unrefined', 'cold-pressed-groundnut-oil-spray', 'amlaprash-500-gms',
    'full-moon-ghee', 'buffalo-ghee-a2-cultured', 'tulsi-ghee-herbal-ghee-daily-care-wellness',
    'shatavari-ghee-a2-cultured-250-gms', 'brahmi-ghee-a2-cultured-250-gms',
    'sprouted-ragi-malt-nachni-satva', 'rajgira-atta', 'amorearth-stone-ground-sattu-atta',
    'golden-milk-mix', 'truemato-ketchup', 'single-origin-lakadong-turmeric-powder-150g',
    'khapli-emmer-long-wheat-grains-stoneground-1kg', 'jowar-sorghum-atta-desi-dagdi-stoneground-2kg-1',
    'pink-himalayan-rock-salt', 'two-brothers-organic-farms-amorearth-moringa-powder',
    'organic-turmeric-haldi-stone-grinded', 'amorearth-chywanprash-500-gms',
    'forest-honey', 'acacia-honey-raw',
]
for slug in product_slugs:
    link_map[f'/products/{slug}'] = f'product_{slug}.html'

count = 0
for fname in os.listdir(pages_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content

    # Replace explicit mappings
    for old_path, new_file in link_map.items():
        content = content.replace(f'href="{old_path}"', f'href="{new_file}"')
        content = content.replace(f"href='{old_path}'", f"href='{new_file}'")

    # Fix remaining patterns
    content = re.sub(r'href="/collections/([^"]+)"', r'href="collections_\1.html"', content)
    content = re.sub(r'href="/pages/([^"]+)"', r'href="pages_\1.html"', content)
    content = re.sub(r'href="/products/([^"]+)"', r'href="product_\1.html"', content)
    content = re.sub(r"href='/collections/([^']+)'", r"href='collections_\1.html'", content)
    content = re.sub(r"href='/pages/([^']+)'", r"href='pages_\1.html'", content)
    content = re.sub(r"href='/products/([^']+)'", r"href='product_\1.html'", content)
    content = content.replace('href="/"', 'href="home.html"')

    # Fix CSS paths for pages/ subfolder
    content = content.replace('href="assets/', 'href="../assets/')
    content = content.replace("href='assets/", "href='../assets/")

    # Fix form actions
    content = content.replace('action="/cart/add"', 'action="#"')
    content = content.replace('action="/cart/change"', 'action="#"')

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Fixed links in {count} files')
