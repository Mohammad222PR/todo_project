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
        username="amin",
        email="mmd@example.com",
        password="wdqasfqawfa",
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
            "created_date": datetime.now(),
        }

        user = commend_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_todo_obj_no_aut_response_401(self, api_client):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "complete": True,
            "created_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_auth_response_403(self, api_client):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "complete": True,
            "created_date": datetime.now(),
        }
        api_client.force_login(user={})
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_data_title_response_400(
        self, api_client, commend_user
    ):
        url = reverse("home:api-v1:todo-list")
        data = {
            "tite": "",
            "complete": True,
            "created_date": datetime.now(),
        }
        user = commend_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_create_todo_obj_invalid_data_title_no_auth_response_403(
        self, api_client, commend_user
    ):
        url = reverse("home:api-v1:todo-list")
        data = {
            "tite": "",
            "complete": True,
            "created_date": datetime.now(),
        }

        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_data_title_no_auth_response_403(
        self, api_client, commend_user
    ):
        url = reverse("home:api-v1:todo-list")
        data = {
            "tite": "",
            "complete": True,
            "created_date": datetime.now(),
        }
        api_client.force_login(user={})
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_data_complete_no_auth_response_403(
        self, api_client
    ):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "codmplete": True,
            "created_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_data_complete_none_auth_response_403(
        self, api_client, commend_user
    ):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "codmplete": True,
            "created_date": datetime.now(),
        }
        api_client.force_login(user={})
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_invalid_data_complete_response_403(
        self, api_client, commend_user
    ):
        url = reverse("home:api-v1:todo-list")
        data = {
            "title": "hi",
            "codmplete": True,
            "created_date": datetime.now(),
        }
        user = commend_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 403

    
    def test_create_todo_obj_no_data_response_400(self, api_client):
        url = reverse("home:api-v1:todo-list")
        data = {}
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_no_data_response_400(self, api_client):
        url = reverse("home:api-v1:todo-list")
        data = {}
        user = commend_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_todo_obj_no_data_response_400(self, api_client):
        url = reverse("home:api-v1:todo-list")
        data = {}
        api_client.force_login(user={})
        response = api_client.post(url, data)
        assert response.status_code == 403
