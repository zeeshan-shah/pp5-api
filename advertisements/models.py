from django.db import models


class Advertisement(models.Model):
    """
    Model representing an advertisement.
    """
    ADVERTISEMENT_TYPES = [
        ('banner', 'Banner Ad'),
        ('video', 'Video Ad'),
        ('popup', 'Popup Ad'),
        ('text', 'Text Ad'),
    ]

    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(max_length=500, blank=True, verbose_name='Content')
    advertisement_type = models.CharField(
        max_length=20, choices=ADVERTISEMENT_TYPES, verbose_name='Ad Type'
    )
    image = models.ImageField(
        upload_to='images/', default='default/ad-here.jpg',
        verbose_name='Image'
    )
    video_url = models.URLField(
        max_length=500, verbose_name='Video URL', null=True, blank=True
    )
    target_url = models.URLField(max_length=500, verbose_name='Target URL')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'

    def __str__(self):
        """
        String for representing the Advertisement object.
        """
        return self.title
