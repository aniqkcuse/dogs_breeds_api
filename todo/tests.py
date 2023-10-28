import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Dog, Breed
from django.contrib.auth.models import User
from django.test import TestCase
from dotenv import load_dotenv
import os

load_dotenv()

# Obtain the jwt of an admin user
@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def test_token():
    admin = APIClient().post(reverse('auth_register'), data={"username":"admin", "password":os.environ.get("ADMIN_PASSWORD"), "password2":os.environ.get("ADMIN_PASSWORD"), "email":"admin@localhost.com", "first_name":"admin", "last_name":"admin"})
    admin_token = APIClient().post(reverse('token_obtain_pair'), data={"username":"admin", "password":"$Ken2005*"}, format="json")
    admin_user = User.objects.get(username="admin")
    token = admin_token.getvalue().decode()[0:-1].rsplit(":")[2].replace('"', '')

    breed_example = Breed.objects.create(name="breed1", owner=admin_user, size="sm", friendliness=1, trainability=2, sheddigamount=3, execirseneeds=4)
    dog_example = Dog.objects.create(name="dog1", owner=admin_user, age=1, breed=breed_example, gender="ma", color="Yellow", favorite_food="food_example", favorite_toy="toy_example")
    return token

# Basic CRUD of breeds: create, read, update, delete
@pytest.mark.django_db(transaction=True)
def test_create_breeds(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    # Create
    data = {"name":"breed2", "size":"la", "friendliness":4, "trainability":3,"sheddigamount":2, "execirseneeds":1} 
    response_create = client.post(reverse('breed_list'), data=data, format="json")
    assert response_create.status_code == 201

@pytest.mark.django_db(transaction=True)
def test_get_general_breeds(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    response = client.get(reverse('breed_list'))
    assert response.status_code == 200

@pytest.mark.django_db(transaction=True)
def test_get_specific_breed(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    response = client.get(reverse('breed_detail', args=["breed1"]))
    assert response.status_code == 200

@pytest.mark.django_db(transaction=True)
def test_update_breeds(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    data = {"name":"breed1_new", "size":"me", "friendliness":5, "trainability":1, "sheddigamount":5, "execirseneeds":1}
    response = client.put(reverse('breed_detail', args=["breed1"]), data=data, format="json")
    assert response.status_code == 200

@pytest.mark.django_db(transaction=True)
def test_delete_breeds(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    response = client.delete(reverse('breed_detail', args=["breed1"]))
    assert response.status_code == 204

# Basic CRUD of dogs: create, read, update, delete
@pytest.mark.django_db(transaction=True)
def test_create_dogs(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    data = {"name":"dog2", "age":2, "breed":"breed1", "gender":"fe", "color":"color", "favorite_food":"favorite_food_2", "favorite_toy":"favorite_toy_2"}
    response = client.post(reverse('dog_list'), data=data)
    assert response.status_code == 201

@pytest.mark.django_db(transaction=True)
def test_get_list_dogs(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    response = client.get(reverse('dog_list'))
    assert response.status_code == 200

@pytest.mark.django_db(transaction=True)
def test_get_retrieve_dogs(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer '+ test_token)
    response = client.get(reverse('dog_detail', args=[Dog.objects.get(name="dog1").pk]))
    assert response.status_code == 200

@pytest.mark.django_db(transaction=True)
def test_update_dogs(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_token)
    data = {"name":"dog1_new", "age":2, "breed":"breed1", "gender":"fe", "color":"new_color", "favorite_food":"favorite_food_2", "favorite_toy":"favorite_toy_2"}
    response = client.put(reverse('dog_detail', args=[Dog.objects.get(name="dog1").pk]), data=data, format="json")
    assert response.status_code == 200

@pytest.mark.django_db(transaction=True)
def test_delete_dogs(test_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer '+ test_token)
    response = client.delete(reverse('dog_detail', args=[Dog.objects.get(name="dog1").pk]))
    assert response.status_code == 204
