from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, EmployeeProfile, TeamLeaderProfile

# Auto-create profiles when a user is created
@receiver(post_save, sender=User)
def create_user_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'employee':
            EmployeeProfile.objects.create(user=instance)
        elif instance.role == 'teamleader':
            TeamLeaderProfile.objects.create(user=instance)
