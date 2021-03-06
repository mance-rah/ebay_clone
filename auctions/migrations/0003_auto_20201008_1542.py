# Generated by Django 3.1.1 on 2020-10-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comments_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='product_desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='listings',
            name='product_img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='product_listed',
            field=models.CharField(default='', max_length=64),
        ),
    ]
