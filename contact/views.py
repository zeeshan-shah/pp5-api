# contact/views.py
from rest_framework import generics, permissions
from .models import ContactTicket
from .serializers import ContactTicketSerializer
from pp5_api.permissions import IsOwnerOrReadOnly


class ContactTicketListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactTicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ContactTicket.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ContactTicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Edit or delete a contact ticket if you own it.
    """
    serializer_class = ContactTicketSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return ContactTicket.objects.all()
