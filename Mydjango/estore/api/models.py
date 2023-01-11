from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):

    name=models.CharField(max_length=300)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(null=True,upload_to="images")

    def __str__(self):
        return self.name
#ORM
#modelname.objects.create(field=value1,field2=value2,,,,)
#products.objet.create(name="oppo",price=30000,description="mobile",category="electroics")

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    data=models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinLengthValidator(1),MaxLengthValidator(5)])
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.comment



