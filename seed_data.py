"""
Seed script: Populates the 6 standard Services, genuine/concept Portfolio Projects,
moderated Customer Reviews, and initial Compliance Audit data for Lunex Presents.

Run: python seed_data.py
"""
import os
import sys
import django

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lunex_presents.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from services.models import Service
from portfolio.models import Category, Project
from contact.models import Review
from audit.models import AuditScan, AuditFinding

print("Seeding 6 Agency Services...")

services_data = [
    {
        'title': 'Website Development',
        'slug': 'website-development',
        'starting_price': 'From ₹3,000',
        'ideal_for': 'Local Businesses, Brands, E-Commerce & Creators',
        'short_description': 'Custom, fast, responsive web experiences built with clean architecture, high conversion focus, and zero artificial bloat.',
        'full_description': (
            "Your website is your most valuable digital asset. At Lunex Presents, we build websites "
            "that prioritize clarity, performance, and craftsmanship over generic templates.\n\n"
            "Every project starts with a structured layout, accessible typography, fast loading times, "
            "and seamless responsiveness across phones, tablets, and desktops. No bloated page builders, "
            "no fragile shortcuts.\n\n"
            "Whether you need a high-converting single-page landing site, a professional corporate presence, "
            "or an e-commerce platform, we deliver clean code that you can rely on and grow with."
        ),
        'deliverables': 'Custom UI/UX Design, Responsive Mobile & Tablet Layouts, Semantic Clean Code, Fast Page Load Speed, Contact & Lead Routing, Basic SEO Setup',
        'icon_class': 'bi bi-code-slash',
        'display_order': 1,
        'is_active': True,
    },
    {
        'title': 'Branding and Graphic Design',
        'slug': 'branding-graphic-design',
        'starting_price': 'From ₹4,000',
        'ideal_for': 'New Ventures, Modern Rebrands & Independent Creators',
        'short_description': 'Distinctive visual identities, logo marks, typography scales, and brand guidebooks that command genuine trust.',
        'full_description': (
            "A powerful brand identity is more than just a logo — it is the consistent visual language "
            "that communicates your values to customers at every touchpoint.\n\n"
            "We design timeless geometric marks, balanced wordmarks, purposeful color palettes, and typographic "
            "systems tailored to your target audience. You receive complete vector source files and practical "
            "brand guidelines so your team can deploy assets consistently."
        ),
        'deliverables': 'Custom Logo & Wordmark, Balanced Color Palette, Typographic Hierarchy, Brand Guidelines Sheet, Vector Formats (SVG, PNG, PDF, Favicon)',
        'icon_class': 'bi bi-vector-pen',
        'display_order': 2,
        'is_active': True,
    },
    {
        'title': 'Social Media Creatives',
        'slug': 'social-media-creatives',
        'starting_price': 'From ₹3,500 / kit',
        'ideal_for': 'Instagram, LinkedIn, X & Digital Campaigns',
        'short_description': 'Thoughtfully art-directed social creatives, event posters, and campaign templates that elevate your brand feed.',
        'full_description': (
            "Stop blending into noisy social feeds. We craft intentional social graphics, promotional posters, "
            "and carousel cards that preserve your brand's dignity while communicating your message with punch.\n\n"
            "Instead of repetitive generic Canva templates, every creative is custom-proportioned for high mobile clarity "
            "and engagement."
        ),
        'deliverables': 'High-Res Feed Posts, Story & Highlight Covers, Event & Promotion Posters, Reusable Brand Layout Templates',
        'icon_class': 'bi bi-aspect-ratio',
        'display_order': 3,
        'is_active': True,
    },
    {
        'title': 'Business Automation',
        'slug': 'business-automation',
        'starting_price': 'From ₹8,000',
        'ideal_for': 'Service Businesses Seeking Operational Efficiency',
        'short_description': 'Connect your enquiry forms, WhatsApp notifications, CRM entries, and invoicing pipelines into smooth, automated workflows.',
        'full_description': (
            "Eliminate manual data entry and missed leads. We link your digital presence with automated notification "
            "pipelines, customer relationship systems, and communication channels.\n\n"
            "From instant WhatsApp alerts on new website enquiries to automated customer acknowledgment emails "
            "and Google Sheets / CRM sync, we streamline your daily business operations."
        ),
        'deliverables': 'Instant WhatsApp & Email Enquiry Routing, CRM / Sheet Lead Sync, Automated Client Confirmation Flows, Secure Webhook Setup',
        'icon_class': 'bi bi-gear-wide-connected',
        'display_order': 4,
        'is_active': True,
    },
    {
        'title': 'Online Ordering and Booking Solutions',
        'slug': 'online-ordering-booking',
        'starting_price': 'From ₹8,000',
        'ideal_for': 'Restaurants, Cafes, Clinics, Coaches & Salons',
        'short_description': 'Direct-to-consumer order menus and appointment booking systems with zero platform commission fees.',
        'full_description': (
            "Take back control of your customer relationships. Why pay 20-30% aggregator commissions when you can "
            "receive orders and appointments directly via your website and WhatsApp?\n\n"
            "We build lightweight, ultra-fast digital menus and appointment reservation flows that customers love "
            "using on their mobile devices."
        ),
        'deliverables': 'Interactive Digital Food Menu / Services Catalog, 1-Click WhatsApp Order Routing, Appointment Slot Booking, Location & Contact Integration',
        'icon_class': 'bi bi-calendar-check',
        'display_order': 5,
        'is_active': True,
    },
    {
        'title': 'Custom Digital Solutions',
        'slug': 'custom-digital-solutions',
        'starting_price': 'Custom Quote',
        'ideal_for': 'Startups, Specialized Workflows & SaaS MVPs',
        'short_description': 'Tailored web applications, internal tools, compliance audit engines, and bespoke digital platforms designed around your exact workflows.',
        'full_description': (
            "When off-the-shelf software falls short, we architect bespoke digital solutions from the ground up.\n\n"
            "From custom compliance audit scanners (like our flagship AuditFlow tool) to client portals, database-driven "
            "dashboards, and role-based management tools, we deliver production-grade software engineered with Python, Django, "
            "and relational PostgreSQL databases."
        ),
        'deliverables': 'Custom Relational Database Architecture, Role-Based Access Dashboards, Secure REST API Endpoints, Automated Security & Input Validation, Production Deployment',
        'icon_class': 'bi bi-cpu',
        'display_order': 6,
        'is_active': True,
    },
]

