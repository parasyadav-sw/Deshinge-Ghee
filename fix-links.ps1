# Script to replace external links with local links
$pagesDir = "C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference\pages"

# URL mapping - external path to local file
$urlMap = @{
    "/" = "pages/index.html"
    "/collections/all" = "pages/collections_all.html"
    "/collections/ghee" = "pages/collections_ghee.html"
    "/collections/atta" = "pages/collections_atta.html"
    "/collections/wood-pressed-oils" = "pages/collections_wood-pressed-oils.html"
    "/collections/natural-sweetners" = "pages/collections_natural-sweetners.html"
    "/collections/spices" = "pages/collections_spices.html"
    "/collections/immunity" = "pages/collections_immunity.html"
    "/collections/new-launches" = "pages/collections_new-launches.html"
    "/collections/rice" = "pages/collections_rice.html"
    "/pages/our-philosophy" = "pages/pages_our-philosophy.html"
    "/pages/contact-us" = "pages/pages_contact-us.html"
    "/pages/about-us" = "pages/pages_about-us.html"
    "/pages/farm-visit" = "pages/pages_farm-visit.html"
    "/pages/membership" = "pages/pages_membership.html"
    "/pages/shipping-and-delivery-policy" = "pages/pages_shipping-and-delivery-policy.html"
    "/policies/refund-policy" = "pages/policies_refund-policy.html"
    "/blogs/all-blogs" = "pages/blogs_all-blogs.html"
    "/pages/shop-by-concern" = "pages/pages_shop-by-concern.html"
    "/collections/diabetes-care" = "pages/collections_diabetes-care.html"
    "/collections/gluten-free-gut-health" = "pages/collections_gluten-free-gut-health.html"
    "/collections/weight-loss" = "pages/collections_weight-loss.html"
    "/collections/breakfast-spreads" = "pages/collections_breakfast-spreads.html"
    "/collections/pulses" = "pages/collections_pulses.html"
    "/collections/pantry-essentials" = "pages/collections_pantry-essentials.html"
    "/collections/our-best-sellers" = "pages/collections_our-best-sellers.html"
    "/collections/value-combos" = "pages/collections_value-combos.html"
    "/collections/under-999" = "pages/collections_under-999.html"
    "/collections/monsoon-special" = "pages/collections_monsoon-special.html"
    "/collections/price-drop" = "pages/collections_price-drop.html"
    "/collections/summer" = "pages/collections_summer.html"
    "/collections/handmade-pickles" = "pages/collections_handmade-pickles.html"
    "/collections/healthy-snacks" = "pages/collections_healthy-snacks.html"
    "/pages/founders-and-team" = "pages/pages_founders-and-team.html"
    "/pages/awards" = "pages/pages_awards.html"
    "/pages/tbof-traceability" = "pages/pages_tbof-traceability.html"
    "/pages/health-of-people-and-planet" = "pages/pages_health-of-people-and-planet.html"
    "/pages/team-on-ground" = "pages/pages_team-on-ground.html"
    "/pages/events" = "pages/pages_events.html"
    "/pages/quality-assurance" = "pages/pages_quality-assurance.html"
    "/pages/tbof-testimonials" = "pages/pages_tbof-testimonials.html"
    "/pages/our-team" = "pages/pages_our-team.html"
    "/pages/csr-activities" = "pages/pages_csr-activities.html"
    "/pages/farmers-markets" = "pages/pages_farmers-markets.html"
    "/pages/contact" = "pages/pages_contact.html"
    "/pages/career" = "pages/pages_career.html"
    "/pages/customer-feedback-1" = "pages/pages_customer-feedback-1.html"
    "/pages/international-orders" = "pages/pages_international-orders.html"
    "/pages/work-with-farmers" = "pages/pages_work-with-farmers.html"
    "/pages/workshops-lectures" = "pages/pages_workshops-lectures.html"
    "/pages/collaborations" = "pages/pages_collaborations.html"
    "/pages/soil-health" = "pages/pages_soil-health.html"
    "/pages/conscious-cattle-rearing" = "pages/pages_conscious-cattle-rearing.html"
    "/pages/impact-recognition" = "pages/pages_impact-recognition.html"
    "/pages/our-community" = "pages/pages_our-community.html"
    "/pages/farmer-diaries-a-quarterly-magazine-by-tbof" = "pages/pages_farmer-diaries.html"
    "/pages/gifting" = "pages/pages_gifting.html"
}

