# Generated by Django 4.2.3 on 2023-12-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0006_remove_manga_total_volume_remove_manga_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='slug',
            field=models.SlugField(default='tr', unique=True),
        ),
    ]
