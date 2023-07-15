from django.urls import path
from app_library.views import BookList, AuthorList

urlpatterns = [
    path('books/', BookList.as_view({'get': 'list'}), name='books'),
    path('authors/', AuthorList.as_view({'get': 'list'}), name='authors'),
]
