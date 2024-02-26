from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UpcomingBlog(models.Model):
    """ Model representing upcoming blogs. """

    CATEGORY_CHOICES = [
        ("science", "Science and Technology"),
        ("politics", "Politics"),
        ("sports", "Sports"),
        ("travel", "Travel"),
        ("programming", "Programming"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name="Category"
    )
    release_date = models.DateField()

    class Meta:
        """ Meta class for UpcomingBlog model. """

        ordering = ["release_date"]

    def __str__(self):
        """
        String representation of the
        UpcomingBlog object.
        """

        return f"{self.title} by {self.owner.username}"

    def release_date_has_passed(self):
        """ Check if the release date has passed. """

        today = timezone.now().date()
        return self.release_date < today

    def save(self, *args, **kwargs):
        """
        Save method overridden to delete the entry
        if the release date has passed.
        """

        if self.release_date_has_passed():
            # Delete the entry if the release date has passed
            self.delete()
        else:
            super().save(*args, **kwargs)
