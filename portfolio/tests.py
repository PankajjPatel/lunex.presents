from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Project


class PortfolioTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Web Design', slug='web-design')
        self.project = Project.objects.create(
            title='NovaTech Portal',
            slug='novatech-portal',
            client_name='NovaTech Solutions',
            category=self.category,
            short_description='SaaS website and landing page.',
            description='Complete redesign of the NovaTech brand and digital app portal.',
            deliverables='UI Design, Frontend, Backend',
            is_concept=True,
            is_featured=True,
            display_order=1,
        )

    def test_work_page_loads(self):
        response = self.client.get(reverse('portfolio:work'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NovaTech Portal')

    def test_project_detail_page_loads(self):
        response = self.client.get(reverse('portfolio:project_detail', args=[self.project.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NovaTech Solutions')

    def test_nonexistent_project_returns_404(self):
        response = self.client.get(reverse('portfolio:project_detail', args=['nonexistent-project']))
        self.assertEqual(response.status_code, 404)
