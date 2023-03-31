from django.db import models

# Create your models here.

class Portfolio_Item(models.Model):
    img = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    tech = models.CharField(max_length=100)
    desc = models.TextField()
    website = models.CharField(max_length=100, default = "https://aserene.dev")
    github = models.CharField(max_length=100, default = "https://github.com/aserene")