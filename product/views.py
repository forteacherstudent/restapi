from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import products
from product.serializers import dataserializer
from rest_framework import viewsets

class ProdViewSet(viewsets.ModelViewSet):
    serializer_class = dataserializer
    queryset = products.objects.all()

@api_view(['GET'])
def viewproducts(request):
    #QuerySet = products.objects.get(nm='Xerox')
    QuerySet = products.objects.all()
    s = dataserializer(QuerySet,many=True) 
    return Response(s.data)

# Create your views here.
