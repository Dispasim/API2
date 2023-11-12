from django.urls import path
from django.views.generic import TemplateView
#from .views import AccueilView
from . import views

app_name = 'projet'

urlpatterns = [
    path('',TemplateView.as_view(template_name="projet/site.html")),
    #path('test/',TemplateView.as_view(template_name="projet/test.html")),
    path("test", index, name="index"),
    path('test2/',TemplateView.as_view(template_name="projet/test2.html")),
    path('', views.post_view, name='post'),
    #path('<int:nombre_boites>/',accueil,TemplateView.as_view(template_name="projet/index.html")),
    #path('<int:nombre_boites>/', accueil, name='template/projet/index.html'),
    #path('',AccueilView.as_view(template_name="projet/index.html"))
    #path('<int:nombre_boites>/', AccueilView.as_view(), name='accueil')
]