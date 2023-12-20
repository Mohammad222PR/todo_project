import pytest
from django.contrib.auth.models import User
from ..models import *
from datetime import datetime
from rest_framework.test import APIClient


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="amin",
        email="mmd@example.com",
        password="wdqasfqawfa",
       
    )
    return user

@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
class TestModel():
    def test_model_create_response_200(self, user):
        todo = Todo.objects.create(
            user = user,
            title = 'test',
            complete = True,
            created_date = datetime.now(),
            updated_date = datetime.now(),
        )
        
        assert Todo.objects.filter(id=todo.id).exists()

   
