from django.http import HttpResponse
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landingpage.html')

def home(request):
    return render(request, 'homepage.html')

def myclicks(request):
    return render(request, 'myclicks.html')