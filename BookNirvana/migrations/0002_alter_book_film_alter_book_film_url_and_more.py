# Generated by Django 4.1.7 on 2023-03-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookNirvana', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='film',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='book',
            name='film_url',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='followed_by',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='book',
            name='followed_url',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='preceded_by',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='book',
            name='set_in',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
