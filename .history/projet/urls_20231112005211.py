from django.urls import path
from django.views.generic import TemplateView
#from .views import AccueilView
from . import views
from .views import index

app_name = 'projet'

urlpatterns = [
    path('',TemplateView.as_view(template_name="projet/site.html")),
    #path('test/',TemplateView.as_view(template_name="projet/test.html")),
    path("test/", index, name="index"),
    path('test2/',TemplateView.as_view(template_name="projet/test2.html")),
    path('post/', views.post_view, name='post'),
   
]