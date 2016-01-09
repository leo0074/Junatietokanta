from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from junaApp import sql_komentajat
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
import json
from junaApp.utils.mjonoksi import *

@login_required
def juna(request):
    junat = sql_komentajat.hae_junat()

    dumps = list(junat)
    dumps = [model_to_dict(juna) for juna in dumps]
    dumps = json.dumps(dumps, default=date_handler)

    if request.method == 'POST':
        data = request.POST.copy().dict()

        if "create" in data:
            if not _validoi(data):
                return _virheviesti(request, data, "Pakollista tietoa puuttuu!", junat, dumps)

            if sql_komentajat.juna_olemassa(data["numero"]):
                sql_komentajat.paivita_juna(data)
                messages.add_message(request, messages.SUCCESS, "Juna muutettu!")
            else:
                sql_komentajat.luo_juna(data)
                messages.add_message(request, messages.SUCCESS, "Juna tallennettu!")

        if "delete" in data:
            print(data)
            sql_komentajat.poista_juna(data)
            messages.add_message(request, messages.SUCCESS, "Juna poistettu!")
    return render(request, 'junaApp/juna.html', {'junat' : [{'mjono' : junastr(juna), 'numero' : juna.numero} for juna in junat], 'jscript' : dumps})

def _virheviesti(request, data, viesti, junat, dumps):
    context = RequestContext(request, data)
    context.update({'junat' : [{'mjono' : junastr(juna), 'numero' : juna.numero} for juna in junat], 'jscript' : dumps})
    template = loader.get_template('junaApp/juna.html')
    messages.add_message(request, messages.ERROR, viesti)
    return HttpResponse(template.render(context))

def _validoi(data):
    if not data["numero"]:
        return False
    if not data["tyyppi"]:
        return False
    if not data["lahtoasema"]:
        return False
    if not data["paateasema"]:
        return False
    return True

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj
