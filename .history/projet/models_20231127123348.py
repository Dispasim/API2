from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):

    class OrderObject(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='processed')

    options = ["processing", "Processed"]

    text = models.TextField()
    isin = models.CharField(max_length=12,null=True)
    trade_date = models.DateField(null=True)
    settlement_date = models.DateField(null=True)
    primary_brocker = models.CharField(max_length=100,null=True)
    sens = models.CharField(max_length=100,null=True)
    trader = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    price_type = models.CharField(max_length=10,null=True)
    currency = models.CharField(max_length=10,null=True)
    clean_dirty = models.CharField(max_length=100,null=True)
    Timestamp = models.DateTimeField(default=timezone.now,null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)#pas nécessaire 
    
    objects = models.Manager()
    orderobjects =  OrderObject()
    


    
    


#nomenclature : découper une pâte = subtrade 
#réunion de deux subtrade = brockertrade



