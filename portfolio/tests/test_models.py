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
        # Gets Portfolio instance created by signals after user creation
        self.portfolio = Portfolio.objects.get(
                user=self.user
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


class PortfolioTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='TestUser'
        )
    
    def test_portfolio_creation_by_customuser(self):
        """ Test if a Portfolio instance is created when User is instantiated """
        portfolio = Portfolio.objects.get(user=self.user)
        self.assertIsInstance(portfolio, Portfolio)
    
    def test_portfolio_str(self):
        """ Test string representation of Portfolio model """
        portfolio = Portfolio.objects.get(user=self.user)
        self.assertEqual(str(portfolio), f'Owner: {portfolio.user.username}')


class CoinTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='TestUser'
        )
    
    def test_coin_creation_by_customuser(self):
        """ Test if a Coin instance is created when User is instantiated """
        coin = Coin.objects.get(
            name='US Dollar',
            symbol='USD',
            decimal_places=2
        )
        self.assertIsInstance(coin, Coin)
    
    def test_coin_str(self):
        """ Test string representation of Portfolio model """
        coin = Coin.objects.get(
            name='US Dollar',
            symbol='USD',
            decimal_places=2
        )
        self.assertEqual(str(coin), 'US Dollar - USD')
