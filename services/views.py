from django.shortcuts import render

from .models import Service


def services(request):
    """Services listing page."""
    service_list = Service.objects.filter(is_active=True)
    context = {
        'services': service_list,
        'page_title': 'Our Services — Lunex Presents',
        'meta_description': (
            'Explore Lunex Presents services: professional website design & development, '
            'logo & brand identity, and social media creatives for businesses.'
        ),
    }
    return render(request, 'services/services.html', context)
