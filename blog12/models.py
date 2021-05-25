from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    img = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)