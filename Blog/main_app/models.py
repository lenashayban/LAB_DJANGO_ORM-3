from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    is_published = models.BooleanField(default=False)
    publish_date = models.DateField()