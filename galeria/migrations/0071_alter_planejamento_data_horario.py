# Generated by Django 4.2.1 on 2023-06-11 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0070_alter_planejamento_data_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 14, 53, 57, 846666)),
        ),
    ]
