# Generated by Django 3.2.2 on 2021-11-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidadEducativa', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
            ],
        ),
    ]