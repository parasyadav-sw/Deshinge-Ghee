#!/usr/bin/env python3
"""Generate all 6 Ghee product pages."""

import os
import json

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")

PRODUCTS = [
    {
        "id": "product_amorearth-desi-cow-a2-ghee",
        "title": "Desi Gir Cow Cultured Ghee",
        "usp_line": "Bilona-made | Certified Glyphosate-Free",
        "rating": 4.90,
        "review_count": 2364,
        "meta_title": "Buy A2 Cow Ghee from Two Brothers India | Organic A2 Ghee",
        "meta_description": "Buy A2 Cow Ghee from Two Brothers India. Made from Gir Cow Milk, Raw, Desi and Certified Organic Cow Milk Ghee with Free Delivery Across India. Shop Cow Ghee Order Now",
        "og_image": "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-a2-gir-cow-cultured-ghee.jpg?v=1780393282&width=1024",
        "images": [
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-a2-gir-cow-cultured-ghee.jpg?v=1780393282",
            "https://twobrothersindiashop.com/cdn/shop/files/Shop_Pure_A2_Cow_Ghee.jpg?v=1767778411",
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-a2-gir-cow-cultured-ghee.jpg?v=1780393282&width=800",
            "https://twobrothersindiashop.com/cdn/shop/files/Shop_Pure_A2_Cow_Ghee.jpg?v=1767778411&width=800",
        ],
        "short_description": "Looking for that comforting taste of tradition? Every drop of our Desi Gir Cow Cultured Ghee is just that! Crafted from the milk of free-grazed, pasture-raised Gir cows, this ghee is authentic &amp; wholesome.",
        "description_html": """<p>Looking for that comforting taste of tradition? Every drop of our Desi Gir Cow Cultured Ghee is just that!</p>
<p>Crafted from the milk of free-grazed, pasture-raised Gir cows, this ghee is authentic &amp; wholesome.</p>
<p>Our process starts with choosing the right cattle feed that's not sprayed with dangerous weedicides containing glyphosate. Then, we take the fresh milk, carefully turn it into yogurt using a natural starter culture and set it overnight. In the stillness of the early morning, the yogurt is then churned using the ancient Bilona method - clockwise and anticlockwise to separate the raw white butter. This butter is then gently simmered to create a rich, golden ghee filled with natural goodness.</p>
<p>Made daily in small batches and certified glyphosate free by The detox project, our Desi Gir Cow Cultured Ghee contains no additives, preservatives, chemicals or artificial ingredients. So, whether for cooking, baking, or enjoying its health benefits, this ghee is the perfect way to bring a taste of home to your table.</p>""",
        "ingredients_html": """<p>100% Pure A2 Gir Cow Cultured Ghee</p>
<ul><li>Made from grass-fed, free-grazing Gir cow milk</li>
<li>Bilona churned (traditional method)</li>
<li>No additives, preservatives, or chemicals</li>
<li>Certified Glyphosate-Free</li></ul>""",
        "usage_html": """<ul><li>Use for cooking, sautéing, and deep frying</li>
<li>Add to hot rice, dal, or rotis</li>
<li>Use in baking for rich flavor</li>
<li>Take a spoonful daily for wellness benefits</li>
<li>Use in Ayurvedic preparations</li></ul>""",
        "benefits_html": """<ul><li>Rich in healthy fats and fat-soluble vitamins (A, D, E, K)</li>
<li>Contains CLA (Conjugated Linoleic Acid) for heart health</li>
<li>Supports digestion and gut health</li>
<li>Boosts immunity naturally</li>
<li>Helps in nutrient absorption</li>
<li>Supports brain health and cognitive function</li></ul>""",
        "storage_html": """<p>Store in a cool, dry place away from direct sunlight.</p>
<p>Best before 1 year from the date of packaging.</p>
<p>No refrigeration required. Use a clean, dry spoon to scoop ghee.</p>""",
        "faqs": [
            {"q": "What makes this ghee different from regular ghee?", "a": "Our ghee is made using the traditional Bilona method from A2 Gir cow milk. It is certified glyphosate-free and contains no additives or preservatives. The cows are free-grazed and pasture-raised."},
            {"q": "Is this ghee suitable for lactose intolerant people?", "a": "Ghee is generally well tolerated by lactose intolerant individuals as the lactose is removed during the clarification process."},
            {"q": "How should I store this ghee?", "a": "Store in a cool, dry place away from direct sunlight. No refrigeration needed. Use a clean, dry spoon."},
            {"q": "What is the shelf life?", "a": "Best before 1 year from the date of packaging."},
            {"q": "Can I use this for cooking at high temperatures?", "a": "Yes, ghee has a high smoke point (around 250°C/482°F), making it ideal for high-temperature cooking, sautéing, and deep frying."},
        ],
        "reviews": [
            {"name": "Priya S.", "rating": 5, "date": "15 Jan 2026", "title": "Authentic taste", "text": "This ghee takes me back to my grandmother's kitchen. The aroma and taste are exactly like the traditional homemade ghee. Absolutely love it!"},
            {"name": "Rahul M.", "rating": 5, "date": "28 Dec 2025", "title": "Best quality ghee", "text": "I've been using this ghee for over a year now. The quality is consistently excellent. The Bilona method really makes a difference in taste."},
            {"name": "Anita K.", "rating": 4, "date": "10 Dec 2025", "title": "Great product, slightly pricey", "text": "The ghee is fantastic quality and tastes pure. Only reason for 4 stars is the price point, but I understand the quality justifies it."},
        ],
        "variants": [
            {"name": "1000 ml", "price": 3370, "unit_ml": 1000, "available": True},
            {"name": "500 ml", "price": 935, "unit_ml": 500, "available": True},
            {"name": "5 L", "price": 15935, "unit_ml": 5000, "available": True},
            {"name": "250 ml", "price": 935, "unit_ml": 250, "available": True},
        ],
    },
    {
        "id": "product_full-moon-ghee",
        "title": "Full Moon Cultured Ghee, Desi Gir Cow",
        "usp_line": "Once a month | 12 times a year",
        "rating": 4.92,
        "review_count": 413,
        "meta_title": "Buy Full Moon Cultured Ghee, Desi Gir Cow | Two Brothers India",
        "meta_description": "Shop Full Moon Ghee made from A2 Gir cow milk using the traditional Bilona method. Pure cultured ghee with rich aroma, healthy fats & authentic taste.",
        "og_image": "https://twobrothersindiashop.com/cdn/shop/files/Purchase_Full_Moon_Cultured_Ghee.jpg?v=1754562885&width=1024",
        "images": [
            "https://twobrothersindiashop.com/cdn/shop/files/Purchase_Full_Moon_Cultured_Ghee.jpg?v=1754562885",
            "https://twobrothersindiashop.com/cdn/shop/files/Purchase_Full_Moon_Cultured_Ghee.jpg?v=1754562885&width=800",
        ],
        "short_description": "Our Full Moon Cultured Ghee is prepared using milk from free-grazing Gir cows, known for their rich, high-quality milk. Made in limited quantities - just 12 small batches a year.",
        "description_html": """<p>Our Full Moon Cultured Ghee is prepared using milk from free-grazing Gir cows, known for their rich, high-quality milk. This ghee is made from cultured butter, using a slow-churning process traditionally practiced during the waxing phase of the full moon each month.</p>
<p>While this timing has historical and cultural significance in traditional Indian practices, it does not alter the nutritional content of the ghee.</p>
<p>Prepared in limited quantities - just 12 small batches a year - this ghee is unrefined, free from additives, and contains no preservatives. Its production method follows Ayurvedic traditions, and it is commonly used by Ayurvedic practitioners in various formulations.</p>""",
        "ingredients_html": """<p>100% Pure A2 Gir Cow Cultured Ghee</p>
<ul><li>Made from grass-fed, free-grazing Gir cow milk</li>
<li>Prepared during full moon (once a month)</li>
<li>Traditional slow-churning Bilona method</li>
<li>No additives, preservatives, or chemicals</li></ul>""",
        "usage_html": """<ul><li>Use for cooking, sautéing, and deep frying</li>
<li>Add to hot rice, dal, or rotis</li>
<li>Use in Ayurvedic preparations</li>
<li>Take a spoonful daily for wellness benefits</li></ul>""",
        "benefits_html": """<ul><li>Rich in healthy fats and fat-soluble vitamins</li>
<li>Follows Ayurvedic traditions for enhanced potency</li>
<li>Supports digestion and gut health</li>
<li>Boosts immunity naturally</li>
<li>Limited batch production ensures quality</li></ul>""",
        "storage_html": """<p>Store in a cool, dry place away from direct sunlight.</p>
<p>Best before 12 months from the date of packaging.</p>""",
        "faqs": [
            {"q": "What is Full Moon Ghee?", "a": "Full Moon Ghee is prepared during the waxing phase of the full moon each month, following traditional Ayurvedic practices. It is made just 12 times a year in limited batches."},
            {"q": "Does the full moon timing affect the ghee?", "a": "While the timing has historical and cultural significance in traditional Indian practices, it does not alter the nutritional content of the ghee."},
            {"q": "How is this different from regular ghee?", "a": "This ghee is prepared in limited quantities during specific lunar phases, following Ayurvedic traditions. It is commonly used by Ayurvedic practitioners."},
        ],
        "reviews": [
            {"name": "Deepak R.", "rating": 5, "date": "5 Feb 2026", "title": "Premium quality", "text": "The quality of this ghee is exceptional. You can taste the difference in every spoonful. Highly recommended for those who appreciate authentic products."},
            {"name": "Meera J.", "rating": 5, "date": "20 Jan 2026", "title": "Ayurvedic perfection", "text": "Perfect for my Ayurvedic routines. The aroma is divine and the texture is smooth."},
        ],
        "variants": [
            {"name": "500 ml", "price": 2335, "unit_ml": 500, "available": True},
        ],
    },
    {
        "id": "product_tulsi-ghee-herbal-ghee-daily-care-wellness",
        "title": "Tulsi Ghee",
        "usp_line": "Tulsi infused | Gir Cow Ghee",
        "rating": 4.93,
        "review_count": 70,
        "meta_title": "Buy A2 Tulsi Bilona Cow Ghee Online | Herbal Wellness Ghee",
        "meta_description": "Shop Tulsi-infused A2 Cow Bilona Ghee made from cultured Gir cow milk. Crafted using the traditional Bilona process for daily wellness, immunity and nourishment.",
        "og_image": "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-tulsi-ghee-jar-on-a-bed-of-green-leaves..jpg?v=1780395520&width=1024",
        "images": [
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-tulsi-ghee-jar-on-a-bed-of-green-leaves..jpg?v=1780395520",
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-tulsi-ghee-jar-on-a-bed-of-green-leaves..jpg?v=1780395520&width=800",
        ],
        "short_description": "Infused with the goodness of Tulsi and the richness of Cultured Desi Gir Cow ghee, our Tulsi Ghee brings the healing power of Ayurveda to your kitchen.",
        "description_html": """<p>Infused with the goodness of Tulsi and the richness of Cultured Desi Gir Cow ghee, our Tulsi Ghee brings the healing power of Ayurveda to your kitchen. This unique blend enhances Tulsi's natural benefits, supporting immunity, digestion, and overall wellness.</p>
<p>Tulsi, as we know of it, reduces stress and provides skin-glowing properties, merges perfectly with the nourishment of our cow ghee, carrying its vitality deep into the body.</p>
<p>Thus, a spoonful of this ghee offers a simple, delicious way to feel connected to nature's goodness, even if you are craving for that homecoming vibes.</p>""",
        "ingredients_html": """<ul><li>A2 Gir Cow Cultured Ghee</li>
<li>Organic Tulsi (Holy Basil) extract</li>
<li>No additives, preservatives, or chemicals</li></ul>""",
        "usage_html": """<ul><li>Take a spoonful daily for immunity support</li>
<li>Use in cooking for enhanced flavor</li>
<li>Add to warm milk before bedtime</li>
<li>Use in Ayurvedic preparations</li></ul>""",
        "benefits_html": """<ul><li>Supports immune system</li>
<li>Promotes respiratory wellness</li>
<li>Reduces stress and supports calmness</li>
<li>Enhances digestion</li>
<li>Rich in antioxidants from Tulsi</li>
<li>Supports overall wellness</li></ul>""",
        "storage_html": """<p>Store in a cool, dry place away from direct sunlight.</p>
<p>Best before 12 months from the date of packaging.</p>""",
        "faqs": [
            {"q": "What is Tulsi Ghee?", "a": "Tulsi Ghee is A2 Gir Cow cultured ghee infused with organic Tulsi (Holy Basil). It combines the benefits of traditional ghee with the healing properties of Tulsi."},
            {"q": "Can I use this for cooking?", "a": "Yes, Tulsi Ghee can be used for cooking, added to warm milk, or taken directly as a daily supplement."},
            {"q": "Is this suitable for daily use?", "a": "Yes, a spoonful of Tulsi Ghee daily can support immunity and overall wellness."},
        ],
        "reviews": [
            {"name": "Kavita P.", "rating": 5, "date": "12 Feb 2026", "title": "Love the Tulsi flavor", "text": "The combination of Tulsi and ghee is perfect. I take it daily and have noticed improved immunity. Great product!"},
            {"name": "Sanjay T.", "rating": 5, "date": "28 Jan 2026", "title": "Excellent herbal ghee", "text": "The Tulsi infusion is subtle but effective. Perfect for my morning routine. Highly recommend."},
        ],
        "variants": [
            {"name": "250 ml", "price": 2335, "unit_ml": 250, "available": True},
        ],
    },
    {
        "id": "product_brahmi-ghee-a2-cultured-250-gms",
        "title": "Brahmi Ghee",
        "usp_line": "Brahmi infused | Desi Gir Cow Ghee",
        "rating": 4.89,
        "review_count": 62,
        "meta_title": "Buy A2 Brahmi Bilona Cow Ghee Online | Herbal Wellness Ghee",
        "meta_description": "Made with Brahmi and cultured Gir cow milk using the Bilona method. A nourishing herbal ghee with healthy fats for daily wellness and mindful living.",
        "og_image": "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-brahmi-ghee-jar-on-a-bed-of-herbs.jpg?v=1780397089&width=1024",
        "images": [
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-brahmi-ghee-jar-on-a-bed-of-herbs.jpg?v=1780397089",
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-brahmi-ghee-jar-on-a-bed-of-herbs.jpg?v=1780397089&width=800",
        ],
        "short_description": "A spoonful of pure, golden goodness, where the nurturing essence of Brahmi meets the wholesome richness of Desi Gir Cow Cultured Ghee.",
        "description_html": """<p>A spoonful of pure, golden goodness, where the nurturing essence of Brahmi meets the wholesome richness of Desi Gir Cow Cultured Ghee. Our Brahmi Ghee is just that and much more!</p>
<p>Crafted from the freshest milk of grass-fed Gir cows, this ghee is infused with sustainably grown Brahmi. Known for its ability to enhance cognitive function, promote overall wellness, and anxiety healing properties, every batch is handmade with traditional methods, preserving the natural goodness that's both soothing and revitalizing.</p>
<p>100% natural, free from preservatives, additives, and artificial ingredients, our Brahmi Ghee is here to bring warmth and healing into your daily routine.</p>""",
        "ingredients_html": """<ul><li>A2 Gir Cow Cultured Ghee</li>
<li>Organic Brahmi (Bacopa monnieri) extract</li>
<li>No additives, preservatives, or chemicals</li></ul>""",
        "usage_html": """<ul><li>Take a spoonful daily for cognitive support</li>
<li>Use in cooking for enhanced flavor</li>
<li>Add to warm milk before bedtime</li>
<li>Use in Ayurvedic preparations</li></ul>""",
        "benefits_html": """<ul><li>Enhances cognitive function and memory</li>
<li>Reduces stress and anxiety</li>
<li>Supports brain health</li>
<li>Promotes overall wellness</li>
<li>Rich in healthy fats from A2 ghee</li></ul>""",
        "storage_html": """<p>Store in a cool, dry place away from direct sunlight.</p>
<p>Best before 12 months from the date of packaging.</p>""",
        "faqs": [
            {"q": "What is Brahmi Ghee?", "a": "Brahmi Ghee is A2 Gir Cow cultured ghee infused with organic Brahmi (Bacopa monnieri). It combines the benefits of traditional ghee with the cognitive-enhancing properties of Brahmi."},
            {"q": "Is this suitable for students?", "a": "Yes, Brahmi is known for enhancing cognitive function and memory, making it beneficial for students and anyone seeking mental clarity."},
            {"q": "Can I use this for cooking?", "a": "Yes, Brahmi Ghee can be used for cooking or taken directly as a daily supplement."},
        ],
        "reviews": [
            {"name": "Vikram S.", "rating": 5, "date": "5 Feb 2026", "title": "Great for focus", "text": "I've been taking this for a month and notice improved concentration during work. The taste is pleasant and the quality is excellent."},
            {"name": "Neha G.", "rating": 4, "date": "20 Jan 2026", "title": "Good quality product", "text": "The ghee is smooth and the Brahmi infusion is subtle. I use it daily in my morning routine."},
        ],
        "variants": [
            {"name": "250 ml", "price": 2335, "unit_ml": 250, "available": False},
        ],
    },
    {
        "id": "product_shatavari-ghee-a2-cultured-250-gms",
        "title": "Shatavari Ghee",
        "usp_line": "Shatavari infused | A2 Ghee",
        "rating": 4.91,
        "review_count": 58,
        "meta_title": "Buy A2 Shatavari Bilona Cow Ghee Online | Herbal Wellness Ghee",
        "meta_description": "Made with cultured Gir cow milk and Shatavari, this A2 Bilona Ghee supports women's wellness, vitality and nourishment while providing healthy fats and rich flavor.",
        "og_image": "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-shatavari-ghee-jar-on-shatavari-roots-backgroundq.jpg?v=1780396268&width=1024",
        "images": [
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-shatavari-ghee-jar-on-shatavari-roots-backgroundq.jpg?v=1780396268",
            "https://twobrothersindiashop.com/cdn/shop/files/two-brothers-organic-farms-shatavari-ghee-jar-on-shatavari-roots-backgroundq.jpg?v=1780396268&width=800",
        ],
        "short_description": "Indulge in the nourishing richness of our Shatavari Ghee, made from pure A2 Gir Cow Cultured Ghee and enhanced with sustainably grown Shatavari.",
        "description_html": """<p>Indulge in the nourishing richness of our Shatavari Ghee, made from pure A2 Gir Cow Cultured Ghee and enhanced with sustainably grown Shatavari. This ghee is a traditional Ayurvedic blend, designed to support your health and well-being by improving the bioavailability of Shatavari's powerful benefits.</p>
<p>Crafted with love using the Vedic Bilona method, this ghee is made from the fresh, grass-fed milk of free-grazing Gir cows, ensuring purity and quality in every jar. It's lactose-free, GMO-free, lab-verified, and made handmade in small batches, ensuring the highest standards of quality and authenticity.</p>
<p>Free from additives, preservatives, and hormones, it's 100% natural and full of goodness. So, whether added to your daily routine or used in cooking, TBOF Shatavari Ghee brings a taste of tradition, comfort, and vitality - just like home.</p>""",
        "ingredients_html": """<ul><li>A2 Gir Cow Cultured Ghee</li>
<li>Organic Shatavari (Asparagus racemosus) extract</li>
<li>No additives, preservatives, or chemicals</li></ul>""",
        "usage_html": """<ul><li>Take a spoonful daily for women's wellness</li>
<li>Use in cooking for enhanced flavor</li>
<li>Add to warm milk before bedtime</li>
<li>Use in Ayurvedic preparations</li></ul>""",
        "benefits_html": """<ul><li>Supports women's health and wellness</li>
<li>Promotes hormonal balance</li>
<li>Enhances vitality and energy</li>
<li>Supports reproductive health</li>
<li>Rich in healthy fats from A2 ghee</li></ul>""",
        "storage_html": """<p>Store in a cool, dry place away from direct sunlight.</p>
<p>Best before 12 months from the date of packaging.</p>""",
        "faqs": [
            {"q": "What is Shatavari Ghee?", "a": "Shatavari Ghee is A2 Gir Cow cultured ghee infused with organic Shatavari (Asparagus racemosus). It combines the benefits of traditional ghee with the women's wellness properties of Shatavari."},
            {"q": "Is this suitable for all ages?", "a": "While Shatavari is particularly beneficial for women's health, this ghee can be enjoyed by adults of all ages as a nutritious supplement."},
            {"q": "How should I consume this?", "a": "Take a spoonful daily, add to warm milk, or use in cooking. For best results, consume consistently."},
        ],
        "reviews": [
            {"name": "Ritu D.", "rating": 5, "date": "10 Feb 2026", "title": "Amazing for wellness", "text": "I've been using this for 3 months and love it. The Shatavari infusion makes it perfect for my daily wellness routine. Great quality!"},
            {"name": "Pooja M.", "rating": 5, "date": "25 Jan 2026", "title": "Excellent herbal ghee", "text": "The taste is smooth and the quality is excellent. I highly recommend this for anyone looking for a herbal ghee option."},
        ],
        "variants": [
            {"name": "250 ml", "price": 2335, "unit_ml": 250, "available": True},
        ],
    },
    {
        "id": "product_buffalo-ghee-a2-cultured",
        "title": "Buffalo Ghee",
        "usp_line": "Bilona-made | Firewood process",
        "rating": 4.85,
        "review_count": 113,
        "meta_title": "Buy A2 Buffalo Bilona Ghee Online | Rich, Creamy & Pure Ghee",
        "meta_description": "Made from A2 cultured buffalo milk and prepared using the traditional Bilona method, this pure Buffalo Ghee offers rich flavor, creamy texture and healthy fats.",
        "og_image": "https://twobrothersindiashop.com/cdn/shop/files/Shop_A2_Cultured_Buffalo_Ghee.webp?v=1754995537&width=1024",
        "images": [
            "https://twobrothersindiashop.com/cdn/shop/files/Shop_A2_Cultured_Buffalo_Ghee.webp?v=1754995537",
            "https://twobrothersindiashop.com/cdn/shop/files/Buy_A2_Cultured_Buffalo_Ghee.webp?v=1754562738",
            "https://twobrothersindiashop.com/cdn/shop/files/Shop_A2_Cultured_Buffalo_Ghee.webp?v=1754995537&width=800",
        ],
        "short_description": "There's nothing quite like the warmth and richness of freshly made ghee from native buffaloes - straight from the heart of Maharashtra to your kitchen.",
        "description_html": """<p>There's nothing quite like the warmth and richness of freshly made ghee from native buffaloes - straight from the heart of Maharashtra to your kitchen.</p>
<p>Made with fresh, unpasteurized milk from native buffaloes in the fertile belt of Western Maharashtra, this ghee is crafted with love and tradition. Every batch begins with curd that's carefully churned just before dawn, forming creamy white butter (Makkhan) which is then slow-cooked over firewood.</p>
<p>This traditional process ensures that our ghee is pure, aromatic, and packed with natural goodness. Handmade in small batches daily, our A2 cultured buffalo ghee brings a rich, distinct flavor to your cooking, baking, or even as a nourishing spread. Free from additives, preservatives, and artificial flavors, it's a true taste of home that's as wholesome as it is delicious.</p>""",
        "ingredients_html": """<ul><li>100% Pure A2 Buffalo Cultured Ghee</li>
<li>Made from fresh, unpasteurized buffalo milk</li>
<li>Bilona churned and firewood slow-cooked</li>
<li>No additives, preservatives, or artificial flavors</li></ul>""",
        "usage_html": """<ul><li>Use for cooking, sautéing, and deep frying</li>
<li>Spread on rotis or bread</li>
<li>Add to hot rice or dal</li>
<li>Use in baking for rich flavor</li></ul>""",
        "benefits_html": """<ul><li>Rich, creamy texture with distinct flavor</li>
<li>Higher fat content than cow ghee</li>
<li>Rich in fat-soluble vitamins (A, D, E, K)</li>
<li>Supports digestion and gut health</li>
<li>Firewood process adds traditional smoky flavor</li></ul>""",
        "storage_html": """<p>Store in a cool, dry place away from direct sunlight.</p>
<p>Best before 12 months from manufacture.</p>
<p>No refrigeration required.</p>""",
        "faqs": [
            {"q": "How is Buffalo Ghee different from Cow Ghee?", "a": "Buffalo Ghee has a higher fat content, creamier texture, and richer flavor compared to cow ghee. It is also white in color due to the nature of buffalo milk."},
            {"q": "What does 'firewood process' mean?", "a": "Our buffalo ghee is slow-cooked over firewood, which is a traditional method that imparts a unique, smoky flavor and ensures thorough cooking."},
            {"q": "Can I use this for deep frying?", "a": "Yes, Buffalo Ghee has a high smoke point and is excellent for deep frying, sautéing, and all types of cooking."},
        ],
        "reviews": [
            {"name": "Amit V.", "rating": 5, "date": "8 Feb 2026", "title": "Authentic buffalo ghee", "text": "This ghee reminds me of the one my mother used to make. The firewood process gives it a unique flavor. Absolutely love it!"},
            {"name": "Sunita R.", "rating": 4, "date": "22 Jan 2026", "title": "Rich and creamy", "text": "The texture is incredibly smooth and creamy. Perfect for cooking and spreading on rotis. Great quality product."},
        ],
        "variants": [
            {"name": "1000 ml", "price": 1950, "unit_ml": 1000, "available": False},
            {"name": "500 ml", "price": 995, "unit_ml": 500, "available": True},
        ],
    },
]


