from django.contrib import admin
from app_library.models import Book, Author

class BookInline(admin.TabularInline):
    model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'isbn', 'date_of_issue', 'number_of_pages', 'author']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'date_of_birth']
    inlines = [BookInline]
