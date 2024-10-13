from rest_framework import serializers
from .models import Portfolio, StockHolding
from core.models import Stock
from core.serializers import StockSerializer



class StockHoldingSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True)

    class Meta:
        model = StockHolding
        fields = ['stock', 'quantity']


class PortfolioSerializer(serializers.ModelSerializer):
    stocks = StockHoldingSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'stocks']