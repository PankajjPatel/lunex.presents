from django import forms
from django.contrib.auth.forms import AuthenticationForm
from portfolio.models import Project, Category


class DashboardLoginForm(AuthenticationForm):
    """Clean editorial styled login form for Lunex Admin."""

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-cream border-warm py-2',
                'placeholder': 'Admin Username',
                'autocomplete': 'username',
                'autofocus': True,
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control bg-cream border-warm py-2',
                'placeholder': 'Admin Password',
                'autocomplete': 'current-password',
            }
        )
    )


class ProjectForm(forms.ModelForm):
    """Form for adding and editing portfolio projects in dashboard."""

    class Meta:
        model = Project
        fields = [
            'title',
            'slug',
            'category',
            'thumbnail',
            'short_description',
            'description',
            'deliverables',
            'tech_stack',
            'project_url',
            'client_name',
            'is_concept',
            'is_featured',
            'display_order',
            'created_date',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-cream border-warm'}),
            'slug': forms.TextInput(attrs={'class': 'form-control bg-cream border-warm'}),
            'category': forms.Select(attrs={'class': 'form-select bg-cream border-warm'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control bg-cream border-warm'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control bg-cream border-warm'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-cream border-warm', 'rows': 5}),
            'deliverables': forms.TextInput(attrs={'class': 'form-control bg-cream border-warm', 'placeholder': 'e.g. Website Development, UI/UX, SEO'}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control bg-cream border-warm', 'placeholder': 'e.g. Django, Python, PostgreSQL, WhiteNoise'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control bg-cream border-warm', 'placeholder': 'https://example.com'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control bg-cream border-warm', 'placeholder': 'Leave blank for internal/concept'}),
            'is_concept': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control bg-cream border-warm'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control bg-cream border-warm', 'type': 'date'}),
        }

