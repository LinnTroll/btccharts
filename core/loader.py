"""Provide functions for load markets data from API to database."""
import datetime
import json
import urllib.request

from core.models import Currency, Market

API_URL = 'http://api.bitcoincharts.com/v1/markets.json'


def _process_market(market):
    code = market['currency']
    currency, _ = Currency.objects.get_or_create(code=code)
    latest_trade = datetime.datetime.fromtimestamp(market['latest_trade'])
    Market.objects.update_or_create(
        symbol=market['symbol'],
        defaults={
            'currency': currency,
            'latest_trade': latest_trade,
            'bid': market['bid'],
            'ask': market['ask'],
            'high': market['high'],
            'low': market['low'],
            'close': market['close'],
        }
    )


def load_data():
    """Load data from API to database."""
    response = urllib.request.urlopen(API_URL)
    markets_data = json.load(response)
    for market in markets_data:
        _process_market(market)
