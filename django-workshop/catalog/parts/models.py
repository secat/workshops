from django.db import models


# Create your models here.

class CarParts(models.Model):
    name = models.CharField(max_length=64, null=False)
    slug = models.SlugField(max_length=64, unique=True)
    year = models.IntegerField()
    available = models.BooleanField(default=True)

    # add the function to_dict in order to be compatible with json
