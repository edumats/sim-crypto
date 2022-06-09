import requests
# Allows to create tasks without an app instance
from celery import shared_task


@shared_task
def get_coinbase():
    r = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=USD')
    # Available keys: currency and rates
    usd_to_crypto = r.json()['data']
    print(usd_to_crypto)
    return usd_to_crypto

