from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Breed(models.Model):
    class Integer_choice(models.IntegerChoices):
        LOW = 1
        LOW_MEDIUM = 2
        MEDIUM = 3
        MEDIUM_HIGH = 4
        HIGH = 5
    size_choice = [
            ("ti","Tiny"),
            ("sm","Small"),
            ("me","Medium"),
            ("la","Large"),
            ]
    name = models.CharField(max_length=100, primary_key=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=size_choice)
    friendliness = models.IntegerField(choices=Integer_choice.choices)
    trainability = models.IntegerField(choices=Integer_choice.choices)
    sheddigamount = models.IntegerField(choices=Integer_choice.choices)
    execirseneeds = models.IntegerField(choices=Integer_choice.choices)
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(choices=[("ma","Male"),("fe","Female")])
    color = models.CharField(max_length=10)
    favorite_food = models.CharField(max_length=20)
    favorite_toy = models.CharField(max_length=20)
