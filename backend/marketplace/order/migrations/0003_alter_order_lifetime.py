# Generated by Django 5.0.2 on 2024-03-08 14:42

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lifetime',
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 8, 14, 44, 54, 490915)
            ),
        ),
    ]
