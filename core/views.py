from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer

# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"})
    
    
@api_view(['GET','POST'])
def stock(requst):
    if requst.method=="GET":
        objs = Stock.objects.all()
        serializer = StockSerializer(objs, many=True)
        return Response(serializer.data)
    
    else:
        data =  requst.data
        serializer = StockSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
