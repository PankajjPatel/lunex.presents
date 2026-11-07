from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

ENQUIRY_TYPE_CHOICES = [
    ('general', 'General Project Enquiry'),
    ('demo', 'Free Demo / Concept Request'),
    ('quote', 'Custom Quote Request'),
]

SERVICE_CHOICES = [
    ('web-dev', 'Website Development'),
    ('branding', 'Branding & Graphic Design'),
    ('social', 'Social Media Creatives'),
    ('automation', 'Business Automation'),
    ('ordering', 'Online Ordering & Booking Solutions'),
    ('custom', 'Custom Digital Solutions'),
    ('other', 'Other / Consultation'),
]

WEBSITE_TYPE_CHOICES = [
    ('landing', 'Basic Landing Page (₹3,000–₹5,000)'),
    ('portfolio', 'Portfolio Website (₹4,000–₹8,000)'),
    ('business', 'Business Website (₹7,000–₹15,000)'),
    ('restaurant', 'Restaurant / Cafe Website (₹8,000–₹18,000)'),
    ('gym', 'Gym / Coaching Website (₹7,000–₹15,000)'),
    ('ecommerce', 'E-commerce Website (₹15,000–₹35,000+)'),
    ('custom_app', 'Custom Web Application (Custom Quote)'),
    ('not_sure', 'Not sure yet / Need recommendation'),
]

BUDGET_CHOICES = [
    ('under_5k', '₹3,000 – ₹5,000'),
    ('5k_10k', '₹5,000 – ₹10,000'),
    ('10k_20k', '₹10,000 – ₹20,000'),
    ('20k_35k', '₹20,000 – ₹35,000'),
    ('above_35k', '₹35,000+'),
    ('flexible', 'Flexible / Scope-dependent'),
]


class Enquiry(models.Model):
    """A client enquiry, free demo request, or custom quote request."""

    enquiry_type = models.CharField(
        max_length=20,
        choices=ENQUIRY_TYPE_CHOICES,
        default='general',
        verbose_name="Enquiry Purpose",
    )
    name = models.CharField(max_length=120, verbose_name="Customer Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=30, blank=True, verbose_name="Phone Number")
    business_name = models.CharField(max_length=140, blank=True, verbose_name="Business / Brand Name")

    service_interest = models.CharField(
        max_length=30,
        choices=SERVICE_CHOICES,
        default='web-dev',
        verbose_name="Service Required",
    )
    website_type = models.CharField(
        max_length=40,
        choices=WEBSITE_TYPE_CHOICES,
        default='business',
        blank=True,
        verbose_name="Website Type",
    )
    expected_features = models.TextField(
        blank=True,
        help_text="Key features expected (e.g. WhatsApp booking, payments, contact form, CMS, etc.)",
    )
    budget_range = models.CharField(
        max_length=30,
        choices=BUDGET_CHOICES,
        blank=True,
        default='flexible',
        verbose_name="Budget Range",
    )
    message = models.TextField(
        verbose_name="Project Details / Requirements",
        help_text="Detailed description of your business needs, goals, or questions.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(
        default=False,
        help_text="Mark as read once you've reviewed this enquiry.",
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Customer Enquiry'
        verbose_name_plural = 'Customer Enquiries'

    def __str__(self):
        return f"[{self.get_enquiry_type_display()}] {self.name} — {self.business_name or self.email} ({self.created_at.strftime('%d %b %Y')})"


class Review(models.Model):
    """
    Customer review and rating system.
    Strictly moderated: only approved reviews appear publicly.
    """

    client_name = models.CharField(max_length=120, verbose_name="Client Name")
    business_name = models.CharField(
        max_length=140,
        blank=True,
        verbose_name="Business / Organization",
    )
    project_title = models.CharField(
        max_length=140,
        blank=True,
        verbose_name="Project / Service Delivered",
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5,
        help_text="Rating from 1 to 5 stars.",
    )
    feedback = models.TextField(
        verbose_name="Client Feedback",
        help_text="Honest review of the deliverables, communication, and results.",
    )
    is_verified_client = models.BooleanField(
        default=False,
        help_text="Checked only when verified against an actual paid client engagement.",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Moderation check: Must be approved by admin before appearing on the site.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Customer Review'
        verbose_name_plural = 'Customer Reviews'

    def __str__(self):
        status = "Approved" if self.is_approved else "Pending Moderation"
        return f"{self.client_name} ({self.rating}★) — {status}"

    def stars_range(self):
        return range(self.rating)

    def empty_stars_range(self):
        return range(5 - self.rating)
