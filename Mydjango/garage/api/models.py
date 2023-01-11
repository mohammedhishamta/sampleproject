from django.db import models

# Create your models here.
class garage(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    category=models.TextField(max_length=200)
    fuel=models.CharField(max_length=20)
    colour=models.CharField(max_length=30)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name

