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
        self.asset1 = Asset.objects.create(
            coin=self.coin,
            quantity=1,
            price=1
        )
        self.asset2 = Asset.objects.create(
            coin=self.coin,
            quantity=2,
            price=2
        )

    def test_min_decimal_places(self):
        """ Test if error is raised if invalid decimal places are used """
        with self.assertRaises(ValidationError):
            # Represents one more decimal place than coin's min unit value
            invalid_qty = '0.001'
            Asset.objects.create(
                coin=self.coin,
                quantity=invalid_qty,
                price=1
            )

    def test_creation_with_float(self):
        """ Test if error is not raised if float is used as input """
        asset = Asset.objects.create(
            coin=self.coin,
            quantity=0.01
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
            price=22.01
        )
        self.assertEqual(
            str(asset),
            f'{self.coin} - quantity: {test_quantity}'
        )

    def test_portfolio_creation(self):
        """ Test if Portfolio object is successfully created """
        portfolio = Portfolio(user=self.user)
        portfolio.save()
        self.assertIsInstance(portfolio, Portfolio)
        portfolio.assets.add(self.asset1, self.asset2)
        self.assertEqual(portfolio.assets.all().count(), 2)

    def test_str_portfolio(self):
        portfolio = Portfolio(user=self.user)
        self.assertEqual(str(portfolio), f'Owner: {self.username}')
