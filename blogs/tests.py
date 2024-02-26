from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Blog


class BlogAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="admin", password="pass")
        self.client.force_authenticate(user=self.user)

    def test_can_list_blog_categories(self):
        response = self.client.get("/blogs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_blogs_in_category(self):
        admin = User.objects.get(username="admin")
        Blog.objects.create(
            owner=admin,
            title="a title",
            category="politics",
            content="content",
        )
        response = self.client.get("/blogs/politics/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_blog(self):
        self.client.login(username="admin", password="pass")
        data = {
            "title": "a title",
            "description": "description",
            "content": "content",
            "category": "science",
        }
        response = self.client.post("/blogs/science/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)

    def test_user_not_logged_in_cant_create_blog(self):
        self.client.logout()
        response = self.client.post("/blogs/science/", {"title": "a title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_retrieve_blog_using_valid_id(self):
        blog = Blog.objects.create(
            owner=self.user,
            title="a title",
            description="description",
            category="science",
        )
        response = self.client.get(f"/blogs/science/{blog.id}/")
        self.assertEqual(response.data["title"], "a title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_blog_using_invalid_id(self):
        response = self.client.get("/blogs/science/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_blog(self):
        self.client.login(username="admin", password="pass")
        blog = Blog.objects.create(
            owner=self.user,
            title="a title",
            description="description",
            category="politics",
            content="content",
        )
        response = self.client.put(
            f"/blogs/politics/{blog.id}/",
            {"title": "a new title", "category": "politics"},
        )
        updated_blog = Blog.objects.get(pk=blog.id)
        self.assertEqual(updated_blog.title, "a new title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_blog(self):
        user2 = User.objects.create_user(username="brian", password="pass")
        blog = Blog.objects.create(
            owner=user2,
            title="another title",
            description="description",
            category="science",
        )
        response = self.client.put(
            f"/blogs/science/{blog.id}/", {"title": "a new title"}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
