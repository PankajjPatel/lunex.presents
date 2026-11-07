from django.shortcuts import render, get_object_or_404
from .models import Service


def services(request):
    """Editorial Services directory page."""
    service_list = Service.objects.filter(is_active=True)
    context = {
        'services': service_list,
        'page_title': 'Specialized Digital Services — Lunex Presents',
        'meta_description': (
            'Explore our 6 core digital services: Website Development, Branding & Graphic Design, '
            'Social Media Creatives, Business Automation, Online Ordering & Booking, and Custom Digital Solutions.'
        ),
    }
    return render(request, 'services/services.html', context)


def service_detail(request, slug):
    """Detailed page for an individual service offering."""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    other_services = Service.objects.filter(is_active=True).exclude(id=service.id)[:4]
    context = {
        'service': service,
        'other_services': other_services,
        'page_title': f'{service.title} — Lunex Presents',
        'meta_description': service.short_description,
    }
    return render(request, 'services/service_detail.html', context)
