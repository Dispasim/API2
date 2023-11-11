from django.shortcuts import render
from .models import subtrade
from django.views import View


def accueil(request, nombre_boites=5):  
    boites = subtrade.objects.all()[:int(nombre_boites)]
    return render(request, 'template/template/projet/index.html.html', {'boites': boites})
# Create your views here.

class AccueilView(View):
    template_name = 'projet/index.html'

    def get(self, request, nombre_boites=5):
        boites = subtrade.objects.all()[:int(nombre_boites)]
        return render(request, self.template_name, {'boites': boites})