# Generated by Django 3.2.4 on 2021-06-07 19:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.CharField(max_length=1000)),
                ('release_date', models.DateField(verbose_name='date published')),
                ('genre', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=2500)),
                ('review', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
