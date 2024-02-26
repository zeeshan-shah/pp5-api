from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(
        source="owner.profile.id", allow_null=True
    )
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.image.url", allow_null=True
    )
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the comment.
        """
        request = self.context.get("request")
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Format the creation time of the comment using natural language.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Format the update time of the comment using natural language.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "blog",
            "created_at",
            "updated_at",
            "content",
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for detailed representation of a comment.
    """

    blog = serializers.ReadOnlyField(source="blog.id", allow_null=True)
