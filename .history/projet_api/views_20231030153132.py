from django.shortcuts import render
from rest_framework import generics
from projet.models import Order
from .serializers import OrderSerializer
# Create your views here.

class OrderList(generics.ListCreateAPIView):
    queryset  = Order.objects.all()
    serializer_class = OrderSerializer
    pass

class OrderDetail(generics.RetrieveDestroyAPIView):
    pass
