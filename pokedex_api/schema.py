from graphene import Schema, ObjectType, Field
import pokedex.api.schema as pokedex_api

class Query(pokedex_api.Query,ObjectType):
    pass

class Mutation(pokedex_api.Mutation,ObjectType):
    pass

schema = Schema(
    query = Query,
    #mutation = Mutation,
)


