from django import forms
from .models import Enquiry, SERVICE_CHOICES


class ContactForm(forms.ModelForm):
    """
    Project enquiry contact form.
    Includes a honeypot field for basic spam prevention.
    """

    # Honeypot — hidden field that bots fill but real users leave blank
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label='',
    )

    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'service_interest', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
                'id': 'id_name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com',
                'id': 'id_email',
            }),
            'service_interest': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_service_interest',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your project — what do you need, when, and any relevant details...',
                'rows': 5,
                'id': 'id_message',
            }),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'service_interest': 'Service You\'re Interested In',
            'message': 'Project Details',
        }

    def clean_website(self):
        """Honeypot validation — reject if the hidden field was filled."""
        value = self.cleaned_data.get('website', '')
        if value:
            raise forms.ValidationError("Spam detected.")
        return value

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        if len(message.strip()) < 20:
            raise forms.ValidationError(
                "Please provide a bit more detail about your project (at least 20 characters)."
            )
        return message
