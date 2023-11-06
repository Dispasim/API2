from rest_framework import serializers
from projet.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("text","isin","trade_date","settlement_date","primary_brocker","sens","trader","price","size","price_type","currency","clean_dirty","user")#ajouter status
        #fields = ("text")
