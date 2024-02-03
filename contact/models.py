# contact/models.py
from django.db import models
from django.contrib.auth.models import User

TICKET_STATUSES = (
    ('0', 'Pending'),
    ('1', 'In Progress'),
    ('2', 'Resolved'),
    ('3', 'On Hold'),
)

CONTACT_CATEGORIES = (
    ('1', 'Blog Inquiry'),
    ('2', 'Technical Support'),
    ('3', 'Business Partnership'),
    ('4', 'General Inquiry'),
)

class ContactTicket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=1, choices=CONTACT_CATEGORIES, default='1')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    ticket_status = models.CharField(max_length=1, choices=TICKET_STATUSES, default='0')
    admin_response = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'Contact Ticket #{self.id} - {self.subject}'
