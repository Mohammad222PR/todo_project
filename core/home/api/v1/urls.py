from rest_framework.routers import DefaultRouter
from . import views

app_name = "api-v1"


router = DefaultRouter()
router.register(r'todo/todo_list', views.TodoApi, basename='todo')

urlpatterns = router.urls
