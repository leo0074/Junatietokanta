from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from junaApp import sql_komentajat
from django.contrib.auth.decorators import login_required
from junaApp.utils.mjonoksi import *

@login_required
def pysahdys(request):
    junat = sql_komentajat.hae_junat()
    asemat = sql_komentajat.hae_asemat()
    if request.method == 'POST':
        data = request.POST.copy().dict()

        if not _validoi(data):
            messages.add_message(request, messages.ERROR, "Tietoa puuttuu!")

        elif sql_komentajat.pysahdys_olemassa(data):
            messages.add_message(request, messages.ERROR, "On jo olemassa!")
        else:
            sql_komentajat.luo_pysahdys(data)
            messages.add_message(request, messages.SUCCESS, "Luonti onnistui!")

    return render(request, 'junaApp/pysahdys.html', {'junat' : [{'mjono' : junastr(juna), 'numero' : juna.numero} for juna in junat], 'asemat' : [asema.nimi for asema in asemat]})


def _validoi(data):
    if not data["saapumisaika"]:
        return False
    if not data["lahtoaika"]:
        return False
    return True