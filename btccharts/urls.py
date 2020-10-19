"""Base urls."""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import index, MarketViewSet

router = routers.DefaultRouter()
router.register(r'market', MarketViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path("", index)
]
