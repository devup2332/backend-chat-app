from api.models.UserChat import UserChat
from django.db import models

class Avatar(models.Model):

    public_id = models.CharField(max_length=200,null=True)
    url = models.CharField(max_length=300,default="https://res.cloudinary.com/dder8kjda/image/upload/v1617211129/user-icon_x13zob.png")
    user = models.ForeignKey(UserChat,on_delete=models.CASCADE)

    def __str__(self):
        return self.user