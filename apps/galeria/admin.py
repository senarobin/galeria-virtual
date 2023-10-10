from django.contrib import admin
from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')   
    list_display_links = ('id', 'nome', 'legenda')
    search_fields = ('id', 'nome', 'legenda') 
    list_filter = ('categoria', 'usuario',)
    list_editable = ('publicada',)
    list_per_page = 1
    

admin.site.register(Fotografia, ListandoFotografias)
# Register your models here.
