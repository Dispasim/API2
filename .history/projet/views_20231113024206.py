from django.shortcuts import render
from .models import subtrade
from django.views import View
from .modele import modele
import requests
from django.urls import reverse
from django.http import HttpResponse
from .models import subtrade
from .forms import CreateSubtradeForm


modele = modele()




    





def index(request):
    return render(request,'projet/test.html')

def post_view(request):
    if request.method == 'POST':
        nombre_boites = request.POST.get('nombre_boites')
        contenu_boites = []

        for i in range(int(nombre_boites)):
            boite_id = 'subtrade{}'.format(i + 1)
            contenu_boite = request.POST.get(boite_id)
            contenu_boites.append(contenu_boite)

        # Faites quelque chose avec les données récupérées, comme les enregistrer dans la base de données
        # ...

        return HttpResponse("Données du formulaire soumises avec succès!")
    else:
        # Traitement si la requête n'est pas de type POST
        return render(request, 'projet/test.html')


def create_subtrade(request):
    if (request.method=='POST'):
        form = CreateSubtradeForm(request.POST)
        if (form.is_valid()):
            text = form.cleaned_data["text_subtrade"]
            subtrade_ =  subtrade(text_subtrade = text)
            subtrade.save()
            return HttpResponse("Succès")
    form = CreateSubtradeForm()
    return render(request, "projet/index.html", {"form" : form})

