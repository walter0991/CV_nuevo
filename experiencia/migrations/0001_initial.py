# Generated by Django 3.2.2 on 2021-11-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=50)),
                ('descirpciom', models.CharField(max_length=255)),
            ],
        ),
    ]