# Generated by Django 3.2.2 on 2021-11-06 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobreMi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobremi',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
    ]