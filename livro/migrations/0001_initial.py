# Generated by Django 4.2.5 on 2023-09-06 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('data_cadastro', models.DateField(default=datetime.date.today)),
                ('emprestado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Livro',
            },
        ),
    ]