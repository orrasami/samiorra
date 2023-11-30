from django.contrib import admin

from .models import Foto, Galeria


@admin.register(Foto)
class FotosAdmin(admin.ModelAdmin):
	list_display = ('nome', 'galeria', 'slug', 'criado', 'modificado', 'ativo')


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
	list_display = ('galeria', 'criado', 'modificado', 'ativo')
