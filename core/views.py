"""Core views."""
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.models import Market
from core.serializers import MarketSerializer


def index(request):
    """Serve index page."""
    return render(request, 'build/index.html')


class MarketViewSet(ReadOnlyModelViewSet):  # pylint: disable=too-many-ancestors
    """Read-only view for represent Market model."""
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
