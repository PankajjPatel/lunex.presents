from django.shortcuts import render, get_object_or_404

from .models import Project, Category


def work(request):
    """Portfolio grid page with optional category filter."""
    categories = Category.objects.all()
    selected_category = request.GET.get('category', '')

    projects = Project.objects.select_related('category').prefetch_related('images')
    if selected_category:
        projects = projects.filter(category__slug=selected_category)

    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': selected_category,
        'page_title': 'Our Work — Lunex Presents',
        'meta_description': (
            'Browse the Lunex Presents portfolio — websites, logos, brand identities, '
            'and social media creatives for businesses and brands.'
        ),
    }
    return render(request, 'portfolio/work.html', context)


def project_detail(request, slug):
    """Individual project detail page with full gallery images."""
    project = get_object_or_404(
        Project.objects.select_related('category').prefetch_related('images'),
        slug=slug
    )
    related = Project.objects.filter(
        category=project.category
    ).exclude(pk=project.pk).select_related('category').prefetch_related('images')[:3]

    images = list(project.images.all())

    context = {
        'project': project,
        'related_projects': related,
        'images': images,
        'page_title': f'{project.title} — Lunex Presents',
        'meta_description': project.short_description,
    }
    return render(request, 'portfolio/project_detail.html', context)

