from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Follower


class FollowerTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="testuser1",
            email="testuser1@example.com",
            password="testpassword",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            email="testuser2@example.com",
            password="testpassword",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)
        self.follower = Follower.objects.create(
            owner=self.user1, followed=self.user2
        )

    def test_follower_creation(self):
        self.assertEqual(Follower.objects.count(), 1)
        follower = Follower.objects.get(id=1)
        self.assertEqual(follower.owner, self.user1)
        self.assertEqual(follower.followed, self.user2)

    def test_follower_list_create_view(self):
        response = self.client.get("/followers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["owner"], self.user1.username
        )
        self.assertEqual(
            response.data["results"][0]["followed_name"], self.user2.username
        )

    def test_follower_detail_view(self):
        response = self.client.get(f"/followers/{self.follower.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["owner"], self.user1.username)
        self.assertEqual(response.data["followed_name"], self.user2.username)
