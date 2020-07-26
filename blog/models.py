from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    body = models.TextField()
