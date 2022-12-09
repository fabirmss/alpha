from django.urls import path # lib do framework urls path
from . import views # importa da pasta altenticacao o arquivo views

urlpatterns = [
    path('', views.index, name='index'), # define que a pagina index será a principal do app altenticacao
]