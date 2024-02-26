from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import UpcomingBlog
from django.utils import timezone
from datetime import datetime


class UpcomingBlogAPITestCase(TestCase):
    """
    A TestCase class for testing the
    UpcomingBlog API.
    """

    def setUp(self):
        """
        Set up the test environment by
        creating a test client and a test user.
        """

        self.client = APIClient()
        self.user = User.objects.create_user(username="admin", password="pass")
        self.client.force_authenticate(user=self.user)

    def test_can_list_upcoming_blogs(self):
        """ Test whether upcoming blogs can be listed. """

        response = self.client.get("/upcoming-blogs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_upcoming_blog(self):
        """ Test whether a new upcoming blog can be created. """

        data = {
            "title": "Upcoming Blog Title",
            "category": "science",
            "release_date": "2024-03-01",
        }
        response = self.client.post("/upcoming-blogs/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UpcomingBlog.objects.count(), 1)

    def test_user_not_logged_in_cant_create_upcoming_blog(self):
        """
        Test whether a non-authenticated user can
        create an upcoming blog.
        """

        self.client.logout()
        data = {
            "title": "Upcoming Blog Title",
            "category": "science",
            "release_date": "2024-03-01",
        }
        response = self.client.post("/upcoming-blogs/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_retrieve_upcoming_blog_using_invalid_id(self):
        """
        Test whether an upcoming blog with an invalid ID
        cannot be retrieved.
        """

        response = self.client.get("/upcoming-blogs/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_upcoming_blog(self):
        """
        Test whether a user can update their own
        upcoming blog.
        """

        self.client.login(username="admin", password="pass")

        release_date = "2024-03-01"
        release_date_obj = datetime.strptime(release_date, "%Y-%m-%d").date()

        upcoming_blog = UpcomingBlog.objects.create(
            owner=self.user,
            title="Upcoming Blog Title",
            category="science",
            release_date=release_date_obj,
        )
        response = self.client.put(
            f"/upcoming-blogs/{upcoming_blog.id}/",
            {
                "title": "Updated Upcoming Blog Title",
                "category": "science",
                "release_date": release_date,
            },
        )
        updated_upcoming_blog = UpcomingBlog.objects.get(pk=upcoming_blog.id)
        self.assertEqual(
            updated_upcoming_blog.title, "Updated Upcoming Blog Title"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_upcoming_blog(self):
        """
        Test whether a user cannot update another user's
        upcoming blog.
        """

        user2 = User.objects.create_user(username="brian", password="pass")

        release_date = "2024-03-01"
        release_date_obj = datetime.strptime(release_date, "%Y-%m-%d").date()

        upcoming_blog = UpcomingBlog.objects.create(
            owner=user2,
            title="Another Upcoming Blog Title",
            category="science",
            release_date=release_date_obj,
        )
        response = self.client.put(
            f"/upcoming-blogs/{upcoming_blog.id}/",
            {
                "title": "Updated Upcoming Blog Title",
                "category": "science",
                "release_date": release_date,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
