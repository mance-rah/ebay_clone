# Generated by Django 3.1.1 on 2020-10-09 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201008_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='product_desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='listings',
            old_name='product_img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='listings',
            old_name='init_bid',
            new_name='initial_bid',
        ),
        migrations.RenameField(
            model_name='listings',
            old_name='user',
            new_name='listing_user',
        ),
        migrations.RenameField(
            model_name='listings',
            old_name='product_listed',
            new_name='title',
        ),
    ]
