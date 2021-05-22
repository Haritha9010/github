# Generated by Django 3.0 on 2021-04-29 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('im', models.ImageField(default='home1.png', upload_to='handcrafts/')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Category')),
            ],
        ),
    ]