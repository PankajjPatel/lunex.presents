from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Portfolio project category, e.g. Web Development, Brand Identity, SaaS & Systems."""

    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    """A portfolio project showcasing genuine agency work or concepts."""

    title = models.CharField(max_length=140)
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
        help_text="Main project image (recommended: 1200x800px).",
    )
    short_description = models.CharField(
        max_length=240,
        help_text="One-liner shown on the portfolio grid card.",
    )
    description = models.TextField(
        help_text="Full project description and context shown on the detail page.",
    )
    deliverables = models.TextField(
        blank=True,
        help_text="Comma-separated deliverables, e.g. Website, Brand Identity, UI/UX.",
    )
    tech_stack = models.CharField(
        max_length=200,
        blank=True,
        help_text="Technology stack, e.g. 'Django, Python, PostgreSQL, WhiteNoise'.",
    )
    project_url = models.URLField(
        blank=True,
        help_text="Live project URL if deployed.",
    )
    client_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Client or brand name. Leave blank if internal/concept.",
    )
    is_concept = models.BooleanField(
        default=False,
        help_text="Clearly marks this as a 'Demo Project' or 'Concept Project'.",
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Show this project in the homepage featured section.",
    )
    display_order = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateField(
        blank=True,
        null=True,
        help_text="Project completion date.",
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

    def get_tech_stack_list(self):
        """Return tech stack items as a clean list."""
        if not self.tech_stack:
            return []
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def get_thumbnail_url(self):
        """Return project thumbnail url or first gallery image url."""
        if self.thumbnail:
            try:
                return self.thumbnail.url
            except ValueError:
                pass
        first_img = self.images.first()
        if first_img and first_img.image:
            try:
                return first_img.image.url
            except ValueError:
                pass
        return ""

    def get_gallery_images(self):
        """Return all gallery images in display order."""
        return self.images.all()


class ProjectImage(models.Model):
    """Gallery image for a project (multi-image showcase)."""

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        upload_to='portfolio/gallery/',
        help_text="Gallery image (recommended: 1200x800px).",
    )
    caption = models.CharField(
        max_length=150,
        blank=True,
        help_text="Caption or view label, e.g. 'Brand Guide', 'Mobile View'.",
    )
    display_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Display order in the project gallery.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'

    def __str__(self):
        return f"{self.project.title} — {self.caption or f'Image #{self.display_order}'}"
