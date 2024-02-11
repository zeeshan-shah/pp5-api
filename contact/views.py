from rest_framework import generics, permissions
from .models import ContactTicket
from .serializers import ContactTicketSerializer
from pp5_api.permissions import IsOwnerOrReadOnly


class ContactTicketListCreateView(generics.ListCreateAPIView):
    """
    List or create contact tickets.
    """
    serializer_class = ContactTicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Get the queryset of contact tickets owned by the current user.
        """
        return ContactTicket.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Save the contact ticket with the current user as the owner.
        """
        serializer.save(owner=self.request.user)


class ContactTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a contact ticket if the user owns it.
    """
    serializer_class = ContactTicketSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Get the queryset of all contact tickets.
        """
        return ContactTicket.objects.all()
