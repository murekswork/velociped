# Generated by Django 5.0.2 on 2024-03-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('shop', '0005_alter_shop_options_alter_shopstaffgroup_permissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={
                'permissions': [
                    ('create_shop_product', 'Can create shop products'),
                    ('update_shop_product', 'Can update shop products'),
                    ('delete_shop_product', 'Can delete shop products'),
                    ('upload_many_product', 'Can upload many products'),
                    ('create_shop_sales', 'Can create shop sales'),
                    ('update_shop_sales', 'Can update shop sales'),
                    ('delete_shop_sales', 'Can delete shop sales'),
                    ('manage_shop_data', 'Can manage shop data'),
                    (
                        'manage_shop_managers',
                        'Can grant shop permission to other users',
                    ),
                    ('create_product_upload', 'Can create product uploads'),
                    ('delete_product_upload', 'Can delete product uploads'),
                    ('read_product_upload', 'Can read product uploads'),
                ]
            },
        ),
        migrations.AlterField(
            model_name='shopmanager',
            name='title',
            field=models.CharField(default='Shop manager title', max_length=120),
        ),
        migrations.AlterField(
            model_name='shopstaffgroup',
            name='permissions',
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={
                    'codename__in': [
                        'create_shop_product',
                        'update_shop_product',
                        'delete_shop_product',
                        'create_shop_sales',
                        'update_shop_sales',
                        'delete_shop_sales',
                        'manage_shop_data',
                        'manage_shop_managers',
                        'create_product_upload',
                        'delete_product_upload',
                        'read_product_upload',
                    ]
                },
                to='auth.permission',
            ),
        ),
    ]
