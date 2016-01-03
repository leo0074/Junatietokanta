from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from junaApp import sql_komentajat
from django.contrib.auth.decorators import login_required

@login_required
def asema(request):
    asemat = sql_komentajat.hae_asemat()
    if request.method == 'POST':
        data = request.POST.copy().dict()
        if "create" in data:

            if not data["nimi"] or not data["kaupunki"]:
                return _virheviesti(request, data, "Pakollista tietoa puuttuu!", asemat)

            if sql_komentajat.asema_olemassa(data["nimi"]):
                sql_komentajat.paivita_asema(data)
                messages.add_message(request, messages.SUCCESS, "Asema muutettu!")
            else:
                sql_komentajat.luo_asema(data)
                messages.add_message(request, messages.SUCCESS, "Uusi asema tallennettu!")

        if "delete" in data:
            sql_komentajat.poista_asema(data)
            messages.add_message(request, messages.SUCCESS, "Asema poistettu!")

    return render(request, 'junaApp/asema.html', {'asemat' : [asema.nimi for asema in asemat]})

def _virheviesti(request, data, viesti, asemat):
    context = RequestContext(request, data)
    context.update({'asemat' : [asema.nimi for asema in asemat]})
    template = loader.get_template('junaApp/asema.html')
    messages.add_message(request, messages.ERROR, viesti)
    return HttpResponse(template.render(context))


