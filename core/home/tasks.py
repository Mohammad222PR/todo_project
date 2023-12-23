from time import sleep
from celery import shared_task
from django_celery_results.models import TaskResult


@shared_task()
def Task():
    sleep(3)
    print('x')

# tasks.py

@shared_task
def clean_up_completed_tasks():
    completed_tasks = TaskResult.objects.filter(enabled=False)

    for task in completed_tasks:
        task.delete()

    print("Cleaned up completed tasks.")
