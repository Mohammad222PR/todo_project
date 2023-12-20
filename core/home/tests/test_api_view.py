import pytest
from ..models import Todo
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def commend_user():
    user = User.objects.create_user(
        username="mmddwdd",
        email="mmd@example.com",
        password="wdqasfqawfa",
        first_name="John",
        last_name="rafael",
        is_staff = False,
        is_active = True
    )
    return user


@pytest.mark.django_db
class TestTodoApi:
    def test_get_todo_response_200(self, api_client):
        url = reverse("home:api-v1:todo-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_todo_obj_response_201(self, api_client, commend_user):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "complete": True,
            "created_data": datetime.now(),
        }
        user = commend_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_response_403(self, api_client, commend_user):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "complete": True,
            "created_data": datetime.now(),
        }
        api_client.force_login(user={})
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_user_response_401(self, api_client):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "complete": True,
            "created_data": datetime.now(),
            "updated_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_response_400(self, api_client, commend_user):
        url = reverse("home:api-v1:todo-list")
        data = {}
        user = commend_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
