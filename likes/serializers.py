from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Meta class for LikeSerializer.
        """
        model = Like
        fields = ['id', 'created_at', 'owner', 'blog']

    def create(self, validated_data):
        """
        Create a new Like instance.

        Args:
            validated_data (dict): Validated data for creating a Like instance.

        Returns:
            Like: The created Like instance.

        Raises:
            serializers.ValidationError: Raised if there's
            an integrity error (possible duplicate).
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
