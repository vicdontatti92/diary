# Generated by Django 3.0 on 2019-12-11 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20191211_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='comp',
            new_name='complete',
        ),
    ]
