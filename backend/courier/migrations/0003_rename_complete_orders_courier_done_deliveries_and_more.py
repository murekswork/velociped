# Generated by Django 5.0.2 on 2024-03-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_alter_courier_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courier',
            old_name='complete_orders',
            new_name='done_deliveries',
        ),
        migrations.AddField(
            model_name='courier',
            name='username',
            field=models.CharField(default='username', max_length=120),
        ),
    ]
