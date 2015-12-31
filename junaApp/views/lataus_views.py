import chardet
import csv
from django.shortcuts import render
from io import StringIO
from junaApp.sql_komentajat import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def lataus(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
        else:
            messages.add_message(request, messages.ERROR, "Et valinnut tiedostoa!")
            return render(request, 'junaApp/lataus.html')
        filestream = _decode(uploaded_file).read()
        reader = csv.reader(filestream.splitlines(), delimiter=",")
        results = [row for row in reader]
        headeri = results[0]
        for line in results[1:]:
            alkio = dict(zip(headeri, line))
            if "nimi" in alkio and not asema_olemassa(alkio["nimi"]):
                luo_asema(alkio)
            if "numero" in alkio and not juna_olemassa(alkio["numero"]):
                luo_juna(alkio)
            if "junan_numero" in alkio and not pysahdys_olemassa(alkio):
                luo_pysahdys(alkio)
        messages.add_message(request, messages.SUCCESS, "Tiedot ladattu!")
    return render(request, 'junaApp/lataus.html')

def _decode(file):
    content = file.read()
    encoding = chardet.detect(content)['encoding']
    content = content.decode(encoding)
    filestream = StringIO(content)
    return filestream