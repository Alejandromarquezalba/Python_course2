from django.urls import path, include
from MyProject.views import *
from Applic.views import *
from . import views


urlpatterns = [
    path('', Home, name='home'),
    path('acerca/', Acerca, name='acerca'),
    path('contacto/', Contacto, name='contacto'),

    path('form/', Form, name='form'),
    path('search/', Search, name='search'),  
    path('find/', Find, name='Find'),
]

