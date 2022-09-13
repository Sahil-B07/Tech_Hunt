from django.urls import path
from . import views

urlpatterns = [
    path('', views.form),
    path('home', views.home, name='home'),
    path('login', views.handlelogin),
]
