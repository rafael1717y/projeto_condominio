from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def apartamentos_disponiveis(request):
    return render(request, 'apartamentos_disponiveis.html')


def visualizacao_apartamento(request):
    return render(request, 'visualizacao_apartamento.html')