from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Apartamento


def index(request):
    return render(request, 'index.html')


def apartamentos_disponiveis(request):
    apartamentos = Apartamento.objects.all()

    dados = {
        'apartamentos': apartamentos
    }
    return render(request, 'apartamentos_disponiveis.html', dados )  # apartamentos_disponveis === index


def visualizacao_apartamento(request, apartamento_id):
    apartamento = get_object_or_404(Apartamento, pk=apartamento_id)

    apartamento_a_exibir = {
        'apartamento' : apartamento
    }

    return render(request, 'visualizacao_apartamento.html', apartamento_a_exibir)