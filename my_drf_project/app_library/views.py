from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from app_library.models import Book, Author
from app_library.serializers import BookSerializer, AuthorSerializer


class ListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 300


class BookList(ModelViewSet):
    serializer_class = BookSerializer
    pagination_class = ListPagination
    queryset = Book.objects.all()



class AuthorList(ModelViewSet):
    serializer_class = AuthorSerializer
    pagination_class = ListPagination
    queryset = Author.objects.all()

