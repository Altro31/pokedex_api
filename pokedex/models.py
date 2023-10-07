from typing import Any
from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
    
    def __str__(self) -> str:
        return self.name
    

class Pokemon(models.Model):
    number = models.PositiveIntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    evolve_from = models.ForeignKey("self",on_delete=models.CASCADE, related_name="evolve_to", blank=True, null=True)
    type_1 = models.ForeignKey(Type, on_delete=models.PROTECT, related_name="pokemon_type_1")
    type_2 = models.ForeignKey(Type, null=True, blank=True, on_delete=models.PROTECT, related_name="pokemon_type_2")
    
    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"
    
    def __str__(self) -> str:
        return f'{self.number} - {self.name}'