"""
Seed script: Populates initial Services, Portfolio Categories and
concept Projects for Lunex Presents.

Run: python manage.py shell < seed_data.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lunex_presents.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from services.models import Service
from portfolio.models import Category, Project, ProjectImage

print("Seeding Services...")


services_data = [
    {
        'title': 'Website Design & Development',
        'slug': 'website-design-development',
        'short_description': 'Custom-built websites that look stunning, load fast, and convert visitors into customers.',
        'full_description': (
            "Your website is your most important digital asset — and we build it to perform. "
            "We design and develop custom websites that are visually stunning, fast-loading, "
            "mobile-first, and optimized for search engines.\n\n"
            "Whether it's a single landing page or a full multi-page business site, every line "
            "of code and every design decision is made with your audience in mind.\n\n"
            "Deliverables include: responsive custom design, cross-browser testing, SEO-optimized "
            "structure, performance optimization, and content management setup."
        ),
        'icon_class': 'bi bi-code-slash',
        'display_order': 1,
    },
    {
        'title': 'Logo & Brand Identity',
        'slug': 'logo-brand-identity',
        'short_description': 'Distinctive logos and complete brand systems that tell your story and build recognition.',
        'full_description': (
            "Your logo is the first thing people see — and the last thing they forget. "
            "We create distinctive logos and comprehensive brand identity systems that capture "
            "the essence of your business and make it instantly recognizable.\n\n"
            "From initial concept to final brand guidelines, we give you everything you need "
            "to present your brand consistently and confidently across every platform.\n\n"
            "Deliverables include: custom logo design, colour palette, typography system, "
            "usage guidelines, and files in all formats (SVG, PNG, PDF)."
        ),
        'icon_class': 'bi bi-pen',
        'display_order': 2,
    },
    {
        'title': 'Posters & Social Media Creatives',
        'slug': 'posters-social-media',
        'short_description': 'Eye-catching social media graphics and posters that stop the scroll and drive engagement.',
        'full_description': (
            "In a feed full of noise, you need content that stops the scroll. We design "
            "eye-catching posters, social media graphics, and promotional creatives that get "
            "noticed, drive engagement, and stay perfectly on-brand.\n\n"
            "From one-off event posters to full social media content kits — we design assets "
            "that work beautifully on every platform and every screen size.\n\n"
            "Deliverables include: Instagram/Facebook/LinkedIn graphics, event posters, "
            "story templates, reel covers, and social media content kits."
        ),
        'icon_class': 'bi bi-images',
        'display_order': 3,
    },
]

for s in services_data:
    obj, created = Service.objects.update_or_create(slug=s['slug'], defaults=s)
    print(f"  {'Created' if created else 'Updated'} service: {obj.title}")

print("\nSeeding Portfolio Categories...")

categories_data = [
    {'name': 'Web Design',     'slug': 'web-design'},
    {'name': 'Brand Identity', 'slug': 'brand-identity'},
    {'name': 'Social Media',   'slug': 'social-media'},
]

categories = {}
for c in categories_data:
    obj, created = Category.objects.update_or_create(slug=c['slug'], defaults=c)
    categories[c['slug']] = obj
    print(f"  {'Created' if created else 'Updated'} category: {obj.name}")

print("\nSeeding Concept Portfolio Projects...")

projects_data = [
    {
        'title': 'Bloom Bakery — Brand & Web',
        'slug': 'bloom-bakery',
        'category': categories['web-design'],
        'short_description': 'A warm, modern website and brand identity for a local artisan bakery.',
        'description': (
            "Bloom Bakery needed a digital presence as warm and inviting as their baked goods. "
            "This concept project explores a complete brand and web solution — combining soft, "
            "earthy tones with clean typography to create a premium yet approachable identity.\n\n"
            "The website features an online menu, story page, and booking enquiry form, "
            "all designed mobile-first for a smooth experience across devices."
        ),
        'deliverables': 'Logo Design, Colour Palette, Typography System, Website Design, Mobile Responsive Layout',
        'is_concept': True,
        'is_featured': True,
        'display_order': 1,
    },
    {
        'title': 'NovaTech Solutions — Corporate Identity',
        'slug': 'novatech-solutions',
        'category': categories['brand-identity'],
        'short_description': 'A bold, minimal brand identity for a technology consulting startup.',
        'description': (
            "NovaTech Solutions required an identity that communicated authority and innovation. "
            "This concept identity uses a strong geometric logomark, a monochromatic palette, "
            "and sharp typography to position the brand as a serious player in the B2B tech space.\n\n"
            "The full identity system covers business stationery, email signatures, "
            "LinkedIn banners, and brand usage guidelines."
        ),
        'deliverables': 'Logo Design, Brand Guidelines, Business Card, Letterhead, LinkedIn Banner',
        'is_concept': True,
        'is_featured': True,
        'display_order': 2,
    },
    {
        'title': 'Velocity Gym — Social Media Kit',
        'slug': 'velocity-gym',
        'category': categories['social-media'],
        'short_description': 'High-energy social media templates and promotional graphics for a fitness brand.',
        'description': (
            "Velocity Gym needed content that matched the energy of their brand. "
            "This concept social media kit delivers bold, high-contrast post templates, "
            "story layouts, and promotional graphics built for Instagram and Facebook.\n\n"
            "The kit includes 20+ customizable templates in Figma, designed to maintain "
            "brand consistency while giving the team creative flexibility."
        ),
        'deliverables': 'Post Templates (x12), Story Templates (x8), Promo Graphics, Figma Source Files',
        'is_concept': True,
        'is_featured': True,
        'display_order': 3,
    },
    {
        'title': 'Grind Coffee Co. — Brand Identity',
        'slug': 'grind-coffee-co',
        'category': categories['brand-identity'],
        'short_description': 'A craft-forward brand identity for an independent specialty coffee shop.',
        'description': (
            "Grind Coffee Co. is a concept identity project for an independent specialty coffee brand. "
            "The visual system draws inspiration from craft culture, using rich espresso tones, "
            "textured typography, and a hand-drawn logomark to create authentic brand character.\n\n"
            "The identity is designed to work beautifully on packaging, signage, and digital platforms."
        ),
        'deliverables': 'Logo Design, Brand Identity System, Packaging Mockup, Social Profile Assets',
        'is_concept': True,
        'is_featured': False,
        'display_order': 4,
    },
    {
        'title': 'Apex Real Estate — Landing Page',
        'slug': 'apex-real-estate',
        'category': categories['web-design'],
        'short_description': 'A premium property listing landing page with enquiry conversion focus.',
        'description': (
            "Apex Real Estate needed a high-converting landing page for their luxury property listings. "
            "This concept design prioritizes visual impact and clear calls to action — "
            "featuring a full-screen hero, property highlights, and an integrated enquiry form.\n\n"
            "The design is intentionally minimal and refined, letting the properties speak for themselves."
        ),
        'deliverables': 'Landing Page Design, Mobile Responsive Layout, Enquiry Form Integration',
        'is_concept': True,
        'is_featured': False,
        'display_order': 5,
    },
]

gallery_images_map = {
    'novatech-solutions': [
        ('portfolio/gallery/novatech-solutions-1.jpg', 'Corporate Brand Identity & Executive Stationery Suite', 1),
        ('portfolio/gallery/novatech-solutions-2.jpg', 'Enterprise Cloud Platform & Live Telemetry Dashboard', 2),
        ('portfolio/gallery/novatech-solutions-3.jpg', 'Executive Mobile App & Infrastructure Alert Cockpit', 3),
        ('portfolio/gallery/novatech-solutions-4.jpg', 'Design System, Brand Guidelines & Typography Tokens', 4),
    ],
    'bloom-bakery': [
        ('portfolio/gallery/bloom-bakery-1.jpg', 'Artisanal Bakery Web Storefront & Daily Ovens Hero', 1),
        ('portfolio/gallery/bloom-bakery-2.jpg', 'Daily Fresh Sourdough & Pastry Menu Catalog', 2),
        ('portfolio/gallery/bloom-bakery-3.jpg', 'Eco-Friendly Kraft Bread Bag & Cafe Collateral', 3),
        ('portfolio/gallery/bloom-bakery-4.jpg', 'Mobile Ordering, Table Reservation & Rapid Checkout', 4),
    ],
    'velocity-gym': [
        ('portfolio/gallery/velocity-gym-1.jpg', 'High-Performance Fitness Web Portal & Membership Hero', 1),
        ('portfolio/gallery/velocity-gym-2.jpg', '20+ Social Media Carousel & Story Kit in Figma', 2),
        ('portfolio/gallery/velocity-gym-3.jpg', 'Interactive Weekly Class Timetable & Session Booking', 3),
        ('portfolio/gallery/velocity-gym-4.jpg', 'Companion Workout Tracker & Member QR Entry App', 4),
    ],
    'grind-coffee-co': [
        ('portfolio/gallery/grind-coffee-co-1.jpg', 'Specialty Coffee Roasters Story & Single-Origin Hero', 1),
        ('portfolio/gallery/grind-coffee-co-2.jpg', 'Matte Charcoal & Copper Foil Bag Packaging Suite', 2),
        ('portfolio/gallery/grind-coffee-co-3.jpg', 'E-Commerce Fresh Bean Roaster Subscription System', 3),
        ('portfolio/gallery/grind-coffee-co-4.jpg', 'Hand-Drawn Brand Emblem & Cafe Menu Board Signage', 4),
    ],
    'apex-real-estate': [
        ('portfolio/gallery/apex-real-estate-1.jpg', 'Full-Screen Luxury Penthouse Architectural Showcase', 1),
        ('portfolio/gallery/apex-real-estate-2.jpg', 'Level 42 Architectural Blueprint & Residence Specs', 2),
        ('portfolio/gallery/apex-real-estate-3.jpg', 'Mobile Luxury Property Portfolio & VIP Tour Booking', 3),
        ('portfolio/gallery/apex-real-estate-4.jpg', 'Bespoke Property Lookbook & Foil Stationery Monogram', 4),
    ],
}

for p in projects_data:
    p['thumbnail'] = f"portfolio/{p['slug']}-thumb.jpg"
    obj, created = Project.objects.update_or_create(slug=p['slug'], defaults=p)
    print(f"  {'Created' if created else 'Updated'} project: {obj.title}")
    
    # Seed 4 gallery images
    if p['slug'] in gallery_images_map:
        ProjectImage.objects.filter(project=obj).delete()
        for img_path, caption, order in gallery_images_map[p['slug']]:
            ProjectImage.objects.create(
                project=obj,
                image=img_path,
                caption=caption,
                display_order=order,
            )
        print(f"    Added 4 gallery images for {obj.title}")

print("\nSeed complete. Database populated with dynamic projects and gallery images.")

