# Generated by Django 4.2.3 on 2023-07-17 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='local_name', to='manga.language'),
        ),
        migrations.AddField(
            model_name='manga',
            name='original_language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='original_name', to='manga.language'),
        ),
    ]
