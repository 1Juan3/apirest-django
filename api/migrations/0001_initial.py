# Generated by Django 4.1.3 on 2022-11-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('centroFormacion', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('cedula', models.PositiveIntegerField()),
                ('telefono', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('años', models.PositiveIntegerField()),
            ],
        ),
    ]
