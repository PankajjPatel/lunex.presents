from django.shortcuts import render
from portfolio.models import Project
from services.models import Service
from contact.models import Review
from contact.forms import ContactForm, ReviewForm


def home(request):
    """
    Homepage view for Lunex Presents.
    Features:
    1. Hero: Ideas to Digital Experiences that Grow.
    2. Services overview (6 services).
    3. Featured portfolio projects (honestly labeled).
    4. How we work (01 Discuss, 02 Plan, 03 Build, 04 Launch).
    5. Pricing overview (transparent starting rates).
    6. Customer reviews (approved only).
    7. Free demo CTA.
    8. Payment terms (40% / 40% / 20%).
    9. Unified Contact & Quote form.
    """
    featured_projects = (
        Project.objects.filter(is_featured=True)
        .select_related('category')
        .prefetch_related('images')[:6]
    )
    services = Service.objects.filter(is_active=True)[:6]
    approved_reviews = Review.objects.filter(is_approved=True)[:6]
    contact_form = ContactForm()
    review_form = ReviewForm()

    pricing_tiers = [
        {
            'name': 'Basic Landing Page',
            'price': '₹3,000 – ₹5,000',
            'tag': 'Fast Turnaround',
            'desc': 'Clean, single-page website optimized for campaign conversions, portfolios, or event launches.',
            'deliverables': ['1 Custom High-Converting Page', 'Mobile & Tablet Responsive', 'Contact / Lead Capture Form', 'Basic SEO Setup', '3–5 Days Turnaround'],
        },
        {
            'name': 'Portfolio Website',
            'price': '₹4,000 – ₹8,000',
            'tag': 'For Creators & Freelancers',
            'desc': 'Distinctive showcase for designers, photographers, consultants, and individual professionals.',
            'deliverables': ['Up to 4 Custom Pages', 'Interactive Project Showcase', 'About & Experience Section', 'Contact Integration', 'Fast Loading & Optimized Assets'],
        },
        {
            'name': 'Business Website',
            'price': '₹7,000 – ₹15,000',
            'tag': 'Most Popular for Local Brands',
            'desc': 'Comprehensive digital home for service businesses, agencies, clinics, and professional firms.',
            'deliverables': ['Up to 7 Clean Pages', 'Service Showcase with Pricing', 'WhatsApp & Direct Inquiry Links', 'Custom Design Language', 'Admin Dashboard for Updates'],
        },
        {
            'name': 'Restaurant / Cafe Website',
            'price': '₹8,000 – ₹18,000',
            'tag': 'Hospitality',
            'desc': 'Digital menu, table reservation inquiry, location map, and seamless WhatsApp ordering integration.',
            'deliverables': ['Interactive Digital Food Menu', 'Reservation / Booking Forms', 'Location & Google Maps Embed', 'Photo Gallery', 'Mobile-First Quick Actions'],
        },
        {
            'name': 'Gym / Coaching Website',
            'price': '₹7,000 – ₹15,000',
            'tag': 'Fitness & Education',
            'desc': 'Schedule showcase, trainer profiles, membership tier comparisons, and trial session signups.',
            'deliverables': ['Class Timetables & Batches', 'Trainer / Mentor Showcase', 'Membership Tier Cards', 'Free Trial Request Flow', 'WhatsApp Lead Routing'],
        },
        {
            'name': 'E-commerce Website',
            'price': '₹15,000 – ₹35,000+',
            'tag': 'Full Commerce',
            'desc': 'Complete online store with product catalog, cart, checkout, payment gateway, and order notifications.',
            'deliverables': ['Product Catalog & Filtering', 'Shopping Cart & Checkout', 'Payment Gateway Integration', 'Order Confirmation Emails', 'Customer & Order Management'],
        },
        {
            'name': 'Custom Web Application',
            'price': 'Custom Quote',
            'tag': 'Tailored Software',
            'desc': 'Bespoke web platforms, SaaS MVP development, custom booking engines, or automation dashboards.',
            'deliverables': ['Custom Database Architecture', 'Role-Based User Dashboards', 'API Integrations & Workflows', 'Full Scalability & Testing', 'Detailed Milestones & SOW'],
        },
    ]

    context = {
        'featured_projects': featured_projects,
        'services': services,
        'approved_reviews': approved_reviews,
        'pricing_tiers': pricing_tiers,
        'contact_form': contact_form,
        'review_form': review_form,
        'page_title': 'Lunex Presents — Ideas to Digital Experiences that Grow',
        'meta_description': (
            'We design, develop and build digital solutions for businesses, brands and creators. '
            'Web development, brand identity, social creatives, and privacy compliance.'
        ),
    }
    return render(request, 'core/home.html', context)


