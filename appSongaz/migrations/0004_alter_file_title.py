# Generated by Django 4.2.10 on 2024-03-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSongaz', '0003_file_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
