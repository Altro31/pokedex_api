from django.contrib import admin
from .models import Type, Pokemon

# Register your models here.

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    fields = ("number", "name", "height", "weight", "evolve_from", "type_1", "type_2")
    ordering = ("number",)
    
