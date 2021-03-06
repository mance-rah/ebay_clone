from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

CATEGORY_CHOICES = (
    ('Toys and Hobbies', 'TOYS AND HOBBIES'),
    ('Auto', 'AUTO'),
    ('Collectibles and Art', 'COLLECTIBLES AND ART'),
    ('Fashion', 'FASHION'),
    ('Sporting Goods', 'SPORTING GOODS'),
    ('Electronics', 'ELECTRONICS'),
    ('Home and Garden', 'HOME AND GARDEN'),
    ('Other', 'OTHER'),
)
class Listings(models.Model):
    title = models.CharField(max_length=64, default="")
    description = models.TextField(default="")
    image = models.URLField(blank=True, null=True)
    initial_bid = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default="other")
    # active = models.BooleanField(default=1) 
    listing_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    # winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="winner")

    def __str__(self):
        return f"{self.title}: {self.category}"

class Bid(models.Model):
    bid = models.DecimalField(max_digits=8, default=0, decimal_places=2)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bid")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")

    
    def __str__(self):
        return f"{self.listing}: {self.bid}"

class Comments(models.Model):
    comment = models.TextField(max_length=400, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="comments")
    submitted = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['submitted']


    def __str__(self):
        return f"Comment {self.comment} by {self.user}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_list")
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="watched_listings")