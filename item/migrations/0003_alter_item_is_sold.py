# Generated by Django 4.2.3 on 2023-08-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
