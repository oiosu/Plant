from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 추가적인 필드 정의
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # 추가적인 메서드 정의
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"