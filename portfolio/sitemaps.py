from django.contrib.sitemaps import Sitemap
from .models import Project


class ProjectSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.created_date
