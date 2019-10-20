import graphene

from graphene_django.types import DjangoObjectType

from library.books.models import Category, Book

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(object):
    category = graphene.Field(CategoryType,
                                id=graphene.Int(),
                                name=graphene.String())
    all_categories = graphene.List(CategoryType)

    book = graphene.Field(BookType,
                         id=graphene.Int(),
                         name=graphene.String())
    all_books = graphene.List(BookType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()        

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.select_related('category').all()