# Generated by Django 4.1.7 on 2023-03-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookNirvana', '0005_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.CharField(max_length=100),
        ),
    ]