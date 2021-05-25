from api.models.Message import MessageModel
from django.db import models
from api.models.UserChat import UserChat

class ChatModel(models.Model):
    user_1 = models.ForeignKey(UserChat,on_delete=models.CASCADE,related_name="user_1")
    user_2 = models.ForeignKey(UserChat,on_delete=models.CASCADE,related_name="user_2")
    last_message = models.ForeignKey(MessageModel,on_delete=models.CASCADE,related_name="last_message")
    messages = models.ManyToManyField(MessageModel)

    def __str__(self):

        return self.last_message.message