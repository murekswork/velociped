# Generated by Django 5.0.2 on 2024-03-08 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='order.order'
            ),
        ),
    ]
