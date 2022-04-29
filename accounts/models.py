from symtable import Symbol
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from portfolio.models import Coin, Asset, Portfolio

DEFAULT_CREDITS = 10000


class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)