def render_stars(rating):
    full = int(rating)
    half = 1 if rating - full >= 0.25 else 0
    empty = 5 - full - half
    stars = ""
    for _ in range(full):
        stars += '<span class="star filled">&#9733;</span>'
    if half:
        stars += '<span class="star half">&#9733;</span>'
    for _ in range(empty):
        stars += '<span class="star empty">&#9733;</span>'
    return stars


def generate_page(product):
    variants_json = json.dumps(product["variants"])
    rating_distribution = ""
    total = product["review_count"]
    r5 = int(total * 0.85)
    r4 = int(total * 0.10)
    r3 = int(total * 0.03)
    r2 = int(total * 0.01)
    r1 = total - r5 - r4 - r3 - r2
    dist = [(5, r5), (4, r4), (3, r3), (2, r2), (1, r1)]
    for stars, count in dist:
        pct = round(count / total * 100) if total else 0
        rating_distribution += f'''<div class="rating-bar"><span class="bar-label">{stars} ★</span><div class="bar-track"><div class="bar-fill" style="width:{pct}%"></div></div><span class="bar-count">{count}</span></div>'''

    review_cards = ""
    for rev in product["reviews"]:
        review_cards += f'''<div class="review-card"><div class="review-header"><strong>{rev["name"]}</strong><span class="review-date">{rev["date"]}</span></div><div class="review-stars">{"★" * rev["rating"]}{"☆" * (5 - rev["rating"])}</div><div class="review-title">{rev["title"]}</div><p class="review-text">{rev["text"]}</p></div>'''

    faq_items = ""
    for i, faq in enumerate(product["faqs"]):
        faq_items += f'''<div class="faq-item"><button class="faq-question" onclick="toggleFaq({i})">{faq["q"]} <span class="faq-icon">+</span></button><div class="faq-answer" id="faq-{i}"><p>{faq["a"]}</p></div></div>'''

    variant_buttons = ""
    for i, v in enumerate(product["variants"]):
        unit_price = round(v["price"] / v["unit_ml"], 2) if v["unit_ml"] else 0
        oos_class = ' oos' if not v["available"] else ''
        disabled = ' disabled' if not v["available"] else ''
        oos_label = ' (Out of Stock)' if not v["available"] else ''
        variant_buttons += f'''<button class="variant-btn{oos_class}" data-index="{i}" onclick="selectVariant({i})"{disabled}><span class="variant-name">{v["name"]}</span><span class="variant-price">₹{v["price"]:,}{oos_label}</span><span class="variant-unit">₹{unit_price}/ml</span></button>'''

    related_products = [p for p in PRODUCTS if p["id"] != product["id"]][:4]
    related_html = ""
    for rp in related_products:
        related_html += f'''<div class="related-card"><a href="{rp['id']}.html"><img src="{rp['images'][0]}" alt="{rp['title']}" loading="lazy"><h4>{rp['title']}</h4><div class="related-rating">{"★" * int(rp["rating"])}{"☆" * (5 - int(rp["rating"]))} {rp["rating"]}</div><p class="related-price">From ₹{rp['variants'][0]['price']:,}</p></a></div>'''

    default_variant = product["variants"][0]

    structured_data = json.dumps({
        "@context": "https://schema.org",
        "@type": "Product",
        "name": product["title"],
        "description": product["short_description"],
        "image": product["images"],
        "brand": {"@type": "Brand", "name": "Two Brothers Organic Farms"},
        "sku": product["id"],
        "offers": {
            "@type": "AggregateOffer",
            "lowPrice": min(v["price"] for v in product["variants"]),
            "highPrice": max(v["price"] for v in product["variants"]),
            "priceCurrency": "INR",
            "availability": "https://schema.org/InStock" if any(v["available"] for v in product["variants"]) else "https://schema.org/OutOfStock"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": product["rating"],
            "reviewCount": product["review_count"]
        }
    })

    first_available_idx = 0
    for idx, v in enumerate(product["variants"]):
        if v["available"]:
            first_available_idx = idx
            break

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{product["meta_title"]}</title>
<meta name="description" content="{product["meta_description"]}">
<meta property="og:type" content="product">
<meta property="og:title" content="{product["title"]}">
<meta property="og:description" content="{product["meta_description"]}">
<meta property="og:image" content="{product["og_image"]}">
<link rel="canonical" href="https://twobrothersindiashop.com/products/{product["id"].replace("product_", "")}">
<link rel="stylesheet" href="../assets/product-page.css">
<script type="application/ld+json">{structured_data}</script>
</head>
<body>

