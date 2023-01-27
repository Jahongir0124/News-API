# Generated by Django 4.1.1 on 2023-01-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Yangilik nomi')),
                ('text', models.TextField(verbose_name='Yangilik matni')),
                ('author', models.CharField(max_length=400, verbose_name='Yangilik muallifi')),
                ('datePublished', models.DateTimeField(verbose_name='Chiqgan sana')),
                ('dataCreated', models.DateTimeField(auto_now_add=True)),
                ('dataUpdated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': "Yangiliklar ro'yxati",
            },
        ),
    ]