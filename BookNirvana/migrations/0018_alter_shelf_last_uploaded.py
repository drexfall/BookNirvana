# Generated by Django 4.1.7 on 2023-03-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookNirvana', '0017_remove_book_likes_remove_book_ratings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='last_uploaded',
            field=models.DateField(auto_created=True),
        ),
    ]
