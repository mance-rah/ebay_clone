# Generated by Django 3.1.1 on 2020-10-21 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201021_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='active',
        ),
    ]
