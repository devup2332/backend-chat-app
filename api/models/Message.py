
from api.models.Chat import Chat
from django.db import models
from .User import User

class Message (models.Model):
    message = models.CharField(max_length=200)
    emitter = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE,null=True,related_name="messages")

    def __str__(self):
        return self.message
