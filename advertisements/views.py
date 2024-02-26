from rest_framework import generics
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementListAPIView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
