# Generated by Django 4.1.7 on 2023-04-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0011_sono_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sono',
            name='acordou',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sono',
            name='dormiu',
            field=models.IntegerField(default=0),
        ),
    ]
