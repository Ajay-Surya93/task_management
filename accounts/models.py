from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

ROLE_CHOICES = [
    ('admin','Admin'),
    ('teamleader','TeamLeader'),
    ('employee','Employee'),
]

def save(self, *args, **kwargs):
    if self.is_superuser:
        self.role = 'admin'
    super().save(*args, **kwargs)


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)

    def is_admin(self):
        return self.role == 'admin' or self.is_superuser
    def is_teamleader(self):
        return self.role == 'teamleader'
    def is_employee(self):
        return self.role == 'employee'

class Team(models.Model):
    name = models.CharField(max_length=120)
    tech_stack = models.CharField(max_length=120, blank=True)
    leader = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='leading_teams')

    def __str__(self):
        return f"{self.name} - {self.tech_stack}"

class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_memberships')
    joined_at = models.DateTimeField(auto_now_add=True)

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    points = models.IntegerField(default=0)
    notify_status = models.CharField(max_length=20, default='On Time')  # On Time / Overdue
    tasks_completed = models.IntegerField(default=0)
    last_updated_task = models.DateTimeField(null=True, blank=True)

class TeamLeaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tl_profile')
    managed_teams = models.ManyToManyField(Team, blank=True, related_name='managed_by')

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
