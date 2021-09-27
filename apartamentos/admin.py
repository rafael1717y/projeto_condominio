from django.contrib import admin
from .models import Apartamento

class ListandoApartamentos(admin.ModelAdmin):
    list_display = ('id', 'nr_apartamento', 'nome_proprietario', 'categoria', 'bloco')
    list_display_links = ('id', 'nr_apartamento')
    search_fields = ('nr_apartamento', 'nome_proprietario')
    list_filter = ('categoria', )
    list_per_page = 10


admin.site.register(Apartamento, ListandoApartamentos)