# Also map product pages (we'll create placeholder pages)
$productPages = @(
    "/products/amorearth-desi-cow-a2-ghee",
    "/products/khapli-emmer-long-wheat-atta-stoneground-2kg",
    "/products/wood-pressed-organic-groundnut-peanut-oil-1litre-bottle",
    "/products/protein-atta",
    "/products/khapli-multigrain-atta",
    "/products/date-palm-jaggery-solid-pure-date-palm-sap-1-kg",
    "/products/two-brothers-organic-farms-amorearth-jaggery",
    "/products/crushed-organic-jaggery-500-gms-pack-granular-form",
    "/products/black-mustard-oil",
    "/products/sunflower-oil",
    "/products/virgin-coconut-oil-cold-pressed-single-filtered",
    "/products/coconut-oil-wood-pressed-unrefined",
    "/products/cold-pressed-groundnut-oil-spray",
    "/products/amlaprash-500-gms",
    "/products/full-moon-ghee",
    "/products/buffalo-ghee-a2-cultured",
    "/products/tulsi-ghee-herbal-ghee-daily-care-wellness",
    "/products/shatavari-ghee-a2-cultured-250-gms",
    "/products/brahmi-ghee-a2-cultured-250-gms",
    "/products/sprouted-ragi-malt-nachni-satva",
    "/products/rajgira-atta",
    "/products/amorearth-stone-ground-sattu-atta",
    "/products/golden-milk-mix",
    "/products/truemato-ketchup",
    "/products/single-origin-lakadong-turmeric-powder-150g",
    "/products/khapli-emmer-long-wheat-grains-stoneground-1kg",
    "/products/jowar-sorghum-atta-desi-dagdi-stoneground-2kg-1",
    "/products/pink-himalayan-rock-salt",
    "/products/two-brothers-organic-farms-amorearth-moringa-powder",
    "/products/organic-turmeric-haldi-stone-grinded",
    "/products/amorearth-chywanprash-500-gms",
    "/products/forest-honey",
    "/products/acacia-honey-raw"
)

foreach ($p in $productPages) {
    $slug = $p -replace "/products/", ""
    $urlMap[$p] = "pages/product_$slug.html"
}

