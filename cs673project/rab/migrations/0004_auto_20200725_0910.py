# Generated by Django 3.0.8 on 2020-07-25 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rab', '0003_auto_20200725_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='close',
            new_name='close_time',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='open',
            new_name='open_time',
        ),
    ]
