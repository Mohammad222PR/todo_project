import pytest
from django.contrib.auth.models import User
from home.api.v1.views import *
from rest_framework.test import APIClient
from django.urls import reverse, resolve


@pytest.mark.django_db
class TestUrl():
    def test_url_todo_list_resolve(self):
        url = reverse('home:api-v1:todo-list')
        assert (resolve(url).func,TodoApi)
        
    def test_url_todo_detail_resolve(self):
        url = reverse('home:api-v1:todo-detail', kwargs={"pk":3})
        assert (resolve(url).func,TodoApi)