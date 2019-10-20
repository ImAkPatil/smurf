import graphene

from graphene import relay

from graphene_django.types import DjangoObjectType

from library.books.models import Category, Book

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node,)

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class CategoryConnetion(relay.Connection):
    class Meta:
        node = CategoryType        

class Query(object):
    category = graphene.Field(CategoryType,
                                id=graphene.Int(),
                                name=graphene.String())
    all_categories = graphene.List(CategoryType)

    categories = relay.ConnectionField(CategoryConnetion)

    book = graphene.Field(BookType,
                         id=graphene.Int(),
                         name=graphene.String())
    all_books = graphene.List(BookType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()        

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.select_related('category').all()


    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Book.objects.get(pk=id)

        if name is not None:
            return Book.objects.get(name=name)

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()
