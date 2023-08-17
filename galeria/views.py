from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Projeto de site do L3 system</h1>')
    
    
    
    
# Create your views here.
