from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'receiver', 'type', 'status', 'timestamp')
    list_filter = ('type', 'status')
    search_fields = ('message',)

