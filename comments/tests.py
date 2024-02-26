from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from blogs.models import Blog
from .models import Comment


class CommentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.blog = Blog.objects.create(
            title="Test Blog", content="Test content", owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.comment = Comment.objects.create(
            owner=self.user,
            blog=self.blog,
            content="Test comment content",
        )

    def test_comment_creation(self):
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.content, "Test comment content")

    def test_comment_list_create_view(self):
        response = self.client.get("/comments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if response data contains any items
        if response.data["results"]:
            self.assertEqual(
                response.data["results"][0]["content"], "Test comment content"
            )

    def test_comment_detail_view(self):
        response = self.client.get(f"/comments/{self.comment.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "Test comment content")
