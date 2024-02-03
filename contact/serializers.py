# contact/serializers.py
from rest_framework import serializers
from .models import ContactTicket

class ContactTicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    ticket_status = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def get_ticket_status(self, obj):
        return obj.get_ticket_status_display()

    class Meta:
        model = ContactTicket
        fields = ['owner', 'created_at', 'updated_at', 'category', 'subject',
                  'message', 'ticket_status', 'is_owner', 'id', 'admin_response']
