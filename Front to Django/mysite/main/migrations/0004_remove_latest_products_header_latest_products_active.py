# Generated by Django 5.0 on 2023-12-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_latest_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latest_products',
            name='header',
        ),
        migrations.AddField(
            model_name='latest_products',
            name='active',
            field=models.BooleanField(default=1, verbose_name='Product active'),
            preserve_default=False,
        ),
    ]
