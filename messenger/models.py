from io import BytesIO

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    first_message_id = models.IntegerField(default=0)

    def str(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:
            from messenger.utils import generate_user_thumbnail
            thumbnail = generate_user_thumbnail(self.username[0])

            thumbnail_io = BytesIO()
            thumbnail.save(thumbnail_io, format='PNG')
            thumbnail_io.seek(0)

            self.image.save(f'{self.username}_thumbnail.png', ContentFile(thumbnail_io.read()), save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        unique_together = ('email',)


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
