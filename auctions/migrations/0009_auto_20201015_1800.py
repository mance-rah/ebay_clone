# Generated by Django 3.1.1 on 2020-10-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(choices=[('toys and hobbies', 'TOYS AND HOBBIES'), ('auto', 'AUTO'), ('collectibles and art', 'COLLECTIBLES AND ART'), ('fashion', 'FASHION'), ('sporting goods', 'SPORTING GOODS'), ('electronics', 'ELECTRONICS'), ('home and garden', 'HOME AND GARDEN'), ('other', 'OTHER')], default='other', max_length=64),
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='listing',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing',
            field=models.ManyToManyField(related_name='watched_listings', to='auctions.Listings'),
        ),
    ]
