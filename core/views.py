from django.shortcuts import render

from portfolio.models import Project
from services.models import Service


def home(request):
    """Homepage view."""
    featured_projects = (
        Project.objects.filter(is_featured=True)
        .select_related('category')
        .prefetch_related('images')[:6]
    )
    services = Service.objects.filter(is_active=True)[:6]
    total_projects = Project.objects.count()
    total_services = Service.objects.filter(is_active=True).count()
    context = {
        'featured_projects': featured_projects,
        'services': services,
        'total_projects': total_projects,
        'total_services': total_services,
        'page_title': 'Lunex Presents — Digital Creative Agency',
        'meta_description': (
            'Lunex Presents is a digital creative agency crafting premium websites, '
            'logos, and social media visuals for local businesses and brands.'
        ),
    }
    return render(request, 'core/home.html', context)



def about(request):
    """About page view."""
    total_projects = Project.objects.count()
    total_services = Service.objects.filter(is_active=True).count()
    context = {
        'total_projects': total_projects,
        'total_services': total_services,
        'page_title': 'About Us — Lunex Presents',
        'meta_description': (
            'Learn about Lunex Presents — our story, mission, and the process '
            'we use to deliver premium digital work for every client.'
        ),
    }
    return render(request, 'core/about.html', context)



def handler_404(request, exception):
    return render(request, '404.html', status=404)


def handler_500(request):
    return render(request, '500.html', status=500)