<nav class="breadcrumbs">
<a href="../index.html">Home</a> &gt; <a href="../index.html">Ghee</a> &gt; <span>{product["title"]}</span>
</nav>

<main class="product-page">

<section class="product-gallery">
<div class="main-image-wrapper">
<img id="mainImage" src="{product['images'][0]}" alt="{product['title']}" class="main-image" onclick="openLightbox()">
<span class="zoom-hint">Click to zoom</span>
</div>
<div class="thumbnail-strip">
{"".join(f'<img class="thumbnail{" active" if i == 0 else ""}" src="{img}" alt="Thumbnail {i+1}" onclick="switchImage({i})">' for i, img in enumerate(product["images"]))}
</div>
</section>

<section class="product-info">
<div class="product-badge">BEST SELLER</div>
<h1 class="product-title">{product["title"]}</h1>
<p class="product-usp">{product["usp_line"]}</p>

<div class="product-rating">
{render_stars(product["rating"])}
<span class="rating-value">{product["rating"]}</span>
<span class="rating-count">({product["review_count"]} reviews)</span>
</div>

<div class="product-price-section">
<div class="current-price">₹{default_variant["price"]:,}</div>
<div class="price-note">Inclusive of all taxes. Free shipping across India.</div>
<div class="membership-savings">Members save up to 10% on every order. <a href="#">Join now</a></div>
</div>

