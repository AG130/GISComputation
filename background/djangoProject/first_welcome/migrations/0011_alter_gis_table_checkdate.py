# Generated by Django 4.0.3 on 2022-10-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_welcome', '0010_check_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gis_table',
            name='checkdate',
            field=models.FloatField(),
        ),
    ]
