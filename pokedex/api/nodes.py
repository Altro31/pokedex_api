import graphene as gr
from graphene import relay, Field
from graphene_django import DjangoObjectType
from graphql_relay import from_global_id

from pokedex.models import Pokemon, Type


class PokemonNode(DjangoObjectType):
    class Meta:
        model = Pokemon
        interfaces = (relay.Node,)
        filter_fields = {
            'number': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'name': ['exact', 'icontains',]
        }


class TypeNode(DjangoObjectType):
    class Meta:
        model = Type
        interfaces = (relay.Node,)
        filter_fields = {
            'name': ['exact',]
        }
        