def pricing(request):
    """Transparent pricing breakdown, FAQ, and payment terms."""
    contact_form = ContactForm(initial={'enquiry_type': 'quote'})
    context = {
        'contact_form': contact_form,
        'page_title': 'Transparent Website Pricing — Lunex Presents',
        'meta_description': 'Transparent starting pricing for websites, web applications, and digital solutions by Lunex Presents. No hidden charges.',
    }
    return render(request, 'core/pricing.html', context)


def about(request):
    """Editorial About Lunex Presents page."""
    total_projects = Project.objects.count()
    total_services = Service.objects.filter(is_active=True).count()
    context = {
        'total_projects': total_projects,
        'total_services': total_services,
        'page_title': 'About Lunex Presents — Digital Craftsmanship & Purpose',
        'meta_description': 'Who we are, what we build, and our human-first design philosophy. Authentic digital craftsmanship with zero artificial bloat.',
    }
    return render(request, 'core/about.html', context)


def reviews(request):
    """Customer reviews and review submission page."""
    approved_reviews = Review.objects.filter(is_approved=True)
    review_form = ReviewForm()
    context = {
        'reviews': approved_reviews,
        'review_form': review_form,
        'page_title': 'Client Reviews & Feedback — Lunex Presents',
        'meta_description': 'Read genuine feedback from businesses and creators who built their digital platforms with Lunex Presents.',
    }
    return render(request, 'core/reviews.html', context)


def free_demo(request):
    """Free initial concept demo terms and request."""
    form = ContactForm(initial={'enquiry_type': 'demo'})
    context = {
        'form': form,
        'page_title': 'Request a Free Initial Design Demo — Lunex Presents',
        'meta_description': 'Want to see how your website could look before getting started? Request a free initial design concept or preview from Lunex Presents.',
    }
    return render(request, 'core/free_demo.html', context)


def privacy_policy(request):
    """Privacy Policy reflecting DPDP Act 2023 & applicable Indian laws."""
    context = {
        'page_title': 'Privacy Policy — Lunex Presents',
        'meta_description': 'How Lunex Presents collects, protects, and handles personal data across our services and web properties.',
    }
    return render(request, 'core/legal/privacy_policy.html', context)


def terms_and_conditions(request):
    """Terms and Conditions of service."""
    context = {
        'page_title': 'Terms & Conditions — Lunex Presents',
        'meta_description': 'Terms of engagement, client obligations, intellectual property rights, and service delivery policies.',
    }
    return render(request, 'core/legal/terms_and_conditions.html', context)


def refund_policy(request):
    """Refund and Cancellation Policy."""
    context = {
        'page_title': 'Refund & Cancellation Policy — Lunex Presents',
        'meta_description': 'Our milestone-based payment structure, cancellation timelines, and refund terms.',
    }
    return render(request, 'core/legal/refund_policy.html', context)


def payment_policy(request):
    """Service and Payment Policy."""
    context = {
        'page_title': 'Service & Payment Policy — Lunex Presents',
        'meta_description': 'Our 40-40-20 milestone payment model, scope change processes, and handover conditions.',
    }
    return render(request, 'core/legal/payment_policy.html', context)




