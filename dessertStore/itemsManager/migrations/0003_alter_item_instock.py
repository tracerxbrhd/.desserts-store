# Generated by Django 4.2 on 2023-04-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("itemsManager", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="instock",
            field=models.BooleanField(default=False),
        ),
    ]