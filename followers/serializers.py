from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    followed_name = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        """
        Meta class for FollowerSerializer.
        """

        model = Follower
        fields = ["id", "owner", "created_at", "followed", "followed_name"]

    def create(self, validated_data):
        """
        Create a new Follower instance.

        Args:
            validated_data (dict): Validated data
            for creating a Follower instance.

        Returns:
            Follower: The created Follower instance.

        Raises:
            serializers.ValidationError: Raised if
            there's an integrity error (possible duplicate).
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
