# Generated by Django 5.0.2 on 2024-03-05 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_user_alter_sale_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 17, 53, 21, 995567)),
        ),
    ]