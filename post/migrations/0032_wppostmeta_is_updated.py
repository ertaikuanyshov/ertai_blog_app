# Generated by Django 3.0.3 on 2020-07-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0031_wppostmeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='wppostmeta',
            name='is_updated',
            field=models.BooleanField(default=False),
        ),
    ]
