from django.shortcuts import render
from .models import subtrade
from django.views import View
from .modele import modele
import requests


modele = modele()

print("hello world")

def accueil(request):
    if request.method == 'POST':
        # Traitement du formulaire de confirmation
        # Récupérez les boîtes de dialogue sélectionnées et envoyez-les à l'API
        boites_selectionnees = request.POST.getlist('boites_selectionnees')
        # Envoyez les données à l'API pour la transformation et le stockage

        # Redirigez l'utilisateur vers une page de confirmation ou une autre page après le traitement

    else:
        # Affichage des boîtes de dialogue initiales
        nombre_boites = 5  # Modifier selon vos besoins
        api_url = 'http://127.0.0.1:8000/api/'
        response = requests.get(api_url, params={'nombre_boites': nombre_boites})
        boites = response.json()

        return render(request, 'projet/index.html', {'boites': boites})
    
    
def post(request):
    if request.method == "POST":
        pass
