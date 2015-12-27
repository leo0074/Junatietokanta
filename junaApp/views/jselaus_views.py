from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from junaApp.models import Juna
from junaApp import sql_komentajat
from django.forms import model_to_dict
import json

def jselaus(request):
    all = list(Juna.objects.raw("SELECT * from junaApp_Juna"))
    all = [model_to_dict(one) for one in all]
    jsoni = json.dumps(all, default=date_handler)
    return render(request, 'junaApp/jselaus.html', {"junat" : jsoni})

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj