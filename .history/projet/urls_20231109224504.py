from django.urls import path
from django.views.generic import TemplateView

app_name = 'projet'

urlpatterns = [
    path('',TemplateView.as_view(template_name="projet/index.html")),
    path('<int:nombre_boites>/', accueil, name='accueil'),
]