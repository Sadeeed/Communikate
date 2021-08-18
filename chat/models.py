from django.db import models
from django.conf import settings

class Message(models.Model):
    msgContent = models.TextField(unique=False, blank=False)
    msgTimestamp = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey()

    def __str__(self):
        return self.msgContent

class ChatRoom(models.Model):
    name = models.CharField(max_length=255 ,unique=True, blank=False)
    userCount = models.ManyToManyField(settings.AUTH_USER_MODEL, help_text="Currently connected users")