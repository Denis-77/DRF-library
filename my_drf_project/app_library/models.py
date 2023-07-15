from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    surname = models.CharField(verbose_name='Surname', max_length=255)
    date_of_birth = models.DateField(verbose_name='Date of Birth')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    isbn = models.CharField(verbose_name='ISBN', max_length=50)
    date_of_issue = models.DateField(verbose_name='Year of issue')
    number_of_pages = models.PositiveIntegerField(verbose_name='Number of pages')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
