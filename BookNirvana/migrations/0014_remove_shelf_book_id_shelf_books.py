# Generated by Django 4.1.7 on 2023-03-20 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookNirvana', '0013_remove_shelf_books_shelf_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelf',
            name='book_id',
        ),
        migrations.AddField(
            model_name='shelf',
            name='books',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
