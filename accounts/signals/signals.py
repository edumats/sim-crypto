from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from portfolio.models import Asset, Coin, Portfolio


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_portfolio(sender, instance, created, **kwargs):
    """ Creates a Portfolio instance for a new user """
    if created:
        # Creates or gets US Dollar currency
        coin, _ = Coin.objects.get_or_create(
            name='US Dollar',
            symbol='USD',
            decimal_places=2
        )
        # Creates a Portfolio instance
        portfolio = Portfolio.objects.create(
            user=instance,
        )
        # Creates initial credits in US Dollar
        Asset.objects.create(
            coin=coin,
            quantity=10000,
            price=10000,
            portfolio=portfolio
        )
