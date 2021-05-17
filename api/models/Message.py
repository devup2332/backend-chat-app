from django.db import models
from .UserChat import UserChat

class MessageModel (models.Model):
    message = models.CharField(max_length=200)
    user = models.ForeignKey(UserChat, related_name="user", on_delete=models.CASCADE)

    def __str__(self):
        return self.message
