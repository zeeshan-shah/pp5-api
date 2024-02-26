from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing user profile.
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(
        upload_to="images/", default="../default_profile_v1xqwd"
    )

    class Meta:
        """
        Meta class for Profile model.
        """

        ordering = ["-created_at"]

    def __str__(self):
        """
        String representation of the Profile object.
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile for the user upon user creation.
    """
    if created:
        Profile.objects.create(owner=instance)


# Connect the create_profile function to the post_save signal of the User model
post_save.connect(create_profile, sender=User)
