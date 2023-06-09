# Generated by Django 4.1.7 on 2023-03-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookNirvana', '0018_alter_shelf_last_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.FileField(default='', upload_to='static/pps/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelf',
            name='last_uploaded',
            field=models.DateField(auto_now=True),
        ),
    ]
