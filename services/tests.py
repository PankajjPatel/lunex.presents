from django.test import TestCase, Client
from django.urls import reverse
from .models import Service


class ServicesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.service = Service.objects.create(
            title='Web Development',
            slug='web-development',
            short_description='Fast and responsive web applications.',
            full_description='Complete end-to-end development.',
            icon_class='bi bi-laptop',
            display_order=1,
            is_active=True,
        )

    def test_services_page_loads(self):
        response = self.client.get(reverse('services:services'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Web Development')
