from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_message_id = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Message(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            'new-message',
            {
                'type': 'new_message',
                'message': {
                    'username': self.user.username,
                    'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'text': self.text
                }
            }
        )
