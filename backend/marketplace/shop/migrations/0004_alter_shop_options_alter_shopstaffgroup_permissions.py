# Generated by Django 5.0.2 on 2024-03-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("shop", "0003_alter_shop_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="shop",
            options={
                "permissions": [
                    ("create_shop_product", "Can create shop products"),
                    ("update_shop_product", "Can update shop products"),
                    ("delete_shop_product", "Can delete shop products"),
                    ("create_shop_sales", "Can create shop sales"),
                    ("update_shop_sales", "Can update shop sales"),
                    ("delete_shop_sales", "Can delete shop sales"),
                    ("manage_shop_data", "Can manage shop data"),
                    (
                        "can_manage_shop_managers",
                        "Can grant shop permission to other users",
                    ),
                ]
            },
        ),
        migrations.AlterField(
            model_name="shopstaffgroup",
            name="permissions",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={
                    "codename__in": [
                        ("create_shop_product", "Can manage shop products"),
                        (
                            "update_shop_product",
                            "Can only create or update shop products",
                        ),
                        (
                            "delete_shop_product",
                            "Can only create or update shop products",
                        ),
                        ("create_shop_sales", "Can manage shop sales"),
                        ("update_shop_sales", "Can manage shop sales"),
                        ("delete_shop_sales", "Can manage shop sales"),
                        ("manage_shop_data", "Can manage shop data"),
                        (
                            "can_manage_shop_managers",
                            "Can grant shop permission to other users",
                        ),
                    ]
                },
                to="auth.permission",
            ),
        ),
    ]