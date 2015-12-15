from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from junaApp.models import Asema
from junaApp import sql_komentajat

@requires_csrf_token
def asema(request):
    asemat = Asema.objects.raw('SELECT nimi FROM junaApp_Asema')
    if request.method == 'POST':
        data = request.POST.copy().dict()
        if "create" in data:
            if not data["nimi"] or not data["kaupunki"]:
                return _virheviesti(request, data, "Pakollista tietoa puuttuu!", asemat)
            if Asema.objects.filter(nimi=data["nimi"]):
                return _virheviesti(request, data, "Asema  on jo olemassa!", asemat)

            sql_komentajat.luo_asema(data)
            messages.add_message(request, messages.SUCCESS, "Asema tallennettu!")

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