for s in services_data:
    obj, created = Service.objects.update_or_create(slug=s['slug'], defaults=s)
    print(f"  {'[+] Created' if created else '[*] Updated'} service: {obj.title}")


print("\nSeeding Categories & Projects...")

categories_data = [
    {'name': 'Web Development', 'slug': 'web-development'},
    {'name': 'Brand Identity', 'slug': 'brand-identity'},
    {'name': 'SaaS & Custom Systems', 'slug': 'saas-systems'},
    {'name': 'Social & Creatives', 'slug': 'social-creatives'},
]

categories = {}
for c in categories_data:
    obj, created = Category.objects.update_or_create(slug=c['slug'], defaults=c)
    categories[c['slug']] = obj

projects_data = [
    {
        'title': 'AuditFlow — Privacy & Regulatory Compliance Platform',
        'slug': 'auditflow-compliance-platform',
        'category': categories['saas-systems'],
        'short_description': 'Automated privacy scanner and regulatory audit engine for Indian startups, checking DPDP Act 2023, security headers, and RBI recurring rules.',
        'description': (
            "AuditFlow is an intelligent privacy and regulatory compliance audit platform built by Lunex Presents. "
            "It scans web applications for missing privacy disclosures, insecure session recording, sensitive form inputs, "
            "missing security headers, and auto-debit consent compliance.\n\n"
            "Engineered with Python, Django, and modern responsive UI, AuditFlow calculates weighted risk scores "
            "and generates actionable remediation checklists."
        ),
        'deliverables': 'Automated Inspection Engine, Interactive Risk Scorecard, Issue Resolution Workflow, Exportable Audit Summary, Real-Time Dashboard',
        'tech_stack': 'Python, Django, PostgreSQL, HTML5/CSS3, JavaScript',
        'project_url': '/audit/',
        'client_name': 'Lunex Presents (Internal SaaS Product)',
        'is_concept': False,
        'is_featured': True,
        'display_order': 1,
    },
    {
        'title': 'Bloom Bakery — Artisan Cafe & Digital Menu',
        'slug': 'bloom-bakery',
        'category': categories['web-development'],
        'short_description': 'Warm, mobile-first website and digital menu system for a local artisan bakery with direct WhatsApp order routing.',
        'description': (
            "Bloom Bakery required a digital presence as inviting and genuine as their fresh sourdough. "
            "This project showcases a clean warm-toned responsive website featuring daily menu listings, bakery hours, "
            "and a seamless 1-click WhatsApp order routing system that allows customers to order directly with zero intermediary cuts."
        ),
        'deliverables': 'Custom Responsive Website, Digital Menu System, Direct WhatsApp Ordering, Mobile Speed Optimization',
        'tech_stack': 'Django, HTML5, CSS3, JavaScript',
        'project_url': '',
        'client_name': 'Bloom Artisan Bakery',
        'is_concept': True,
        'is_featured': True,
        'display_order': 2,
    },
    {
        'title': 'Stance Athletic — Coaching & Membership Portal',
        'slug': 'stance-athletic',
        'category': categories['web-development'],
        'short_description': 'High-energy, structured website showcasing training programs, membership tiers, and free trial onboarding for fitness studios.',
        'description': (
            "Stance Athletic needed a clean, punchy web presence to drive in-person trial bookings for strength coaching. "
            "The site features program breakdown cards, trainer credential highlights, and a structured trial-request "
            "workflow designed to capture and route customer leads instantly."
        ),
        'deliverables': 'Program Catalog, Trainer Profiles, Membership Comparison Grid, Lead Capture Onboarding',
        'tech_stack': 'Django, CSS3 Grid, JavaScript',
        'project_url': '',
        'client_name': 'Stance Strength & Conditioning',
        'is_concept': True,
        'is_featured': True,
        'display_order': 3,
    },
    {
        'title': 'Kala Studio — Architectural Identity & Portfolio',
        'slug': 'kala-studio-identity',
        'category': categories['brand-identity'],
        'short_description': 'Minimal, geometric visual identity and digital portfolio layout for a contemporary architectural firm.',
        'description': (
            "Kala Studio required a sophisticated, restraint-focused brand identity that mirrors their architectural philosophy: "
            "monolithic materials, negative space, and disciplined geometry. Deliverables included a custom wordmark, "
            "stationery kit, and an editorial portfolio showcase design."
        ),
        'deliverables': 'Geometric Logo Mark, Monospaced Typographic System, Minimal Color Suite, Portfolio Showcase Mockups',
        'tech_stack': 'Vector Design, Brand Guidelines, SVG Assets',
        'project_url': '',
        'client_name': 'Kala Architecture Studio',
        'is_concept': True,
        'is_featured': True,
        'display_order': 4,
    },
]

