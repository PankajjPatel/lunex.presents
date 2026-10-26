from django.db import models


SERVICE_CHOICES = [
    ('web', 'Website Design & Development'),
    ('logo', 'Logo Design & Brand Identity'),
    ('social', 'Posters & Social Media Creatives'),
    ('other', 'Other / Not sure yet'),
]


class Enquiry(models.Model):
    """A project enquiry submitted through the contact form."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    service_interest = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        default='other',
        verbose_name='Service of interest',
    )
    message = models.TextField(
        help_text="Project description or enquiry details.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(
        default=False,
        help_text="Mark as read once you've reviewed this enquiry.",
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.name} — {self.get_service_interest_display()} ({self.created_at.strftime('%d %b %Y')})"
