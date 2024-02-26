from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer class for the current user with
    additional profile information.

    This serializer extends the UserDetailsSerializer
    provided by dj_rest_auth to include additional
    fields related to the user's profile.

    Attributes:
        profile_id (ReadOnlyField): A read-only field
        representing the profile ID associated with
        the current user.
        profile_image (ReadOnlyField): A read-only
        field representing the profile image URL
        associated with the current user.
    """

    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_image = serializers.ReadOnlyField(source="profile.image.url")

    class Meta(UserDetailsSerializer.Meta):
        """
        Meta class extending UserDetailsSerializer.Meta.

        This class defines the fields to be included in
        the serialized representation of the current user,
        including the fields from UserDetailsSerializer.Meta
        and the additional profile fields.
        """

        fields = UserDetailsSerializer.Meta.fields + (
            "profile_id",
            "profile_image",
        )
