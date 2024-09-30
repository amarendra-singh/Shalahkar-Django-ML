from django.contrib import admin
from django.urls import path, include
from core.views import HelloWorldView, stock

urlpatterns = [
    path('home', HelloWorldView.as_view()),
    path('stock/', stock, name='stock'),

]