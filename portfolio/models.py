from django.db import models
from core.models import Stock
# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    stocks = models.ManyToManyField(Stock, through='StockHolding')

    def __str__(self) -> str:
        return self.name

class StockHolding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    avg_buy = models.BigIntegerField(blank=True,null=True)
    invested = models.BigIntegerField(blank=True,null=True)
    current_value = models.BigIntegerField(blank=True,null=True)
    quantity = models.PositiveBigIntegerField()


    def invested_sum(self):
        print("current",self.stock.ltp * self.quantity)
        return self.avg_buy * self.quantity if self.avg_buy and self.quantity else 0
    
    def current_value_sum(self):
        print("current",self.stock.ltp * self.quantity)
        return self.stock.ltp * self.quantity if self.stock.ltp and self.quantity else 0
    
    def save(self, *args, **kwargs):
        self.invested = self.invested_sum()
        self.current_value = self.current_value_sum()
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.quantity} of {self.stock} in {self.portfolio}" 