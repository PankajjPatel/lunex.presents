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


def handler_404(request, exception):
    return render(request, '404.html', status=404)


def handler_500(request):
    return render(request, '500.html', status=500)
