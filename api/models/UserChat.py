from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.db import models

class UserChatManager (BaseUserManager):

    def create_user(self,email,last_name,first_name,phone,password=None):

        if not email:
            raise ValueError("Email is needed")
        email = self.normalize_email(email)
        user = self.model(email = email)
        user.last_name = last_name
        user.first_name = first_name
        user.phone = phone
        user.set_password(password)

        user.save(using=self._db)
        return user
        
    def create_superuser(self,email,last_name,first_name,phone,password=None):
        user = self.create_user(email=email,password=password,last_name=last_name,first_name=first_name,phone=phone)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserChat(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField( unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_name = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name','first_name','phone']
    objects = UserChatManager()

    def __str__(self):
        return self.email
