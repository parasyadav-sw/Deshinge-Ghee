#!/usr/bin/env python3
import os

BASE = 'E:\\Deshinge-Ghee\\pages'

# Fix home.html
filepath = os.path.join(BASE, 'home.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('product_jowar-sorghum-atta-desi-dagdi-stoneground-2kg-1.html', 'product_amorearth-desi-cow-a2-ghee.html')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed home.html')

# Fix index.html
filepath = os.path.join(BASE, 'index.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('product_date-palm-ghee-solid-pure-date-palm-sap-1-kg.html', 'product_full-moon-ghee.html')
content = content.replace('product_amlaprash-500-gms.html', 'product_buffalo-ghee-a2-cultured.html')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed index.html')

# Fix pages_shop-by-concern.html
filepath = os.path.join(BASE, 'pages_shop-by-concern.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

non_ghee_products = [
    'protein-atta', 'khapli-emmer-long-wheat-atta-stoneground-2kg', 'khapli-multigrain-atta',
    'date-palm-jaggery-solid-pure-date-palm-sap-1-kg', 'wood-pressed-organic-groundnut-peanut-oil-1litre-bottle',
    'amlaprash-500-gms', 'black-mustard-oil', 'crushed-organic-jaggery-500-gms-pack-granular-form',
    'two-brothers-organic-farms-amorearth-jaggery', 'sunflower-oil', 'virgin-coconut-oil-cold-pressed-single-filtered',
    'coconut-oil-wood-pressed-unrefined', 'cold-pressed-groundnut-oil-spray', 'amorearth-stone-ground-sattu-atta',
    'rajgira-atta', 'sprouted-ragi-malt-nachni-satva', 'truemato-ketchup', 'golden-milk-mix',
    'single-origin-lakadong-turmeric-powder-150g', 'khapli-emmer-long-wheat-grains-stoneground-1kg',
    'two-brothers-organic-farms-amorearth-moringa-powder', 'forest-honey', 'acacia-honey',
    'organic-turmeric-haldi-stone-grinded', 'pink-himalayan-rock-salt', 'amorearth-chywanprash-500-gms',
    'jowar-sorghum-atta-desi-dagdi-stoneground-2kg-1',
]

for product in non_ghee_products:
    content = content.replace(f'product_{product}.html', 'product_amorearth-desi-cow-a2-ghee.html')
    content = content.replace(f'product_{product}?view=', 'product_amorearth-desi-cow-a2-ghee?view=')
    content = content.replace(f'handle="{product}"', 'handle="amorearth-desi-cow-a2-ghee"')
    content = content.replace(f'data-product-handle="{product}"', 'data-product-handle="amorearth-desi-cow-a2-ghee"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed pages_shop-by-concern.html')
