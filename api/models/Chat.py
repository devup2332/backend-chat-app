from api.models.User import User
from django.db import models

class Chat(models.Model):
    user_1 = models.ForeignKey(User,related_name="user_1",on_delete=models.CASCADE,null=True)
    user_2 = models.ForeignKey(User,related_name="user_2",on_delete=models.CASCADE,null=True)
    last_message = models.CharField(max_length=300,default="")
    def __str__(self):

        return self.last_message 