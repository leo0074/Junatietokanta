from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from junaApp.models import Asema

@requires_csrf_token
def asema(request):
    asemat = Asema.objects.raw('SELECT * FROM junaApp_Asema')
    if request.method == 'POST':
        data = request.POST.copy().dict()
        if "create" in data:
            if not data["nimi"] or not data["kaupunki"]:
                return _virheviesti(request, data, "Pakollista tietoa puuttuu!", asemat)
            if Asema.objects.filter(nimi=data["nimi"]):
                return _virheviesti(request, data, "Asema  on jo olemassa!", asemat)

            _luo(data)
            messages.add_message(request, messages.SUCCESS, "Asema tallennettu!")

        if "delete" in data:
            _poista(data)
            messages.add_message(request, messages.SUCCESS, "Asema poistettu!")


    return render(request, 'junaApp/asema.html', {'asemat' : [asema.nimi for asema in asemat]})

def _virheviesti(request, data, viesti, asemat):
    context = RequestContext(request, data)
    context.update({'asemat' : [asema.nimi for asema in asemat]})
    template = loader.get_template('junaApp/asema.html')
    messages.add_message(request, messages.ERROR, viesti)
    return HttpResponse(template.render(context))

def _luo(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO junaApp_Asema (nimi, kaupunki, pituus, leveys) VALUES ('"+data["nimi"]+"','"+data["kaupunki"]+"','"+data["pituus"]+"','"+data["leveys"]+"' )")

def _poista(data):
    cursor = connection.cursor()
    cursor.execute("DELETE from junaApp_Asema where nimi='"+data["asema"]+"'")
    cursor.execute("DELETE from junaApp_Pysahdys where  asema='"+data["asema"]+"'")