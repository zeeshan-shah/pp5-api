from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """
    Model representing a blog post.
    """
    CATEGORY_CHOICES = [
        ('science', 'Science and Technology'),
        ('politics', 'Politics'),
        ('sports', 'Sports'),
        ('travel', 'Travel'),
        ('programming', 'Programming'),
    ]

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(max_length=500, verbose_name='Description')
    content = models.TextField(max_length=4000, blank=True, verbose_name='Content')
    image = models.ImageField(
        upload_to='images/', default='../default_blog_hcaioi',
        verbose_name='Image'
    )
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name='Category'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        """
        String for representing the Blog object.
        """
        return f'{self.title} by {self.owner.username}'

    def get_short_description(self):
        """
        Return a short description for the blog post.
        """
        if len(self.description) > 100:
            return self.description[:100] + '...'
        else:
            return self.description
