# Generated by Django 4.2.3 on 2023-07-19 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0005_alter_manga_total_volume_alter_manga_volume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='total_volume',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='volume',
        ),
    ]
