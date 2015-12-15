from django.shortcuts import render
from junaApp.models import Asema
from django.db import connection

def index(request):
    return render(request, 'junaApp/index.html')