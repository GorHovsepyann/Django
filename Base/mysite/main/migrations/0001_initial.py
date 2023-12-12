# Generated by Django 5.0 on 2023-12-08 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Brend Name')),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Car name')),
                ('image', models.ImageField(upload_to='', verbose_name='Car image')),
                ('price', models.PositiveIntegerField(verbose_name='Car price')),
                ('brend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brend')),
            ],
        ),
    ]