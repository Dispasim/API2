from django.urls import path
from django.views.generic import TemplateView
from .views import AccueilView

app_name = 'projet'

urlpatterns = [
    #path('',TemplateView.as_view(template_name="projet/index.html")),
    #path('<int:nombre_boites>/',accueil,TemplateView.as_view(template_name="projet/index.html")),
    #path('<int:nombre_boites>/', accueil, name='template/projet/index.html'),
    path('',AccueilView.as_view(template_name="projet/index.html"))
]