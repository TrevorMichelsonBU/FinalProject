# Generated by Django 3.0.7 on 2020-07-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rab', '0009_auto_20200728_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='serve',
            field=models.IntegerField(default=0),
        ),
    ]