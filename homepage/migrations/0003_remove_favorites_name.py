# Generated by Django 3.2.7 on 2021-09-16 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_favorites_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='name',
        ),
    ]
