# Generated by Django 5.0.2 on 2024-03-17 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0004_alter_courier_rank'),
        ('delivery', '0002_alter_delivery_latitude_alter_delivery_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='courier',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to='courier.courier'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.IntegerField(choices=[(1, 'In-process'), (2, 'Searching'), (3, 'Delivering'),
                                      (4, 'Delivered'), (0, 'Canceled')], db_index=True, default='searching', max_length=10),
        ),
    ]
