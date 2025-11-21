from django.core.management.base import BaseCommand
from accounts.models import EmployeeProfile
from notifications.models import Notification
from datetime import datetime
import requests

class Command(BaseCommand):
    help = "Check overdue tasks by calling Task microservice or local DB"

    def handle(self, *args, **kwargs):
        """
        You should connect this to your Task Microservice API.
        Here we assume the API endpoint returns:
        [
          {
            "task_id": 1,
            "assigned_to": employee_id,
            "due_date": "2025-01-12",
            "status": "In Progress"
          }
        ]
        """
        try:
            response = requests.get("http://localhost:8001/api/tasks/")  # task service URL
            tasks = response.json()
        except:
            self.stdout.write("Task service unreachable")
            return

        today = datetime.now().date()

        for task in tasks:
            due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
            if task["status"] != "Completed" and due_date < today:
                emp_id = task["assigned_to"]
                try:
                    profile = EmployeeProfile.objects.get(user_id=emp_id)
                except EmployeeProfile.DoesNotExist:
                    continue

                # Update performance & notify status
                profile.points -= 5
                profile.notify_status = "Overdue"
                profile.save()

                # create notification
                Notification.objects.create(
                    sender=None,
                    receiver_id=emp_id,
                    message=f"Task {task['task_id']} is overdue!",
                    type="Overdue"
                )

        self.stdout.write("Overdue check completed.")
