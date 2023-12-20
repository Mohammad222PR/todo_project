from typing import Any
from django.core.management.base import BaseCommand
from faker import Faker
from home.models import Todo
from django.contrib.auth.models import User
from datetime import datetime
import random

class Command(BaseCommand):
    help = "inserting data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args: Any, **options: Any):
        user = User.objects.create_user(
            username=self.fake.name(),
            email=self.fake.email(),
            password="w@12312331",
            first_name=self.fake.last_name(),
            last_name=self.fake.last_name(),
        )

        for _ in range(5):
            Todo.objects.create(
                user = user,
                title = self.fake.paragraph(nb_sentences=1),
                complete = random.choice([True, False]),
                created_date = datetime.now(),
                updated_date = datetime.now(),
            )
