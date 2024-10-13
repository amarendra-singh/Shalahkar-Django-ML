from django.shortcuts import render
from rest_framework import viewsets
from .models import Stock, Portfolio, StockHolding
from .serializers import StockSerializer, PortfolioSerializer, StockHoldingSerializer

# Create your views here.

class StockHoldingViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer