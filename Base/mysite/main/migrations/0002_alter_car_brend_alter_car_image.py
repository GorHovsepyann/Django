# Generated by Django 5.0 on 2023-12-08 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_prod', to='main.brend'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='media/cars/', verbose_name='Car image'),
        ),
    ]
