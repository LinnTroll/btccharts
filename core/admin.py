"""Admin settings for core app."""
from django.contrib import admin

from core.models import Currency, Market


class CurrencyAdmin(admin.ModelAdmin):
    """Admin for Currency model."""
    list_display = ('code',)


admin.site.register(Currency, CurrencyAdmin)


class MarketAdmin(admin.ModelAdmin):
    """Admin for Market model."""
    list_display = ('symbol', 'currency', 'bid', 'ask', 'high', 'low', 'close', 'latest_trade')


admin.site.register(Market, MarketAdmin)
