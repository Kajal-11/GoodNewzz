# Generated by Django 3.0.6 on 2020-11-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20201121_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sugar',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
