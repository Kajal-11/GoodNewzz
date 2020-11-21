# Generated by Django 3.0.6 on 2020-11-21 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('reminder_message', models.CharField(default='', max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
