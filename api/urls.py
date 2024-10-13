from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('core/', include('core.urls')),  

    path('portfolio/', include('portfolio.urls'))

]