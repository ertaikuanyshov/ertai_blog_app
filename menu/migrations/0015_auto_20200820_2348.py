# Generated by Django 3.0.3 on 2020-08-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20200820_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.CharField(choices=[('url', 'Сілтеме'), ('page', 'Парақша')], default=None, max_length=15),
        ),
    ]