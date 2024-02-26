from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from blogs.models import Blog
from .models import Like


class LikeTestCase(TestCase):
    """
    A TestCase class for testing
    Like model and its views.
    """

    def setUp(self):
        """
        Set up the test environment by creating
        a test user, a test blog, authenticating
        a test client with the test user, and
        creating a sample Like instance.
        """

        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
        )
        self.blog = Blog.objects.create(
            title="Test Blog", content="Test content", owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.like = Like.objects.create(owner=self.user, blog=self.blog)

    def test_like_creation(self):
        """ Test the creation of a Like instance. """

        self.assertEqual(Like.objects.count(), 1)
        like = Like.objects.get(id=1)
        self.assertEqual(like.owner, self.user)
        self.assertEqual(like.blog, self.blog)

    def test_like_list_create_view(self):
        """
        Test the list and create views
        for Like instances.
        """

        response = self.client.get("/likes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["owner"], self.user.username
        )
        self.assertEqual(response.data["results"][0]["blog"], self.blog.id)

    def test_like_detail_view(self):
        """
        Test the detail view for a
        Like instance.
        """

        response = self.client.get(f"/likes/{self.like.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["owner"], self.user.username)
        self.assertEqual(response.data["blog"], self.blog.id)
