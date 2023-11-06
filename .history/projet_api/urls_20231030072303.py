from django.urls import path
from .views import PostList, PostDetail

app_name = 'projet_api'

urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(),name='detailcreate'),
    path('',PostList.as_View(), name='listcreate')
]