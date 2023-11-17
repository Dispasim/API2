from django.shortcuts import render
from rest_framework import generics
from projet.models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .modele_ia import transform
import random
from rest_framework.exceptions import ValidationError
# Create your views here.

class OrderList(generics.ListCreateAPIView):
    queryset  = Order.objects.all()#orderobject
    serializer_class = OrderSerializer
    

class OrderDetail(generics.RetrieveDestroyAPIView):
    Queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    

class ApplyIaView(APIView):
    #permission_classes = (permissions.AllowAny,)
    def post(self,request):
        texte = request.data.get("text")
        subtrades = []
        for i in range(random.randint(0,10)):

            order = transform(texte)
            order.save()
            serializer = OrderSerializer(order)
            subtrades.append(serializer.data)
        response = {}
        for i in range(len(subtrades)) :
            response[i] = subtrades[i]

        #if len(response) == 0:
            #raise ValidationError("empty text")


        return Response(response)#,status= status.HTTP_201_CREATED)
        #return render(request, "projet/test3.html", {"data": serializer.data})





