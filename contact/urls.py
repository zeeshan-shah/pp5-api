from django.urls import path
from .views import ContactTicketListCreateView, ContactTicketDetailView

urlpatterns = [
    path('tickets/', ContactTicketListCreateView.as_view(),
         name='contact-ticket-list-create'),
    path('tickets/<int:pk>/', ContactTicketDetailView.as_view(),
         name='contact-ticket-detail'),
]
