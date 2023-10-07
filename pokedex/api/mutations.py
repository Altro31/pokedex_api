import graphene as gr
from graphene import relay, Field
from graphql import FieldNode

from ..models import Pokemon, Type
from .nodes import PokemonNode


class ChangeName(relay.ClientIDMutation):
    class Input:
        number = gr.Int(required=True)
        name = gr.String(required=True)

    pokemon = Field(PokemonNode)

    @classmethod
    def mutate_and_get_payload(cls, _, __, number, name):
        pokemon = Pokemon.objects.get(number=number)
        pokemon.name = name

        pokemon.save()

        return ChangeName(pokemon=pokemon)


class AddPokemon(relay.ClientIDMutation):
    class Input:
        number = gr.Int(required=True)
        name = gr.String(required=True)
        height = gr.Float()
        weight = gr.Float()
        evolve_from_number = gr.Int()
        type_1 = gr.String(required=True)
        type_2 = gr.String(required=False)

    pokemon = Field(PokemonNode)

    @classmethod
    def mutate_and_get_payload(cls, _, __, number, name, type_1, height=None, weight=None, evolve_from_number=None, type_2=None):
        try:
            pokemon = Pokemon.objects.get(number=number)
        except:
            type_1 = Type.objects.get(name=type_1)
            if type_2:
                type_2 = Type.objects.get(name=type_2)
            if evolve_from_number:
                evolve_from_number = Pokemon.objects.get(number=evolve_from_number)
            pokemon = Pokemon(number=number,
                              name=name,
                              height=height,
                              weight=weight,
                              evolve_from=evolve_from_number,
                              type_1=type_1,
                              type_2=type_2)
            pokemon.save()
        return AddPokemon(pokemon=pokemon)

class RemovePokemon(relay.ClientIDMutation):
    class Input:
        number = gr.Int(required=True)
        
    pokemon = Field(PokemonNode)
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, number):
        pokemon = Pokemon.objects.get(number=number)
        #Guardo el número del pokemon
        number = pokemon.number
        pokemon.delete()
        #Devuelvo a pokemon su número
        pokemon.number = number
        return RemovePokemon(pokemon=pokemon)
