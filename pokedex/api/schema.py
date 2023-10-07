import graphene
from graphene import relay, Field
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType

from .mutations import ChangeName, AddPokemon, RemovePokemon
from .nodes import PokemonNode, TypeNode
from ..models import Pokemon

class Query(object):
    pokemons = DjangoFilterConnectionField(PokemonNode)
    types = DjangoFilterConnectionField(TypeNode)

class Mutation(object):
    change_name = ChangeName.Field()
    add_pokemon = AddPokemon.Field()
    remove_pokemon = RemovePokemon.Field()