def help_page(request):
    """
    Help Center & Client Support.
    Provides answers to common questions about starting a project, free demo,
    pricing, revisions, technology stack, DPDP compliance, and direct support.
    """
    contact_form = ContactForm(initial={'enquiry_type': 'general'})
    faq_categories = [
        {
            'title': 'Getting Started & Free Demo',
            'icon': 'bi-rocket-takeoff',
            'desc': 'How we initiate projects, initial concept demos, and timelines.',
            'items': [
                {
                    'q': 'What exactly is the Free Demo offer?',
                    'a': 'Our free demo is an initial design preview or concept tailored to your brand ideas. It helps you visualize layout, typography, and aesthetic direction before committing financially. It is an initial design concept, not a full production-ready code delivery. Full development begins after the project scope, quotation, and payment terms are formally approved.'
                },
                {
                    'q': 'How long does a website project take from start to launch?',
                    'a': 'Standard project turnaround times: Basic Landing Pages take 3 to 5 business days; Business & Portfolio websites take 7 to 14 days; E-commerce & Custom Web Applications take 3 to 5 weeks depending on custom features, third-party integrations, and content readiness.'
                },
                {
                    'q': 'What information do I need to get started?',
                    'a': 'Just your business or brand name, core products or services, preferred design references, and any initial copy or logo assets you have. If you do not have a logo or copy yet, Lunex Presents can develop both under our Branding and Creative services.'
                }
            ]
        },
        {
            'title': 'Pricing, Milestones & Billing',
            'icon': 'bi-cash-coin',
            'desc': 'Transparent pricing ranges, payment terms, and scope management.',
            'items': [
                {
                    'q': 'How does the 40% / 40% / 20% payment milestone work?',
                    'a': 'We never ask for 100% upfront. Our milestone payment schedule is: 40% Advance Payment before development begins; 40% Milestone Payment after the interactive working preview is approved; and 20% Final Payment before final domain deployment and code handover.'
                },
                {
                    'q': 'Are domain, hosting, or third-party fees included?',
                    'a': 'Unless specified in a custom package, domain name registration and cloud hosting fees (e.g. Vercel, Railway, AWS, Hostinger) are paid directly to providers or billed at actual cost. We provide complete end-to-end setup, SSL installation, and DNS configuration without extra service fees.'
                },
                {
                    'q': 'What if my requirements change mid-project?',
                    'a': 'Minor refinements within the agreed scope are included. If you need substantial new pages, features, or integrations, we document an addendum with an honest scope and quotation before writing additional code. No surprise bills.'
                }
            ]
        },
        {
            'title': 'Handover, Ownership & Security',
            'icon': 'bi-shield-check',
            'desc': 'Code ownership, security standards, and post-launch support.',
            'items': [
                {
                    'q': 'Do I own 100% of my website code after launch?',
                    'a': 'Yes, completely. Upon final payment, 100% intellectual property of your custom website code, design files, and database schemas are handed over to you with full repository access.'
                },
                {
                    'q': 'Do you offer support after my website goes live?',
                    'a': 'Every Lunex project includes 30 days of complimentary post-launch support covering bug fixes, browser checks, and minor adjustments. We also offer monthly retainer packages for continuous updates, security audits, and backups.'
                },
                {
                    'q': 'How does Lunex Presents ensure data privacy & DPDP Act compliance?',
                    'a': 'All our websites are built with HTTPS encryption, CSRF protection, SQL injection prevention, strict input sanitization, and compliance with the Digital Personal Data Protection (DPDP) Act 2023. You can also run automated compliance scans on any domain using our built-in AuditFlow platform.'
                }
            ]
        }
    ]

    context = {
        'page_title': 'Help Center & Client Support — Lunex Presents',
        'meta_description': 'Get quick answers to common questions about our web development, pricing, free demos, revisions, payment milestones, and direct support.',
        'faq_categories': faq_categories,
        'contact_form': contact_form,
    }
    return render(request, 'core/help.html', context)


def handler_404(request, exception):
    return render(request, '404.html', status=404)


def handler_500(request):
    return render(request, '500.html', status=500)
