from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    contents = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    lookup = models.IntegerField(default=0)