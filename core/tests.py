"""Tests for core app."""
import datetime

from django.test import Client
from django.test import TestCase

from core.models import Market, Currency


class MarketViewSetTestCase(TestCase):
    """Tests for MarketViewSet view."""

    @classmethod
    def setUp(cls):
        cls.client = Client()
        usd = Currency.objects.create(code='USD')
        Market.objects.create(
            symbol='TestUSD',
            currency=usd,
            latest_trade=datetime.datetime.now(),
            close=10,
        )

    def test_market_viewset_respond_success(self):
        """Test if MarketViewSet respond successfully for GET request."""
        response = self.client.get('/api/v1/market/')
        assert response.status_code == 200
