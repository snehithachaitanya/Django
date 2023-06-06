from django.urls import path
from .views import *
urlpatterns = [
    path('', logIn, name='hl'),
    path('home', home, name='home'),
    path('news',news,name='news'),
    path('register', register, name='register'),
    path('writer', writer, name='writer'),
    path('pomplet', pomplet, name='pomplet'),
    path('horror',horror,name='horror'),
    path('onhorror', OnHorror, name='onhorror'),
    path('action',action,name='action'),
    path('onAction', onAction, name='onAction'),
    path('devetional',devo,name='devo'),
    path('onDev', onDev, name='onDev'),
    path('onnews',onNews,name='onnews'),
    path('onpomplet',onPomplet,name='onpomplet'),
    path('oninsta',onInsta,name='oninsta'),
    path('login',logIn,name='login'),
    path('logout',logOut,name='logout'),
    path('hording',hording,name='hording'),
    path('instagram',instagram,name='insta'),
]