from rest_framework import generics
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementListAPIView(generics.ListAPIView):
    """ A view for retrieving a list of advertisements."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
