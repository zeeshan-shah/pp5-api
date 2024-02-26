from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Advertisement


class AdvertisementTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.advertisement = Advertisement.objects.create(
            title="Test Advertisement",
            content="Test content for advertisement",
            advertisement_type="banner",
            target_url="http://example.com",
            start_date="2024-02-22",
            end_date="2024-02-28",
        )

    def test_advertisement_creation(self):
        self.assertEqual(Advertisement.objects.count(), 1)
        advertisement = Advertisement.objects.get(id=1)
        self.assertEqual(advertisement.title, "Test Advertisement")

    def test_advertisement_list_api_view(self):
        response = self.client.get("/advertisements/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        advertisements = response.data.get("results")  # Extract 'results' key
        self.assertIsNotNone(advertisements)  # Check if 'results' is not None
        self.assertTrue(isinstance(advertisements, list))
        if advertisements:
            self.assertEqual(advertisements[0]["title"], "Test Advertisement")
