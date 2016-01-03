from django.shortcuts import render
from junaApp import sql_komentajat
from django.forms import model_to_dict
import json

def jselaus(request):
    junat = list(sql_komentajat.hae_junat())
    junat = [model_to_dict(juna) for juna in junat]
    junat = json.dumps(junat, default=date_handler)

    pysahdykset = list(sql_komentajat.hae_pysahdykset())
    pysahdykset = [model_to_dict(pysahdys) for pysahdys in pysahdykset]
    pysahdykset[0]["saapumisaika"] = str(pysahdykset[0]["saapumisaika"])
    pysahdykset[0]["lahtoaika"] = str(pysahdykset[0]["lahtoaika"])
    pysahdykset = json.dumps(pysahdykset, default=date_handler)

    return render(request, 'junaApp/jselaus.html', {"junat" : junat, "pysahdykset" : pysahdykset})

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj