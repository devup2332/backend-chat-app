from api.models.Chat import ChatModel
from django.contrib import admin
from api.models.UserChat import UserChat
from api.models.Message import MessageModel

# Register your models here.
admin.site.register(UserChat)
admin.site.register(ChatModel)
admin.site.register(MessageModel)