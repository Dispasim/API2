from django.urls import path
from django.views.generic import TemplateView


app_name = 'projet'

urlpatterns = [
    
   
    
    

    path('test4/',TemplateView.as_view(template_name="projet/test4.html")),
]