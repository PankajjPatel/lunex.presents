from django.db import models


class Service(models.Model):
    """A service offered by Lunex Presents."""

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(
        max_length=255,
        help_text="Brief summary shown on editorial service cards.",
    )
    full_description = models.TextField(
        help_text="Detailed description and service scope.",
    )
    deliverables = models.TextField(
        blank=True,
        help_text="Key deliverables (newline or comma-separated).",
    )
    starting_price = models.CharField(
        max_length=60,
        blank=True,
        help_text="Indicative starting price, e.g. 'From ₹7,000' or 'Custom Quote'.",
    )
    ideal_for = models.CharField(
        max_length=200,
        blank=True,
        help_text="Target business, e.g. 'Local Businesses, Brands & Creators'.",
    )
    icon_class = models.CharField(
        max_length=60,
        default='bi bi-stars',
        help_text="Bootstrap Icons class, e.g. 'bi bi-code-slash'.",
    )
    display_order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

    def get_deliverables_list(self):
        """Return deliverables as clean list."""
        if not self.deliverables:
            return []
        items = [d.strip() for d in self.deliverables.replace('\n', ',').split(',') if d.strip()]
        return items
