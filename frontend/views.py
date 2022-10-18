from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myName(request):
    return HttpResponse("hello")

def mynameTemplt(request):
    return render(request, 'index.html')


def name(request):
    return render(request, "name.html", { "name" : "RAJU" })