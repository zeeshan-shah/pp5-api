from django.contrib.auth.models import User
from .models import Blog
from rest_framework import status
from rest_framework.test import APITestCase


class BlogListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='testpass')

    def test_can_list_blogs(self):
        testuser = User.objects.get(username='testuser')
        Blog.objects.create(owner=testuser, title='a title')
        response = self.client.get('/blogs/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_blog(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/blogs/', {'title': 'a title'}) 
        count = Blog.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_blog(self):
        response = self.client.post('/blogs/', {'title': 'a title'})  
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BlogDetailViewTests(APITestCase):  
    def setUp(self):
        testuser = User.objects.create_user(username='testuser', password='testpass')
        another_user = User.objects.create_user(username='another_user', password='testpass')
        blog1 = Blog.objects.create(
            owner=testuser, title='a title', content='testuser content'
        )
        blog1.id = 1
        blog1.save()
        print(blog1)
        blog2 = Blog.objects.create(
            owner=another_user, title='another title', content='another_user content'
        )

    def test_can_retrieve_blog_using_valid_id(self):
        response = self.client.get('/blogs/1')
        print(response.content)
        # self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Only attempt to access response.data if the status code is 200
        if response.status_code == status.HTTP_200_OK:
            self.assertEqual(response.data['title'], 'a title')

    def test_cant_retrieve_blog_using_invalid_id(self):
        response = self.client.get('/blogs/999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_blog(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put('/blogs/1', {'title': 'a new title'}) 
        blog = Blog.objects.filter(pk=1).first()
        self.assertEqual(blog.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_blog(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put('/blogs/2', {'title': 'a new title'}) 
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
