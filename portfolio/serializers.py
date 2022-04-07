from rest_framework import serializers

from portfolio.models import Coin, Asset, Portfolio
from accounts.models import CustomUser


class CoinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'name', 'symbol', 'decimal_places']


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Asset
        fields = ['user', 'coin', 'quantity', 'buy_price']


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['assets', 'fiat_currency_quantity']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    assets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='asset-detail',
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'assets']
