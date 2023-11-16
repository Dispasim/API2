from django.urls import path
from django.views.generic import TemplateView
from .views import test
from .views import create_subtrade

app_name = 'projet'

urlpatterns = [
    
    #path('test/',TemplateView.as_view(template_name="projet/test.html")),
    path("test/", test, name="index"),
    path('', create_subtrade, name='create_subtrade'),
    path('test2/',TemplateView.as_view(template_name="projet/test2.html")),
]