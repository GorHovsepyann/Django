# Generated by Django 5.0 on 2023-12-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_best_jewellery_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latest_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50, verbose_name='Header name')),
                ('img', models.ImageField(upload_to='images', verbose_name='Product image')),
                ('name', models.CharField(max_length=50, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
            ],
        ),
    ]
