from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog


class Like(models.Model):
    """
    Model representing a like on a blog post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(
        Blog, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for Like model.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'blog']

    def __str__(self):
        """
        String representation of the Like object.
        """
        return f'{self.owner} {self.blog}'
