from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            return Notification.objects.filter(receiver_id=user).order_by('-timestamp')
        return Notification.objects.none()

