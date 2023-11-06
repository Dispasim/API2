from rest_framework import serializers
from projet.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("Text","ISIN","Trade_date","Settlement_date","Primary_brocker","Sens","Trader","Price","Size","Price_type","Currency","User")#ajouter status
