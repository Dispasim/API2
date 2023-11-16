from django.shortcuts import render
from rest_framework import generics
from projet.models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .modele_ia import transform
# Create your views here.

class OrderList(generics.ListCreateAPIView):
    queryset  = Order.objects.all()#orderobject
    serializer_class = OrderSerializer
    

class OrderDetail(generics.RetrieveDestroyAPIView):
    Queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    

class ApplyIaView(generics.CreateAPIView):
    #permission_classes = (permissions.AllowAny,)
    def post(self,request):
        texte = request.data.get("detail")

        order = transform(texte)
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data,status= status.HTTP_201_CREATED)