<p class="product-short-desc">{product["short_description"]}</p>

<div class="usp-icons">
<div class="usp-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg><span>Free Shipping</span></div>
<div class="usp-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg><span>Secure Payments</span></div>
<div class="usp-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg><span>Farmers Empowerment</span></div>
<div class="usp-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg><span>COD Available</span></div>
</div>

<div class="variant-selector">
<h3>Select Variant</h3>
<div class="variant-buttons">
{variant_buttons}
</div>
</div>

<div class="quantity-selector">
<h3>Quantity</h3>
<div class="quantity-controls">
<button class="qty-btn" onclick="changeQty(-1)">−</button>
<input type="number" id="quantity" value="1" min="1" max="10" readonly>
<button class="qty-btn" onclick="changeQty(1)">+</button>
</div>
</div>

<div class="action-buttons">
<button class="btn-add-to-cart" onclick="addToCart()">ADD TO CART</button>
<button class="btn-buy-now" onclick="buyNow()">BUY NOW</button>
</div>

<div class="pincode-checker">
<h3>Check Delivery</h3>
<div class="pincode-input-group">
<input type="text" id="pincodeInput" placeholder="Enter PIN code" maxlength="6">
<button onclick="checkPincode()">Check</button>
</div>
<div id="pincodeResult" class="pincode-result"></div>
</div>

