# Generated by Django 3.0.6 on 2020-05-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200526_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_data',
            name='Last_Updated',
            field=models.DateTimeField(),
        ),
    ]