# Generated by Django 3.2.6 on 2022-07-10 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stoppage', '0004_stop_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stop_data',
            name='date',
        ),
        migrations.RemoveField(
            model_name='stop_data',
            name='timestamp',
        ),
    ]