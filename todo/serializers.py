from .models import Dog, Breed
from django.contrib.auth.models import User
from rest_framework import serializers
from django.http import Http404

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'sheddigamount', 'execirseneeds']
    
    def create(self, validated_data):
        owner = User(id=self.context["request"].user.pk)
        breed = Breed(name=validated_data["name"], owner=owner, size=validated_data["size"], friendliness=validated_data["friendliness"], trainability=validated_data["trainability"], sheddigamount=validated_data["sheddigamount"], execirseneeds=validated_data["execirseneeds"])
        breed.save()
        return breed

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favorite_food', 'favorite_toy']

    def create(self, validated_data):
        owner = User(id=self.context["request"].user.pk)
        dog = Dog(name=validated_data["name"], owner=owner, age=validated_data["age"], breed=validated_data["breed"], gender=validated_data["gender"], color=validated_data["color"], favorite_food=validated_data["favorite_food"], favorite_toy=validated_data["favorite_toy"])
        dog.save()
        return dog
