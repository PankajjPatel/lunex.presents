from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Portfolio project category, e.g. Web Design, Logo Design."""

    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    """A portfolio project."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects',
    )
    thumbnail = models.ImageField(
        upload_to='portfolio/',
        blank=True,
        null=True,
        help_text="Main project image (recommended: 800×600px).",
    )
    short_description = models.CharField(
        max_length=200,
        help_text="One-liner shown on the portfolio grid card.",
    )
    description = models.TextField(
        help_text="Full project description shown on the detail page.",
    )
    deliverables = models.TextField(
        blank=True,
        help_text="Comma-separated list of deliverables, e.g. Logo, Brand Guide, Social Kit.",
    )
    client_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Client or brand name. Leave blank to keep anonymous.",
    )
    is_concept = models.BooleanField(
        default=False,
        help_text="Mark as concept/practice project.",
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Show this project in the homepage featured section.",
    )
    display_order = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateField(
        blank=True,
        null=True,
        help_text="Approximate project date.",
    )

    class Meta:
        ordering = ['display_order', '-created_date']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})

    def get_deliverables_list(self):
        """Return deliverables as a clean list."""
        if not self.deliverables:
            return []
        return [d.strip() for d in self.deliverables.split(',') if d.strip()]
