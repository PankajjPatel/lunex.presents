from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    """Contact / enquiry form page."""
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
            'Get in touch with Lunex Presents to discuss your next website, logo, '
            'or creative project. We\'d love to hear from you.'
        ),
    }
    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """Shown after a successful enquiry submission."""
    context = {
        'page_title': 'Enquiry Received — Lunex Presents',
        'meta_description': 'Your enquiry has been received. We\'ll be in touch soon.',
    }
    return render(request, 'contact/success.html', context)
