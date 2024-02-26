from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import ContactTicket


class ContactTicketTestCase(TestCase):
    """
    A TestCase class for testing ContactTicket
    model and its views.
    """
    def setUp(self):
        """
        Set up the test environment by creating
        a test user, authenticating a test client,
        and creating a sample ContactTicket instance.
        """
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.contact_ticket = ContactTicket.objects.create(
            owner=self.user,
            category="1",
            subject="Test Subject",
            message="Test message for contact ticket",
            ticket_status="0",
        )

    def test_contact_ticket_creation(self):
        """ Test the creation of a ContactTicket instance. """

        self.assertEqual(ContactTicket.objects.count(), 1)
        contact_ticket = ContactTicket.objects.get(id=1)
        self.assertEqual(contact_ticket.subject, "Test Subject")

    def test_contact_ticket_list_create_view(self):
        """
        Test the list and create views
        for ContactTicket instances.
        """

        response = self.client.get("/tickets/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["subject"], "Test Subject"
        )

    def test_contact_ticket_detail_view(self):
        """ Test the detail view for a ContactTicket instance. """

        response = self.client.get(f"/tickets/{self.contact_ticket.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["subject"], "Test Subject")
