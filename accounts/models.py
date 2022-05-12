from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    When creating an instance of this model
    Django signals creates a USD Coin instance, if not present
    also creates a Portfolio and Asset instances
    """
    email_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)