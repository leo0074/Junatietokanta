from django.shortcuts import render
import chardet
from io import StringIO
import csv
from junaApp.sql_komentajat import *



def _decode(file):
    content = file.read()
    encoding = chardet.detect(content)['encoding']
    content = content.decode(encoding)
    filestream = StringIO(content)
    return filestream

def lataus(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
        filestream = _decode(uploaded_file).read()
        reader = csv.reader(filestream.splitlines(), delimiter=",")
        results = [row for row in reader]
        headeri = results[0]
        for line in results[1:]:
            alkio = dict(zip(headeri, line))
            if "nimi" in alkio and not asema_olemassa(alkio["nimi"]):
                luo_asema(alkio)
            if "numero" in alkio and not asema_olemassa(alkio["numero"]):
                luo_juna(alkio)




    return render(request, 'junaApp/lataus.html')
