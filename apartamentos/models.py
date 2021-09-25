from django.db import models
from datetime import datetime

class Apartamento(models.Model):
    nr_apartamento = models.IntegerField(blank=True, verbose_name='Número do apartamento')
    nome_proprietario = models.CharField(max_length=200)
    cpf_proprietario = models.CharField(max_length=14, null=False, blank=False, unique=True)
    bloco  = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descricao_apartamento = models.TextField(max_length=100)
    email_morador = models.EmailField(max_length=100)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=True)
    valor_aluguel = models.DecimalField(max_digits=15, decimal_places=2, blank=True)  ## se nao cadastrar deixa em bco 
    valor_venda = models.DecimalField(max_digits=15, decimal_places=2, blank=True) 
    email_proprietario = models.EmailField(default='', max_length=200, verbose_name='Email')
    fone_proprietario = models.IntegerField(blank=True, verbose_name='Número de telefone')
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    ultima_edicao = models.DateTimeField(auto_now_add=False, auto_now=True)
    # não deixar visível qdo se cadastrar um novo apto
    apartamento_publicado = models.BooleanField(default=False)
    # inclusão de um imagem para cada apto
    