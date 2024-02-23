from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers_set"
    )

    # Add distinct related_names for groups and user_permissions
    groups = models.ManyToManyField(
        "auth.Group", 
        verbose_name=("groups"),
        blank=True,
        help_text=("The groups this user belongs to."),
        related_name="customuser_groups"  # Change this related_name
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="customuser_permissions"  # Change this related_name
    )

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"