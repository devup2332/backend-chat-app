from api.models.Chat import Chat
from django.contrib import admin
from api.models.User import User
from api.models.Message import Message

# Register your models here.
admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Message)