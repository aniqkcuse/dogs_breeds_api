from rest_framework import renderers
from .api import DogViewSet, BreedViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

dog_list = DogViewSet.as_view({'get':'list', 'post':'create'})
dog_detail = DogViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})

breed_list = BreedViewSet.as_view({'get':'list', 'post':'create'})
breed_detail = BreedViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})


urlpatterns = format_suffix_patterns([
    path('api/v1/dogs/', dog_list, name='dog_list'),
    path('api/v1/dogs/<int:pk>/', dog_detail, name='dog_detail'),
    path('api/v1/breeds/', breed_list, name='breed_list'),
    path('api/v1/breeds/<str:pk>/', breed_detail, name='breed_detail')
])
