import graphene as gr
from graphene import relay, Field

from ..models import Pokemon
from .nodes import PokemonNode

class ChangeName(relay.ClientIDMutation):
    class Input:
        number = gr.Int(required=True)
        name = gr.String(required=True)
        
    pokemon=Field(PokemonNode)
    
    @classmethod
    def mutate_and_get_payload(cls, _, __, number, name):    
        pokemon = Pokemon.objects.get(number=number)
        pokemon.name = name

        pokemon.save()

        return ChangeName(pokemon=pokemon)