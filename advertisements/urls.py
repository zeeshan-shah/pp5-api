from django.urls import path
from .views import AdvertisementListAPIView

urlpatterns = [
    path('advertisements/', AdvertisementListAPIView.as_view(), name='advertisement-list'),
]
