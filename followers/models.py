from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model representing followers/following relationship between users.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for Follower model.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        """
        String representation of the Follower object.
        """
        return f'{self.owner} {self.followed}'
