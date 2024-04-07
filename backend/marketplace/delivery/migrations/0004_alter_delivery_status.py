# Generated by Django 5.0.2 on 2024-03-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_delivery_courier_alter_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.IntegerField(
                choices=[
                    (1, 'In-process'),
                    (2, 'Searching'),
                    (3, 'Delivering'),
                    (4, 'Delivered'),
                    (0, 'Canceled'),
                ],
                default='searching',
                max_length=10,
            ),
        ),
    ]
