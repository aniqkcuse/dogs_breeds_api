from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

# We're going to create two views: Dog and Breed
class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated]
    
    def update(self, request, pk=None):
        queryset = Dog.objects.all()
        dog = get_object_or_404(queryset, pk=pk)
        if request.user.pk != dog.owner.id:
            raise exceptions.PermissionDenied(detail="You can't update data created by another user")
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Dog.objects.all()
        dog = get_object_or_404(queryset, pk=pk)
        if request.user.pk != dog.owner.id:
            raise exceptions.PermissionDenied(detail="You can't delete data created by another user")
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, pk=None):
        queryset = Breed.objects.all()
        breed = get_object_or_404(queryset, pk=pk)
        if request.user.pk != breed.owner.id:
            raise exceptions.PermissionDenied(detail="You can't update data created by another user")
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Breed.objects.all()
        breed = get_object_or_404(queryset, pk=pk)
        if request.user.pk != breed.owner.id:
            raise exceptions.PermissionDenied(detail="You can't delete data created by another user")
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
