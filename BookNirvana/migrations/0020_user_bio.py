# Generated by Django 4.1.7 on 2023-03-24 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookNirvana', '0019_user_profile_photo_alter_shelf_last_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
