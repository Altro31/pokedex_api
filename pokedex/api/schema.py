import graphene
from graphene import relay, Field
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType

from .mutations import ChangeName
from .nodes import PokemonNode
from ..models import Pokemon

class Query(object):
    pokemon = relay.Node.Field(PokemonNode)
    pokemons = DjangoFilterConnectionField(PokemonNode)

class Mutation(object):
    change_name = ChangeName.Field()