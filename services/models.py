from django.db import models


class Service(models.Model):
    """A service offered by Lunex Presents."""

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(
        max_length=200,
        help_text="Brief summary shown on cards.",
    )
    full_description = models.TextField(
        help_text="Full description shown on the services page.",
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
