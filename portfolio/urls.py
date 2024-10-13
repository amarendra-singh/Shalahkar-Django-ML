# portfolio/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockHoldingViewSet, PortfolioViewSet

router = DefaultRouter()
router.register(r'stocks', StockHoldingViewSet)
router.register(r'portfolios', PortfolioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]