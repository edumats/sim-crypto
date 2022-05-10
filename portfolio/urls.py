from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from portfolio import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('buy/', views.AssetCreateView.as_view(), name='buy'),
    path('coins/',
         views.CoinList.as_view(),
         name='coin-list'),
    path('coins/<int:pk>',
         views.CoinDetail.as_view(),
         name='coin-detail'),
    path('assets/',
         views.AssetList.as_view(),
         name='asset-list'),
    path('assets/<int:pk>',
         views.AssetDetail.as_view(),
         name='asset-detail'),
    path('portfolios/',
         views.PortfolioList.as_view(),
         name='portfolio-list'),
    path('portfolios/<int:pk>',
         views.PortfolioDetail.as_view(),
         name='portfolio-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>',
         views.UserDetail.as_view(),
         name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth', include('rest_framework.urls'))
]
