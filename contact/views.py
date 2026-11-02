from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    """General Contact Us page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:success')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'page_title': 'Contact Us — Lunex Presents',
        'meta_description': (
            'Get in touch with Lunex Presents directly. Have questions, feedback, '
            'or want to connect? Reach out via email, Twitter/X, Instagram, or message.'
        ),
    }
    return render(request, 'contact/contact.html', context)


def start_project(request):
    """Dedicated Project Onboarding & Brief page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:success')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'page_title': 'Start a Project — Lunex Presents',
        'meta_description': (
            'Ready to build something extraordinary? Tell us about your vision, '
            'project scope, deliverables, and timeline to receive a custom proposal.'
        ),
    }
    return render(request, 'contact/start_project.html', context)


def contact_success(request):
    """Shown after a successful enquiry submission."""
    context = {
        'page_title': 'Enquiry Received — Lunex Presents',
        'meta_description': 'Your enquiry has been received. We\'ll be in touch soon.',
    }
    return render(request, 'contact/success.html', context)
