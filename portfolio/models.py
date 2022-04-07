import decimal
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from djmoney.models.fields import MoneyField


class Coin(models.Model):
    name = models.CharField(max_length=20, unique=True)
    symbol = models.CharField(max_length=5, unique=True)
    decimal_places = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.symbol}'

    class Meta:
        ordering = ['symbol']


class Asset(models.Model):
    coin = models.ForeignKey(
        Coin,
        on_delete=models.CASCADE
    )
    quantity = models.DecimalField(
        max_digits=99,
        decimal_places=20,
    )
    price = MoneyField(
        max_digits=19,
        decimal_places=4,
        default_currency='USD',
        default=10000
    )
    transaction_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f'{self.coin} - quantity: {self.quantity}'

    def clean(self) -> None:
        """
        If quantity's decimal places is less that the coin's allowed value,
        raise error
        """
        quantity = decimal.Decimal(self.quantity)
        # abs() is used to convert negative decimal places to absolute values
        decimal_places = abs(quantity.as_tuple().exponent)

        if decimal_places > self.coin.decimal_places:
            raise ValidationError(
                (f"Quantity has {decimal_places} decimal places "
                 "and is more than currency's minimum unit value "
                 f"which is {self.coin.decimal_places} places")
            )

    def save(self, *args, **kwargs):
        """ In order to run clean method """
        # Coerces quantity to string to prevent precision errors
        # when converting to decimal
        self.quantity = str(self.quantity)
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['transaction_date']


class Portfolio(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    assets = models.ManyToManyField(
        Asset,
        related_name='portfolio_assets'
    )

    def __str__(self) -> str:
        return f'Owner: {self.user}'
