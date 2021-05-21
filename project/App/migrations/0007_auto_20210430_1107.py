# Generated by Django 3.0 on 2021-04-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20210429_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.IntegerField()),
                ('category', models.CharField(choices=[('sarees', 'sarees'), ('decor', 'decor'), ('toys', 'toy'), ('shirts', 'shirts')], max_length=20)),
                ('im', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='is_status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='im',
            field=models.ImageField(upload_to=''),
        ),
    ]
