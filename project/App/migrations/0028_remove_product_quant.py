# Generated by Django 3.0 on 2021-05-16 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_auto_20210516_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quant',
        ),
    ]