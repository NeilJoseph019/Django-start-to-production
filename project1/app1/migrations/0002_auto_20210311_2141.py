# Generated by Django 3.1.7 on 2021-03-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
