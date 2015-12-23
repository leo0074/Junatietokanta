from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from junaApp.models import Juna
from junaApp import sql_komentajat


def juna(request):
    junat = Juna.objects.raw('SELECT * FROM junaApp_Juna')
    if request.method == 'POST':
        data = request.POST.copy().dict()

        if "create" in data:
             if not data["numero"] or not data["tyyppi"] or not data["lahtoasema"]:
                return _virheviesti(request, data, "Pakollista tietoa puuttuu!", junat)

             if sql_komentajat.juna_olemassa(data["numero"]):
                return _virheviesti(request, data, "Juna  on jo olemassa!", junat)
        sql_komentajat.luo_juna(data)
        messages.add_message(request, messages.SUCCESS, "Juna tallennettu!")
    return render(request, 'junaApp/juna.html')

def _virheviesti(request, data, viesti, junat):
    context = RequestContext(request, data)
    context.update({'junat' : [juna.numero for juna in junat]})
    template = loader.get_template('junaApp/juna.html')
    messages.add_message(request, messages.ERROR, viesti)
    return HttpResponse(template.render(context))
