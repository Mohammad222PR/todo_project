from celery import shared_task
from django_celery_beat.models import PeriodicTask
from home.models import Todo
from faker import Faker
from datetime import datetime
from django.contrib.auth.models import User


@shared_task
def Task():
    print("Task completed successfully")


@shared_task
def create_todo():
    fake = Faker()
    Todo.objects.create(
        user=User.objects.get(id=1),
        title=fake.paragraph(nb_sentences=1),
        complete=True,
        created_date=datetime.now(),
        updated_date=datetime.now(),
    )
    print("todo create")


@shared_task
def clean_up_completed_tasks():
    tasks = PeriodicTask.objects.filter(enabled=False)
    for task in tasks:
        task.delete()
    print("clean_up_completed_tasks completed")
