from django.db import models
from django.conf import settings

class Notification(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='sent_notifications')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='received_notifications')
    message = models.TextField()
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Unread')
    timestamp = models.DateTimeField(auto_now_add=True)
