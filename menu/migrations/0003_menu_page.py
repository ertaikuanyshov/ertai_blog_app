# Generated by Django 3.0.3 on 2020-08-18 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
        ('menu', '0002_auto_20200818_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page.Page'),
        ),
    ]