</section>
</main>

<section class="product-details-section">
<h2>Product Details</h2>
<div class="accordion">
<div class="accordion-item">
<button class="accordion-header" onclick="toggleAccordion(0)">Description <span class="accordion-icon">+</span></button>
<div class="accordion-content" id="acc-0"><div class="accordion-inner">{product["description_html"]}</div></div>
</div>
<div class="accordion-item">
<button class="accordion-header" onclick="toggleAccordion(1)">Ingredients <span class="accordion-icon">+</span></button>
<div class="accordion-content" id="acc-1"><div class="accordion-inner">{product["ingredients_html"]}</div></div>
</div>
<div class="accordion-item">
<button class="accordion-header" onclick="toggleAccordion(2)">Usage <span class="accordion-icon">+</span></button>
<div class="accordion-content" id="acc-2"><div class="accordion-inner">{product["usage_html"]}</div></div>
</div>
<div class="accordion-item">
<button class="accordion-header" onclick="toggleAccordion(3)">Benefits <span class="accordion-icon">+</span></button>
<div class="accordion-content" id="acc-3"><div class="accordion-inner">{product["benefits_html"]}</div></div>
</div>
<div class="accordion-item">
<button class="accordion-header" onclick="toggleAccordion(4)">Storage <span class="accordion-icon">+</span></button>
<div class="accordion-content" id="acc-4"><div class="accordion-inner">{product["storage_html"]}</div></div>
</div>
</div>
</section>

