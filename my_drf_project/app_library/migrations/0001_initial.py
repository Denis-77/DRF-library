# Generated by Django 4.2.3 on 2023-07-15 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('surname', models.CharField(max_length=255, verbose_name='Surname')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('isbn', models.CharField(max_length=50, verbose_name='ISBN')),
                ('date_of_issue', models.DateField(verbose_name='Year of issue')),
                ('number_of_pages', models.PositiveIntegerField(verbose_name='Number of pages')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_library.author')),
            ],
        ),
    ]