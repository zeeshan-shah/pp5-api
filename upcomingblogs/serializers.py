from rest_framework import serializers
from .models import UpcomingBlog


class UpcomingBlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the UpcomingBlog model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Check if the requesting user is the owner of the blog.
        """
        request = self.context.get('request')
        return request.user == obj.owner

    class Meta:
        """
        Meta class for UpcomingBlogSerializer.
        """
        model = UpcomingBlog
        fields = [
            'id', 'owner', 'is_owner', 'title',
            'category', 'release_date'
        ]
