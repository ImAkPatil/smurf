import graphene

import library.books.schema

class Query(library.books.schema.Query, graphene.ObjectType):


    pass

schema = graphene.Schema(query=Query)