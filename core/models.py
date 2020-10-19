"""Core models."""
from django.db import models


class Currency(models.Model):
    """Currency model."""
    code = models.CharField(max_length=3, primary_key=True)

    def __str__(self):
        return self.code


class Market(models.Model):
    """Market model."""
    symbol = models.CharField(max_length=32, primary_key=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    latest_trade = models.DateTimeField()
    bid = models.DecimalField(max_digits=30, decimal_places=12, blank=True, null=True)
    ask = models.DecimalField(max_digits=30, decimal_places=12, blank=True, null=True)
    high = models.DecimalField(max_digits=30, decimal_places=12, blank=True, null=True)
    low = models.DecimalField(max_digits=30, decimal_places=12, blank=True, null=True)
    close = models.DecimalField(max_digits=30, decimal_places=12, blank=True, null=True)
