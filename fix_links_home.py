import re
import os

fpath = r'C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages\home.html'

with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Map original paths to local filenames (all in same pages/ directory)
link_map = {
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
    '/pages/farmer-diaries': 'pages_farmer-diaries.html',
    '/pages/gifting': 'pages_gifting.html',
    '/policies/refund-policy': 'policies_refund-policy.html',
    '/blogs/all-blogs': 'blogs_all-blogs.html',
    '/': 'home.html',
}

# Product pages
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

# Apply replacements - href="..." and href='...'
for old_path, new_file in link_map.items():
    content = content.replace(f'href="{old_path}"', f'href="{new_file}"')
    content = content.replace(f"href='{old_path}'", f"href='{new_file}'")

# Fix remaining /collections/ and /pages/ links
content = re.sub(r'href="/collections/([^"]+)"', r'href="collections_\1.html"', content)
content = re.sub(r'href="/pages/([^"]+)"', r'href="pages_\1.html"', content)
content = re.sub(r'href="/products/([^"]+)"', r'href="product_\1.html"', content)
content = re.sub(r"href='/collections/([^']+)'", r"href='collections_\1.html'", content)
content = re.sub(r"href='/pages/([^']+)'", r"href='pages_\1.html'", content)
content = re.sub(r"href='/products/([^']+)'", r"href='product_\1.html'", content)

# Fix href="/" -> home.html
content = content.replace('href="/"', 'href="home.html"')
content = content.replace("href='/'", "href='home.html'")

# Remove action buttons that go nowhere
content = content.replace('action="/cart/add"', 'action="#"')
content = content.replace('action="/cart/change"', 'action="#"')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Fixed all links in home.html')
print(f'File size: {os.path.getsize(fpath) / 1024:.0f} KB')
