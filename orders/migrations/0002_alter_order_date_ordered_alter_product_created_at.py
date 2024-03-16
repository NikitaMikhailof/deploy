# Generated by Django 5.0.2 on 2024-03-07 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 3, 7, 23, 28, 35, 619911)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 23, 28, 35, 618918)),
        ),
    ]