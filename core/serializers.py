"""Core app serializers."""
from rest_framework import serializers

from core.models import Market


class MarketSerializer(serializers.ModelSerializer):
    """Market serrializer."""

    class Meta:
        model = Market
        fields = (
            'symbol',
            'currency',
            'latest_trade',
            'bid',
            'ask',
            'high',
            'low',
            'close',
        )
