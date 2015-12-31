from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib import messages

def kirjaudu(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'junaApp/index.html')
            else:
                messages.add_message(request, messages.ERROR, "Account frozen!")
        else:
            messages.add_message(request, messages.ERROR, "Login failed!")
    return render(request, 'junaApp/login.html')
