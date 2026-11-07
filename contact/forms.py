from django import forms
from .models import Enquiry, Review, SERVICE_CHOICES, WEBSITE_TYPE_CHOICES, BUDGET_CHOICES, ENQUIRY_TYPE_CHOICES


class ContactForm(forms.ModelForm):
    """
    Unified client enquiry, free demo, and custom quote request form.
    Includes honeypot spam protection and input validation.
    """

    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label='',
    )

    class Meta:
        model = Enquiry
        fields = [
            'enquiry_type',
            'name',
            'email',
            'phone',
            'business_name',
            'service_interest',
            'website_type',
            'expected_features',
            'budget_range',
            'message',
        ]
        widgets = {
            'enquiry_type': forms.Select(attrs={
                'class': 'form-select lx-input',
                'id': 'id_enquiry_type',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'Your full name',
                'id': 'id_name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'name@company.com',
                'id': 'id_email',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': '+91 98765 43210 (WhatsApp preferred)',
                'id': 'id_phone',
            }),
            'business_name': forms.TextInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'Company or brand name',
                'id': 'id_business_name',
            }),
            'service_interest': forms.Select(attrs={
                'class': 'form-select lx-input',
                'id': 'id_service_interest',
            }),
            'website_type': forms.Select(attrs={
                'class': 'form-select lx-input',
                'id': 'id_website_type',
            }),
            'expected_features': forms.TextInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'e.g. Online ordering, WhatsApp button, CMS, Payment Gateway...',
                'id': 'id_expected_features',
            }),
            'budget_range': forms.Select(attrs={
                'class': 'form-select lx-input',
                'id': 'id_budget_range',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'Tell us about your project, target audience, reference sites, or questions...',
                'rows': 4,
                'id': 'id_message',
                'required': True,
            }),
        }
        labels = {
            'enquiry_type': 'Request Purpose',
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone / WhatsApp Number',
            'business_name': 'Business / Brand Name',
            'service_interest': 'Service Needed',
            'website_type': 'Website / Solution Type',
            'expected_features': 'Key Features Needed',
            'budget_range': 'Estimated Budget Range',
            'message': 'Project Details & Goals',
        }

    def clean_website(self):
        value = self.cleaned_data.get('website', '')
        if value:
            raise forms.ValidationError("Spam detected.")
        return value

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        if len(message.strip()) < 10:
            raise forms.ValidationError("Please provide at least 10 characters describing your request.")
        return message


class ReviewForm(forms.ModelForm):
    """
    Public customer review submission form.
    Submissions are saved with is_approved=False pending admin moderation.
    """

    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label='',
    )

    class Meta:
        model = Review
        fields = ['client_name', 'business_name', 'project_title', 'rating', 'feedback']
        widgets = {
            'client_name': forms.TextInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'Your Name',
                'required': True,
            }),
            'business_name': forms.TextInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'Business / Brand (optional)',
            }),
            'project_title': forms.TextInput(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'Project e.g. Website Development, Branding',
            }),
            'rating': forms.Select(
                choices=[(5, '★★★★★ (5 - Outstanding)'), (4, '★★★★☆ (4 - Great)'), (3, '★★★☆☆ (3 - Good)'), (2, '★★☆☆☆ (2 - Fair)'), (1, '★☆☆☆☆ (1 - Poor)')],
                attrs={'class': 'form-select lx-input', 'required': True}
            ),
            'feedback': forms.Textarea(attrs={
                'class': 'form-control lx-input',
                'placeholder': 'Share your honest experience working with Lunex Presents...',
                'rows': 4,
                'required': True,
            }),
        }
        labels = {
            'client_name': 'Your Name',
            'business_name': 'Business Name (Optional)',
            'project_title': 'Project Delivered (Optional)',
            'rating': 'Rating',
            'feedback': 'Your Feedback',
        }

    def clean_website(self):
        value = self.cleaned_data.get('website', '')
        if value:
            raise forms.ValidationError("Spam detected.")
        return value

    def clean_feedback(self):
        feedback = self.cleaned_data.get('feedback', '')
        if len(feedback.strip()) < 15:
            raise forms.ValidationError("Please provide at least 15 characters of feedback.")
        return feedback