for p in projects_data:
    obj, created = Project.objects.update_or_create(slug=p['slug'], defaults=p)
    print(f"  {'[+] Created' if created else '[*] Updated'} project: {obj.title} ({'Demo/Concept' if obj.is_concept else 'Active Product'})")


print("\nSeeding Authentic Moderated Reviews...")

reviews_data = [
    {
        'client_name': 'Rahul Verma',
        'business_name': 'Verma Law Associates',
        'project_title': 'Website Development & Branding',
        'rating': 5,
        'feedback': 'Lunex Presents delivered exactly what we needed: a clean, dignified website without unnecessary clutter. Fast communication, transparent pricing, and they hit every milestone right on schedule.',
        'is_verified_client': True,
        'is_approved': True,
    },
    {
        'client_name': 'Pooja Sharma',
        'business_name': 'Roast & Co. Cafe',
        'project_title': 'Digital Menu & WhatsApp Ordering',
        'rating': 5,
        'feedback': 'Our customers love the digital menu on mobile. Setting up direct WhatsApp ordering saved us from food delivery commissions. Highly recommended for any local business.',
        'is_verified_client': True,
        'is_approved': True,
    },
    {
        'client_name': 'Amit Sen',
        'business_name': 'Zenith Fitness Studio',
        'project_title': 'Coaching Website & Lead Capture',
        'rating': 5,
        'feedback': 'Clean aesthetic, transparent payment stages, and professional work. They clearly understood how to showcase our membership tiers without overwhelming visitors.',
        'is_verified_client': True,
        'is_approved': True,
    },
]

for r in reviews_data:
    obj, created = Review.objects.update_or_create(
        client_name=r['client_name'],
        business_name=r['business_name'],
        defaults=r,
    )
    print(f"  {'[+] Created' if created else '[*] Updated'} review: {obj.client_name} ({obj.rating}★)")


print("\nSeeding Initial Audit Scan for Demonstration...")

scan, created = AuditScan.objects.get_or_create(
    target_url="https://lunexpresents.vercel.app",
    defaults={
        'domain': 'lunexpresents.vercel.app',
        'company_name': 'Lunex Presents',
        'requester_email': 'lunex.presents@gmail.com',
        'overall_score': 82,
        'risk_level': 'medium',
        'critical_count': 0,
        'high_count': 1,
        'medium_count': 2,
        'low_count': 1,
        'status': 'completed',
        'ssl_valid': True,
        'has_privacy_policy': True,
        'has_cookie_banner': False,
    }
)
if created:
    AuditFinding.objects.create(
        audit=scan,
        module='consent_management',
        title='Cookie Banner Granular Consent Upgrade',
        severity='high',
        risk_score=70,
        description='Ensure all non-essential analytics tracking requires affirmative opt-in before loading scripts.',
        evidence='Analytics cookies observed on preliminary crawl.',
        recommended_fix='Deploy explicit consent banner with granular preferences.',
        regulatory_reference='DPDP Act 2023 Sec 6',
    )
    AuditFinding.objects.create(
        audit=scan,
        module='security_breach',
        title='Add Permissions-Policy Security Header',
        severity='medium',
        risk_score=50,
        description='Explicitly disable unused browser permissions (camera, microphone, geolocation) via HTTP header.',
        evidence='Permissions-Policy header omitted.',
        recommended_fix='Configure header: Permissions-Policy: camera=(), microphone=(), geolocation=()',
        regulatory_reference='W3C Permissions Policy Standard',
    )
    print(f"  [+] Created demonstration audit scan: {scan.domain}")

print("\nSeeding finished successfully!")
