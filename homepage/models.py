from django.db import models


# Create your models here.

class Favorites(models.Model):
    image_url = models.URLField()
    id = models.CharField(max_length=500, primary_key=True)
