from django.urls import path
from .views import stock, stock_crud

urlpatterns = [
    path('stocks/', stock, name='stock'),
    path('stocks/<int:pk>/', stock_crud, name='stock_crud'),
]