from django.urls import path
from .views import OrderList, OrderDetail

app_name = 'projet_api'

urlpatterns = [
    path('<int:pk>/',OrderDetail.as_view(),name='detailcreate'),
    path('',OrderList.as_View(), name='listcreate')
]