# Generated by Django 3.2.2 on 2021-11-06 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiencia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiencia',
            old_name='descirpciom',
            new_name='descripcion',
        ),
    ]
