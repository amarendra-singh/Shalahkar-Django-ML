from django.contrib import admin
from . models import Portfolio,StockHolding
from core.models import Stock

class StockHoldingAdmin(admin.ModelAdmin):
    list_display = ['portfolio','stock_ticker','quantity','avg_buy','invested','current_value','stock_ltp','stock_volume']

    def stock_ticker(self, obj):
        return obj.stock.ticker if obj.stock else 'N/A'  # Handle the case where stock is not available
    stock_ticker.short_description = 'Ticker'  # Optional

    def stock_ltp(self, obj):
        return obj.stock.ltp if obj.stock else 'N/A'  # Handle the case where stock is not available
    stock_ltp.short_description = 'Last Traded Price'  # Optional

    def stock_volume(self, obj):
        return obj.stock.volume if obj.stock else 'N/A'  # Handle the case where stock is not available
    stock_volume.short_description = 'Volume'

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(StockHolding,StockHoldingAdmin)