# Create a simple product placeholder page function
function Create-ProductPage {
    param($slug, $title)
    $html = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title - Reference</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 40px; background: #fcfaf8; color: #282828; }
        .placeholder { text-align: center; padding: 100px 20px; border: 2px dashed #ccc; margin: 20px 0; }
        a { color: #2a431c; }
        nav { background: #2a431c; padding: 15px; margin-bottom: 20px; }
        nav a { color: white; margin: 0 15px; text-decoration: none; }
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="collections_all.html">All Products</a>
        <a href="collections_ghee.html">Ghee</a>
        <a href="collections_atta.html">Atta</a>
        <a href="collections_wood-pressed-oils.html">Oils</a>
        <a href="pages_our-philosophy.html">Philosophy</a>
        <a href="pages_contact-us.html">Contact</a>
    </nav>
    <div class="placeholder">
        <h1>$title</h1>
        <p>This is a reference placeholder for the product page: <strong>$slug</strong></p>
        <p><a href="collections_all.html">Back to All Products</a></p>
    </div>
</body>
</html>
"@
    return $html
}

# Create product placeholder pages
$productTitles = @{
    "amorearth-desi-cow-a2-ghee" = "Desi Gir Cow Cultured Ghee"
    "khapli-emmer-long-wheat-atta-stoneground-2kg" = "Khapli Wheat Atta"
    "wood-pressed-organic-groundnut-peanut-oil-1litre-bottle" = "Groundnut Oil"
    "protein-atta" = "High Protein Khapli Atta"
    "khapli-multigrain-atta" = "Khapli Multigrain Atta"
    "date-palm-jaggery-solid-pure-date-palm-sap-1-kg" = "Date Palm Jaggery"
    "two-brothers-organic-farms-amorearth-jaggery" = "Sugarcane Jaggery Block"
    "crushed-organic-jaggery-500-gms-pack-granular-form" = "Sugarcane Jaggery Crushed"
    "black-mustard-oil" = "Black Mustard Oil"
    "sunflower-oil" = "Sunflower Oil"
    "virgin-coconut-oil-cold-pressed-single-filtered" = "Virgin Coconut Oil"
    "coconut-oil-wood-pressed-unrefined" = "Coconut Oil"
    "cold-pressed-groundnut-oil-spray" = "Cold-Pressed Groundnut Oil Spray"
    "amlaprash-500-gms" = "Amlaprash"
    "full-moon-ghee" = "Full Moon Cultured Ghee"
    "buffalo-ghee-a2-cultured" = "Buffalo Ghee"
    "tulsi-ghee-herbal-ghee-daily-care-wellness" = "Tulsi Ghee"
    "shatavari-ghee-a2-cultured-250-gms" = "Shatavari Ghee"
    "brahmi-ghee-a2-cultured-250-gms" = "Brahmi Ghee"
    "sprouted-ragi-malt-nachni-satva" = "Sprouted Ragi Flour"
    "rajgira-atta" = "Sprouted Rajgira Atta"
    "amorearth-stone-ground-sattu-atta" = "Sattu Atta"
    "golden-milk-mix" = "Golden Milk Mix"
    "truemato-ketchup" = "Truemato Ketchup"
    "single-origin-lakadong-turmeric-powder-150g" = "Lakadong Turmeric"
    "khapli-emmer-long-wheat-grains-stoneground-1kg" = "Khapli Wheat Grains"
    "jowar-sorghum-atta-desi-dagdi-stoneground-2kg-1" = "Jowar Atta"
    "pink-himalayan-rock-salt" = "Pink Himalayan Rock Salt"
    "two-brothers-organic-farms-amorearth-moringa-powder" = "Moringa Powder"
    "organic-turmeric-haldi-stone-grinded" = "Salem Haldi"
    "amorearth-chywanprash-500-gms" = "TBOF Chyawanprash"
    "forest-honey" = "Forest Honey"
    "acacia-honey-raw" = "Acacia Honey"
}

foreach ($entry in $productTitles.GetEnumerator()) {
    $slug = $entry.Key
    $title = $entry.Value
    $outFile = Join-Path $pagesDir "product_$slug.html"
    if (-not (Test-Path $outFile)) {
        $html = Create-ProductPage -slug $slug -title $title
        $html | Out-File -FilePath $outFile -Encoding UTF8
    }
}

# Also create placeholder pages for missing collection/page links
$missingPages = @(
    "pages_shop-by-concern",
    "collections_diabetes-care",
    "collections_gluten-free-gut-health",
    "collections_weight-loss",
    "collections_breakfast-spreads",
    "collections_pulses",
    "collections_pantry-essentials",
    "collections_our-best-sellers",
    "collections_value-combos",
    "collections_under-999",
    "collections_monsoon-special",
    "collections_price-drop",
    "collections_summer",
    "collections_handmade-pickles",
    "collections_healthy-snacks",
    "pages_founders-and-team",
    "pages_awards",
    "pages_tbof-traceability",
    "pages_health-of-people-and-planet",
    "pages_team-on-ground",
    "pages_events",
    "pages_quality-assurance",
    "pages_tbof-testimonials",
    "pages_our-team",
    "pages_csr-activities",
    "pages_farmers-markets",
    "pages_contact",
    "pages_career",
    "pages_customer-feedback-1",
    "pages_international-orders",
    "pages_work-with-farmers",
    "pages_workshops-lectures",
    "pages_collaborations",
    "pages_soil-health",
    "pages_conscious-cattle-rearing",
    "pages_impact-recognition",
    "pages_our-community",
    "pages_farmer-diaries",
    "pages_gifting"
)

foreach ($page in $missingPages) {
    $outFile = Join-Path $pagesDir "$page.html"
    if (-not (Test-Path $outFile)) {
        $title = ($page -replace "pages_|collections_", "" -replace "-", " ")
        $title = (Get-CultureInfo).TextInfo.ToTitleCase($title)
        $type = if ($page.StartsWith("collections_")) { "Collection" } else { "Page" }
        $html = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title - Reference</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 40px; background: #fcfaf8; color: #282828; }
        .placeholder { text-align: center; padding: 100px 20px; border: 2px dashed #ccc; margin: 20px 0; }
        a { color: #2a431c; }
        nav { background: #2a431c; padding: 15px; margin-bottom: 20px; }
        nav a { color: white; margin: 0 15px; text-decoration: none; }
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="collections_all.html">All Products</a>
        <a href="collections_ghee.html">Ghee</a>
        <a href="collections_atta.html">Atta</a>
        <a href="collections_wood-pressed-oils.html">Oils</a>
        <a href="pages_our-philosophy.html">Philosophy</a>
        <a href="pages_contact-us.html">Contact</a>
    </nav>
    <div class="placeholder">
        <h1>$title</h1>
        <p>This is a reference placeholder for: <strong>$type - $page</strong></p>
        <p><a href="index.html">Back to Home</a></p>
    </div>
</body>
</html>
"@
        $html | Out-File -FilePath $outFile -Encoding UTF8
    }
}

# Now fix links in all downloaded HTML files
$htmlFiles = Get-ChildItem -Path $pagesDir -Filter "*.html"

foreach ($file in $htmlFiles) {
    Write-Host "Processing: $($file.Name)"
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Replace href="..." links
    foreach ($entry in $urlMap.GetEnumerator()) {
        $oldUrl = $entry.Key
        $newUrl = $entry.Value
        
        # Handle href="path"
        $content = $content.Replace("href=`"$oldUrl`"", "href=`"$newUrl`"")
        
        # Handle href='/path' (single quotes)
        $content = $content.Replace("href='$oldUrl'", "href='$newUrl'")
        
        # Handle href="//twobrothersindiashop.com/path"
        $content = $content.Replace("href=`"//twobrothersindiashop.com$oldUrl`"", "href=`"$newUrl`"")
        
        # Handle href="https://twobrothersindiashop.com/path"
        $content = $content.Replace("href=`"https://twobrothersindiashop.com$oldUrl`"", "href=`"$newUrl`"")
    }
    
    # Replace links that point to twobrothersindiashop.com with # (external links we don't have)
    $content = $content -replace 'href="https://twobrothersindiashop\.com[^"]*"', 'href="#"'
    $content = $content -replace "href='https://twobrothersindiashop\.com[^']*'", "href='#'"
    $content = $content -replace 'href="//twobrothersindiashop\.com[^"]*"', 'href="#"'
    $content = $content -replace "href='//twobrothersindiashop\.com[^']*'", "href='#'"
    
    # Replace links to external domains
    $content = $content -replace 'href="https://[^"]*"', 'href="#"'
    
    # Remove form actions that would submit to external
    $content = $content -replace 'action="[^"]*"', 'action="#"'
    
    $content | Out-File -FilePath $file.FullName -Encoding UTF8
}

Write-Host "`nDone! All links have been updated."
Write-Host "Total files processed: $($htmlFiles.Count)"