<section class="faq-section">
<h2>Frequently Asked Questions</h2>
<div class="faq-list">
{faq_items}
</div>
</section>

<section class="reviews-section">
<h2>Customer Reviews</h2>
<div class="reviews-summary">
<div class="rating-big">{render_stars(product["rating"])}<span>{product["rating"]}</span></div>
<p>{product["review_count"]} reviews</p>
<div class="rating-distribution">
{rating_distribution}
</div>
</div>
<div class="reviews-list">
{review_cards}
</div>
</section>

<section class="related-products">
<h2>Related Ghee Products</h2>
<div class="related-grid">
{related_html}
</div>
</section>

<div class="sticky-add-to-cart" id="stickyBar">
<div class="sticky-info">
<span class="sticky-title">{product["title"]}</span>
<span class="sticky-price">₹{default_variant["price"]:,}</span>
</div>
<button class="sticky-btn" onclick="addToCart()">ADD TO CART</button>
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
<span class="lightbox-close">&times;</span>
<img id="lightboxImage" src="" alt="Product Image">
</div>

<div class="cart-toast" id="cartToast">Item added to cart!</div>

<script>
var productData = {json.dumps({"variants": product["variants"], "title": product["title"]})};
var selectedVariant = {first_available_idx};
var quantity = 1;

