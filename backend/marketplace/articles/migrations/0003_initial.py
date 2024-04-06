# Generated by Django 5.0.2 on 2024-03-08 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0002_initial"),
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="user",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
