from django.views.generic import ListView

# For DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import generics

from portfolio.models import Coin, Asset, Portfolio
from accounts.models import CustomUser
from portfolio.serializers import (
    AssetSerializer,
    CoinSerializer,
    UserSerializer,
    PortfolioSerializer
)


class IndexView(ListView):
    model = Asset
    context_object_name = 'asset_list'
    template_name = 'portfolio/index.html'


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse(
        #     'user-list',
        #     request=request,
        #     format=format
        # ),
        'assets': reverse(
            'asset-list',
            request=request,
            format=format
        ),
        'coins': reverse(
            'coin-list',
            request=request,
            format=format
        ),
        'portfolios': reverse(
            'portfolio-list',
            request=request,
            format=format
        ),
    })


class CoinList(generics.ListCreateAPIView):
    """
    List all coins or create a new coin
    """
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoinDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a coin instance
    """
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class AssetList(generics.ListCreateAPIView):
    """ List all assets or create a new one """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Get, update or delete an asset instance """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class PortfolioList(generics.ListCreateAPIView):
    """ List all portfolios or create a new one """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Get, update or delete a portfolio instance """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
