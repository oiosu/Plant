from django.db import models
# from imagekit.processors import ResizeToFill
# from imagekit.models import ProcessedImageField
# from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
