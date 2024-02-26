from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    """ Serializer for the Advertisement model. """

    class Meta:
        model = Advertisement
        fields = [
            "id",
            "title",
            "content",
            "advertisement_type",
            "image",
            "video_url",
            "target_url",
            "start_date",
            "end_date",
            "created_at",
        ]
