from django.contrib import admin

from .models import Coin, Asset, Portfolio

admin.site.register(Coin)
admin.site.register(Asset)
admin.site.register(Portfolio)
