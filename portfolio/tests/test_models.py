from decimal import Decimal

from django.test import TestCase
from django.core.exceptions import ValidationError

from portfolio.models import Asset, Coin, Portfolio
from accounts.models import CustomUser


class AssetTests(TestCase):
    def setUp(self):
        self.name = 'test coin'
        self.symbol = 'TST'
        self.username = 'Test User'
        self.coin = Coin.objects.create(
            name=self.name,
            symbol=self.symbol,
            decimal_places=2
        )
        self.user = CustomUser.objects.create(
            username=self.username
        )
        self.portfolio = Portfolio.objects.get(
                user=self.user
            )
        self.asset1 = Asset.objects.create(
            coin=self.coin,
            quantity=1,
            price=1,
            portfolio=self.portfolio
        )
        self.asset2 = Asset.objects.create(
            coin=self.coin,
            quantity=2,
            price=2,
            portfolio=self.portfolio
        )

    def test_min_decimal_places(self):
        """ Test if error is raised if invalid decimal places are used """
        with self.assertRaises(ValidationError):
            # Represents one more decimal place than coin's min unit value
            invalid_qty = '0.001'
            
            Asset.objects.create(
                coin=self.coin,
                quantity=invalid_qty,
                price=1,
                portfolio=self.portfolio
            )

    def test_creation_with_float(self):
        """ Test if error is not raised if float is used as input """
        asset = Asset.objects.create(
            coin=self.coin,
            quantity=0.01,
            price=1,
            portfolio=self.portfolio
        )
        self.assertIsInstance(asset, Asset)
        self.assertIsInstance(asset.quantity, Decimal)
        self.assertEqual(asset.quantity, Decimal('0.01'))

    def test_str_coin(self):
        coin = Coin.objects.get(id=1)
        self.assertEqual(str(coin), f'{self.name} - {self.symbol}')

    def test_str_asset(self):
        test_quantity = 1.1
        asset = Asset.objects.create(
            coin=self.coin,
            quantity=test_quantity,
            price=22.01,
            portfolio=self.portfolio
        )
        self.assertEqual(
            str(asset),
            f'{self.coin} - quantity: {test_quantity}'
        )

    def test_str_portfolio(self):
        """ Test string represenation of Portfolio model """
        self.assertEqual(str(self.portfolio), f'Owner: {self.username}')
