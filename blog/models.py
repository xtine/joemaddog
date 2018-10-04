from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to='media/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
