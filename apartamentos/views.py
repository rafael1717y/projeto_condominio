from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def apartamentos_disponiveis(request):
    apartamentos = {
        1: '100',
        2: '200',
        3: "878",
    }

    dados = {
        'dados_apartamentos': apartamentos
    }
    return render(request, 'apartamentos_disponiveis.html', dados )


def visualizacao_apartamento(request):
    return render(request, 'visualizacao_apartamento.html')