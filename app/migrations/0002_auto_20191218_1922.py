# Generated by Django 3.0.1 on 2019-12-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='number',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
