# Generated by Django 3.0 on 2021-05-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_product_quant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quant',
            field=models.IntegerField(default=1),
        ),
    ]
