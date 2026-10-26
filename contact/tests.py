from django.test import TestCase, Client
from django.urls import reverse
from .models import Enquiry


class ContactTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact:contact')
        self.success_url = reverse('contact:success')

    def test_contact_page_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Start a Project')

    def test_valid_enquiry_submission(self):
        data = {
            'name': 'Anita Roy',
            'email': 'anita@example.com',
            'service_interest': 'web',
            'message': 'We need a redesign of our modern e-commerce website.',
            'website': '',
        }
        response = self.client.post(self.url, data=data, follow=True)
        self.assertRedirects(response, self.success_url)
        self.assertEqual(Enquiry.objects.count(), 1)
        enquiry = Enquiry.objects.first()
        self.assertEqual(enquiry.name, 'Anita Roy')
        self.assertEqual(enquiry.service_interest, 'web')

    def test_honeypot_rejects_bots(self):
        data = {
            'name': 'Spam Bot',
            'email': 'bot@spammer.com',
            'service_interest': 'web',
            'message': 'We need a redesign of our modern e-commerce website.',
            'website': 'http://spam-link.xyz',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Enquiry.objects.count(), 0)

    def test_short_message_validation(self):
        data = {
            'name': 'Anita Roy',
            'email': 'anita@example.com',
            'service_interest': 'web',
            'message': 'Too short',
            'website': '',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Enquiry.objects.count(), 0)
