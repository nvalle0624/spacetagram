# Generated by Django 3.2.7 on 2021-09-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20210916_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorites',
            name='id',
            field=models.CharField(default=models.URLField(), max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='image_url',
            field=models.URLField(),
        ),
    ]
