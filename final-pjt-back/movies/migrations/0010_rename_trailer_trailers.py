# Generated by Django 3.2.12 on 2022-05-21 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_trailer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='trailer',
            new_name='trailers',
        ),
    ]