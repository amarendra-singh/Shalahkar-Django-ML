from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Stock
from .serializers import StockSerializer

# Create your views here.
    
    
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

@api_view(['GET','PUT','DELETE'])
def stock_crud(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)