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
    settlement_date = models.DateField()
    primary_brocker = models.CharField(max_length=100)
    sens = models.CharField(max_length=100)
    trader = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    price_type = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    clean_dirty = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    #Status = models.CharField(max_length=10, choices = options, default='processing')
    objects = models.Manager()
    orderobjects =  OrderObject()
    #category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