function switchImage(idx) {{
    var images = {json.dumps(product["images"])};
    document.getElementById("mainImage").src = images[idx];
    document.querySelectorAll(".thumbnail").forEach(function(t, i) {{
        t.classList.toggle("active", i === idx);
    }});
}}

function selectVariant(idx) {{
    selectedVariant = idx;
    var v = productData.variants[idx];
    document.querySelector(".current-price").textContent = "\\u20B9" + v.price.toLocaleString("en-IN");
    document.querySelectorAll(".variant-btn").forEach(function(b, i) {{
        b.classList.toggle("selected", i === idx);
    }});
    updateStickyPrice(v.price);
}}

function changeQty(delta) {{
    var input = document.getElementById("quantity");
    var val = parseInt(input.value) + delta;
    if (val < 1) val = 1;
    if (val > 10) val = 10;
    input.value = val;
    quantity = val;
}}

function addToCart() {{
    var v = productData.variants[selectedVariant];
    if (!v.available) {{
        showToast("This variant is currently out of stock");
        return;
    }}
    var cart = JSON.parse(localStorage.getItem("tbof_cart") || "[]");
    var existing = cart.find(function(item) {{ return item.name === productData.title && item.variant === v.name; }});
    if (existing) {{
        existing.qty += quantity;
    }} else {{
        cart.push({{ name: productData.title, variant: v.name, price: v.price, qty: quantity }});
    }}
    localStorage.setItem("tbof_cart", JSON.stringify(cart));
    showToast("Item added to cart! (" + cart.reduce(function(s, i) {{ return s + i.qty; }}, 0) + " items)");
}}

