from django.db import models
from django.conf import settings
from django.db.models.fields.related_descriptors import ReverseManyToOneDescriptor


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    userCount = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True , help_text="Currently connected users")

    def __str__(self):
        return self.name

    def connectUser(self, user):
        isUserAdded = False
        if not user in self.userCount.all():
            self.userCount.add(user)
            self.save()
            isUserAdded = True
        elif user in self.userCount.all():
            isUserAdded = True
        return isUserAdded

    def disconnectUser(self, user):
        isUserRemoved = False
        if user in self.userCount.all():
            self.userCount.remove(user)
            self.save()
            isUserRemoved = True
        return isUserRemoved

    @property
    def groupName(self):
        return f"ChatRoom-{self.id}"

class MessageManager(models.Manager):
    def byRoom(self, room):
        querySet = Message.objects.filter(room=room).order_by("-msgTimestamp")
        return querySet

class Message(models.Model):
    msgContent = models.TextField(unique=False, blank=False)
    msgTimestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    chatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    objects = MessageManager()

    def __str__(self):
        return self.msgContent
