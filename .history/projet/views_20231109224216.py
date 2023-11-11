from django.shortcuts import render
from .models import subtrade


def accueil(request, nombre_boites=5):  
    boites = subtrade.objects.all()[:int(nombre_boites)]
    return render(request, 'template/template/projet/index.html.html', {'boites': boites})
# Create your views here.
