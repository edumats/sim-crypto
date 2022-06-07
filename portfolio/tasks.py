from celery.schedules import crontab
# Allows to create tasks without an app instance
from celery import shared_task

from .models import Coin

@shared_task
def example():
    coin = Coin.objects.get(id=1)
    print(coin)
