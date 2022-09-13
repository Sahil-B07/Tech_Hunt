from email import message
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login
from django.contrib import messages 

# Create your views here.
def regForm(request):
    return render(request, 'hunt/register.html')

def logForm(request):
    return render(request, 'hunt/login.html')

def handleLogin(request):
    if request.method == 'POST':
        logId = request.POST['loginId']
    
        user = authenticate(username=logId, password='hunter')
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, f"{logId} Logged in successfully.")
            return redirect('home')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('logForm')
    
    return HttpResponse('100 Not Found')

def home(request):
    return render(request, 'hunt/base.html')

def handleregister(request):
    if request.method == 'POST':
        registerId = request.POST['regId']

        myuser = User.objects.create_user(username=registerId, password='hunter')
        myuser.save()
        messages.success(request, f"{registerId} has been registered.")
        return redirect('home')
    else:
        return HttpResponse('404 Not Found')