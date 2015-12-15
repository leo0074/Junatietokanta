from django.shortcuts import render
import chardet
from io import StringIO
import csv
from junaApp.models import Asema



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
        headers = results[0]
        parsed = []
        for line in results[1:]:
            parsed_line = dict(zip(headers, line))
            parsed.append(parsed_line)
        for asema in parsed:
            if not Asema.objects.filter(nimi=asema["nimi"]):
                Asema.objects.create(**asema)
    return render(request, 'junaApp/lataus.html')
