from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from blogs.models import Blog
from .models import Like


class LikeTestCase(TestCase):
    def setUp(self):
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
        self.assertEqual(Like.objects.count(), 1)
        like = Like.objects.get(id=1)
        self.assertEqual(like.owner, self.user)
        self.assertEqual(like.blog, self.blog)

    def test_like_list_create_view(self):
        response = self.client.get("/likes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["owner"], self.user.username
        )
        self.assertEqual(response.data["results"][0]["blog"], self.blog.id)

    def test_like_detail_view(self):
        response = self.client.get(f"/likes/{self.like.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["owner"], self.user.username)
        self.assertEqual(response.data["blog"], self.blog.id)
