from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
# Create your models here.

class Order(models.Model):

    class OrderObject(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='processed')

    options = ["processing", "Processed"]

    Text = models.TextField()
    ISIN = models.CharField(max_length=12)
    Trade_date = models.DateField()
    Settlement_date = models.DateField()
    Primary_brocker = models.CharField(max_length=100)
    Sens = models.CharField(max_length=100)
    Trader = models.CharField(max_length=100)
    Price = models.IntegerField()
    Size = models.IntegerField()
    Price_Type = models.CharField(max_length=10)
    Currency = models.CharField(max_length=10)
    Clean_Dirty = models.CharField(max_length=100)
    Published = models.DateTimeField(default=timezone.now)
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    #Status = models.CharField(max_length=10, choices = options, default='processing')
    objects = models.Manager()
    OrderObjects =  OrderObject()
