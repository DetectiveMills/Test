from django.shortcuts import render
from .models import Settings, Collections, Sellers
from django.http import HttpRequest

# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    collections = Collections.objects.all()
    sellers = Sellers.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())


