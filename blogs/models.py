from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(max_length=500, verbose_name='Description')
    content = models.TextField(blank=True, verbose_name='Content')
    image = models.ImageField(
        upload_to='images/', default='default/default_post_rgq6aq.jpg',
        verbose_name='Image'
        )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f'{self.title} by {self.owner.username}'

    def get_short_description(self):
        return self.description[:100] + ('...' if len(self.description) > 100 else '')

