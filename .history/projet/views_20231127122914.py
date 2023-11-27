from django.shortcuts import render
from .models import subtrade




from django.http import HttpResponse
from .models import subtrade
from .forms import CreateSubtradeForm







    





def test(request):
    return render(request,'projet/test.html')



def create_subtrade(request):
    if (request.method=='POST'):
        form = CreateSubtradeForm(request.POST)
        if (form.is_valid()):
            text = form.cleaned_data["text_subtrade"]
            subtrade_ =  subtrade(text_subtrade = text)
            subtrade_.save()
            return HttpResponse("Succès")
    form = CreateSubtradeForm()
    return render(request, "projet/index.html", {"form" : form})

