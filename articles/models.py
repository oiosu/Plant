from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        # 처리할 작업 목록
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        # 최종 저장 포맷
        options={"quality": 80},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
