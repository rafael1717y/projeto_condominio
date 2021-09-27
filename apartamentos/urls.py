from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apartamentos_disponiveis', views.apartamentos_disponiveis, name='apartamentos_disponiveis'),
    path('<int:apartamento_id>', views.visualizacao_apartamento, name='visualizacao_apartamento')  ## 1.
]