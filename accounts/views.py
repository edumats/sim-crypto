from django.shortcuts import render
from django.http import HttpResponseRedirect
from allauth.account.views import SignupView

from portfolio.models import Coin, Asset, Portfolio
