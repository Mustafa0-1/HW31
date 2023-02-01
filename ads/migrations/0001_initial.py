# Generated by Django 4.1.5 on 2023-02-01 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)])),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
            options={
                'verbose_name': 'Объявления',
                'verbose_name_plural': 'Объявление',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категорий',
            },
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('items', models.ManyToManyField(to='ads.ad')),
            ],
            options={
                'verbose_name': 'Подборка',
                'verbose_name_plural': 'Подборки',
            },
        ),
    ]