from django.shortcuts import render
from rest_framework import generics
from projet.models import Order
from .serializers import OrderSerializer
# Create your views here.

class OrderList(generics.ListCreateAPIView):
    queryset  = Order.objects.all()#orderobject
    serializer_class = OrderSerializer
    

class OrderDetail(generics.RetrieveDestroyAPIView):
    Queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