function buyNow() {{
    addToCart();
    window.location.href = "cart.html";
}}

function showToast(msg) {{
    var toast = document.getElementById("cartToast");
    toast.textContent = msg || "Item added to cart!";
    toast.classList.add("show");
    setTimeout(function() {{ toast.classList.remove("show"); }}, 3000);
}}

function checkPincode() {{
    var pin = document.getElementById("pincodeInput").value.trim();
    var result = document.getElementById("pincodeResult");
    if (pin.length !== 6 || !/^[0-9]{{6}}$/.test(pin)) {{
        result.innerHTML = '<span class="pincode-error">Please enter a valid 6-digit PIN code</span>';
        return;
    }}
    var validPincodes = ["110001","400001","560001","600001","700001","500001","380001","411001","302001","226001","440001","462001"];
    if (validPincodes.indexOf(pin) !== -1 || pin.startsWith("4") || pin.startsWith("1")) {{
        result.innerHTML = '<span class="pincode-success">✓ Delivery available! Estimated 3-5 business days.</span>';
    }} else {{
        result.innerHTML = '<span class="pincode-success">✓ Delivery available! Estimated 5-7 business days.</span>';
    }}
}}

function toggleAccordion(idx) {{
    var content = document.getElementById("acc-" + idx);
    var icon = content.previousElementSibling.querySelector(".accordion-icon");
    if (content.classList.contains("open")) {{
        content.classList.remove("open");
        icon.textContent = "+";
    }} else {{
        document.querySelectorAll(".accordion-content").forEach(function(c) {{ c.classList.remove("open"); }});
        document.querySelectorAll(".accordion-icon").forEach(function(i) {{ i.textContent = "+"; }});
        content.classList.add("open");
        icon.textContent = "−";
    }}
}}

function toggleFaq(idx) {{
    var answer = document.getElementById("faq-" + idx);
    var btn = answer.previousElementSibling;
    if (answer.classList.contains("open")) {{
        answer.classList.remove("open");
        btn.querySelector(".faq-icon").textContent = "+";
    }} else {{
        document.querySelectorAll(".faq-answer").forEach(function(a) {{ a.classList.remove("open"); }});
        document.querySelectorAll(".faq-question").forEach(function(q) {{ q.querySelector(".faq-icon").textContent = "+"; }});
        answer.classList.add("open");
        btn.querySelector(".faq-icon").textContent = "−";
    }}
}}

function openLightbox() {{
    var lb = document.getElementById("lightbox");
    document.getElementById("lightboxImage").src = document.getElementById("mainImage").src;
    lb.classList.add("open");
}}

function closeLightbox() {{
    document.getElementById("lightbox").classList.remove("open");
}}

function updateStickyPrice(price) {{
    document.querySelector(".sticky-price").textContent = "\\u20B9" + price.toLocaleString("en-IN");
}}

window.addEventListener("scroll", function() {{
    var bar = document.getElementById("stickyBar");
    if (window.innerWidth <= 768) {{
        var btn = document.querySelector(".action-buttons");
        if (btn && btn.getBoundingClientRect().bottom < 0) {{
            bar.classList.add("visible");
        }} else {{
            bar.classList.remove("visible");
        }}
    }}
}});

selectVariant({first_available_idx});
</script>

</body>
</html>'''

    return html


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for product in PRODUCTS:
        filename = f"{product['id']}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        html = generate_page(product)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {filename}")
    print(f"\nAll {len(PRODUCTS)} product pages generated in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
