from django.db import models

# Create your models here.
class Items(models.Model):
    products=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image = models.ImageField(upload_to="", default="")
    def __str__(self):
        return self.products  
class customer(models.Model):
    name=''
    def __str__(self):
        return self.name
class order(models.Model):
    address=''
    def __str__(self):
        return self.address                  