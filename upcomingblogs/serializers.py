from rest_framework import serializers
from .models import UpcomingBlog

class UpcomingBlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = UpcomingBlog
        fields = ['id', 'owner', 'title', 'category', 'release_date']
