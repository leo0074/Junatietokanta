from django.contrib.auth import logout
from django.shortcuts import render

def ulos(request):
    logout(request)
    return render(request, 'junaApp/index.html')