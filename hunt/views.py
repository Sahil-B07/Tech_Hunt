from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.
def form(request):
    return render(request, 'hunt/register.html')

def home(request):
    return render(request, 'hunt/base.html')

def handlelogin(request):
    if request.method == 'POST':
        registerId = request.POST['regId']

        myuser = User.objects.create_user(username=registerId)
        myuser.save()
        return redirect('home')
    else:
        return HttpResponse('404 Not Found')