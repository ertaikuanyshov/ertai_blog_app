# Generated by Django 3.0.3 on 2020-07-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_wppostmeta_is_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wppostmeta',
            old_name='meta_value',
            new_name='views_count',
        ),
        migrations.RemoveField(
            model_name='wppostmeta',
            name='meta_key',
        ),
        migrations.AlterField(
            model_name='wppostmeta',
            name='post_id',
            field=models.IntegerField(unique=True),
        ),
    ]
