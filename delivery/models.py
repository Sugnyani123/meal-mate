from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length = 20)
    password= models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.username} {self.password} {self.email} {self.mobile} {self.address}"
    


class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture= models.URLField(max_length = 200, default="https://tse2.mm.bing.net/th?id=OIP.GJMl2OLHcXLBHoj672_JggHaHa&pid=Api&P=0&h=180")
    cuisine= models.CharField(max_length = 203)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.cuisine} {self.rating}/5"
    