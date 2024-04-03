from django.db import models

# Create your models her

class Example(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()