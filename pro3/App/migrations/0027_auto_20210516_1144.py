# Generated by Django 3.0 on 2021-05-16 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_auto_20210516_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='quant',
        ),
    ]
