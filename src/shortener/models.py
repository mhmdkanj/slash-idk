from django.db import models

# Create your models here.
class Shortener(models.Model):
    shortened = models.SlugField(max_length=50, unique=True)
    original = models.URLField(max_length=400)
