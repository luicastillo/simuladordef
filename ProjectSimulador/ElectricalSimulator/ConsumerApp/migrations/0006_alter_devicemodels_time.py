# Generated by Django 4.0.5 on 2022-06-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConsumerApp', '0005_alter_devicemodels_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicemodels',
            name='Time',
            field=models.IntegerField(),
        ),
    ]
