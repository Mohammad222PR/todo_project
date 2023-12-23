from time import sleep
from celery import shared_task
from django_celery_results.models import TaskResult

@shared_task
def Task():
    print('Task completed successfully')

@shared_task
def Delete_task():
    task = TaskResult.objects.all()
    task.adelete(all)
    print('successfully deleted')


@shared_task
def clean_up_completed_tasks():
    completed_tasks = TaskResult.objects.filter(status='SUCCESS')
    for task in completed_tasks:
        task.delete()
    print('clean_up_completed_tasks completed')