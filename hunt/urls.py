from django.urls import path
from . import views

urlpatterns = [
    path('', views.logForm, name='logForm'),
    path('reg', views.regForm),
    path('home', views.home, name='home'),
    path('register', views.handleregister),
    path('login', views.handleLogin),
    path('logout', views.handelLogout),
]
