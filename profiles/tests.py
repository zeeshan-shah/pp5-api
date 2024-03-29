from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Profile


class ProfileTestCase(TestCase):
    """ A TestCase class for testing Profile model
    and its views.
    """

    def setUp(self):
        """
        Set up the test environment by creating a
        test user, authenticating a test client
        with the test user.
        """

        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_profile_creation(self):
        """ Test the creation of a Profile instance. """

        self.assertEqual(Profile.objects.count(), 1)
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.owner, self.user)
        self.assertEqual(profile.owner.username, "testuser")

    def test_profile_list_view(self):
        """ Test the list view for Profile instances. """

        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        results = response.data.get("results", [])
        self.assertTrue(results)
        self.assertIsInstance(results, list)
        self.assertTrue(results[0].get("owner"))
        self.assertEqual(results[0]["owner"], self.user.username)

    def test_profile_detail_view(self):
        """ Test the detail view for a Profile instance. """

        response = self.client.get(f"/profiles/{self.user.profile.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["owner"], self.user.username)
