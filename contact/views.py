from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, ReviewForm
from .models import Enquiry, Review


def contact(request):
    """General Contact Us, Free Demo & Custom Quote page."""
    initial_type = request.GET.get('type', 'general')
    if initial_type not in ['general', 'demo', 'quote']:
        initial_type = 'general'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            messages.success(
                request,
                f"Thank you, {enquiry.name}! Your {enquiry.get_enquiry_type_display()} has been received. We will contact you at {enquiry.email} within 24 hours."
            )
            return redirect('contact:success')
    else:
        form = ContactForm(initial={'enquiry_type': initial_type})

    context = {
        'form': form,
        'initial_type': initial_type,
        'page_title': 'Contact & Request a Quote — Lunex Presents',
        'meta_description': 'Get in touch with Lunex Presents. Request a free initial design demo, custom quote, or discuss your upcoming digital project.',
    }
    return render(request, 'contact/contact.html', context)


def start_project(request):
    """Dedicated Custom Quote & Project Brief page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            messages.success(
                request,
                f"Thank you, {enquiry.name}! Your project brief has been received. We'll prepare a structured scope and quotation for you shortly."
            )
            return redirect('contact:success')
    else:
        form = ContactForm(initial={'enquiry_type': 'quote'})

    context = {
        'form': form,
        'page_title': 'Start a Project / Custom Quote — Lunex Presents',
        'meta_description': 'Submit your project requirements, expected features, and budget to receive an accurate scope and transparent quotation from Lunex Presents.',
    }
    return render(request, 'contact/start_project.html', context)


def free_demo_request(request):
    """Dedicated Free Initial Design Demo Request page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            messages.success(
                request,
                f"Demo request received! We'll review your business concept and reach out with an initial visual preview."
            )
            return redirect('contact:success')
    else:
        form = ContactForm(initial={'enquiry_type': 'demo'})

    context = {
        'form': form,
        'page_title': 'Request a Free Initial Design Demo — Lunex Presents',
        'meta_description': 'Want to see how your website could look before getting started? Request a free initial design demo or preview from Lunex Presents.',
    }
    return render(request, 'contact/free_demo.html', context)


def submit_review(request):
    """Handles client review submission with strict moderation."""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_approved = False
            review.save()
            messages.success(
                request,
                "Thank you for sharing your feedback! Your review has been submitted for moderation and will appear publicly once verified."
            )
            return redirect('core:reviews')
        else:
            messages.error(request, "Please check the review form for errors.")
            return redirect('core:reviews')
    return redirect('core:reviews')


def contact_success(request):
    """Shown after a successful enquiry submission."""
    context = {
        'page_title': 'Enquiry Received — Lunex Presents',
        'meta_description': 'Your enquiry has been received. The Lunex Presents team will be in touch within 24 hours.',
    }
    return render(request, 'contact/success.html', context)
