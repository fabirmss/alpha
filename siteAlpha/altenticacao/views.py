from django.shortcuts import render #lib para renderizar paginas

# Create your views here.

def index(request): #view para renderiar a pagina de login
  return render(request,'login.html')
