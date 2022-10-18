from django.urls import path
from . import views

urlpatterns = [
    path('myName/', views.myName),
    path('mynameTemplt/', views.mynameTemplt),
    path('name/', views.name),
]