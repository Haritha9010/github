# Generated by Django 3.0 on 2021-05-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_auto_20210507_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pname',
            field=models.CharField(max_length=300),
        ),
    ]
