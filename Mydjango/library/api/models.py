from django.db import models
class Library(models.Model):

    name=models.CharField(unique=True,max_length=300)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=300)
    category=models.CharField(max_length=300)
    author=models.CharField(max_length=300)

    def __str__(self):
        return self.name


