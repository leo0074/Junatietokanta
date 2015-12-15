from django.shortcuts import render
from junaApp.models import Asema
from django.db import connection

def index(request):
    cursor = connection.cursor()
    #cursor.execute("DELETE FROM junaApp_Asema where nimi='Pasila'")
    #nimet = Asema.objects.raw('SELECT * FROM junaApp_Asema')
    asemat = Asema.objects.all()
    context = {'asemat': asemat}
    return render(request, 'junaApp/index.html', context)