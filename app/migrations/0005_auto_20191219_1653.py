# Generated by Django 3.0.1 on 2019-12-19 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='booking_date',
            new_name='booking_for_date',
        ),
    ]
