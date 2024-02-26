from rest_framework import serializers
from blogs.models import Blog
from likes.models import Like


class BlogCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the category field of the Blog model.
    """

    class Meta:
        model = Blog
        fields = ["category"]


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog model.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validate the uploaded image.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size larger than 2MB!")
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height larger than 4096px!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width larger than 4096px!"
            )
        return value

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the blog.
        """
        request = self.context.get("request")
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Get the ID of the like associated with the current user and blog.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, blog=obj).first()
            return like.id if like else None
        return None

    class Meta:
        model = Blog
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "like_id",
            "likes_count",
            "comments_count",
            "category",
        ]
