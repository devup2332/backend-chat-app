
from api.models.Avatar import Avatar
from django.db import models
from django.contrib.auth.hashers import make_password

class UserManager (models.Manager):

    def hash_pass(self,password):
        hashed = make_password(password=password)
        return hashed
    def register(self,data):
        email = data['email']
        password = data['password']
        phone = data['phone']
        first_name = data['first_name']
        last_name = data['last_name']
        
        user:User = self.model()
        user.password = self.hash_pass(password=password)
        user.email = email
        user.phone = phone
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
        return user
    

class User(models.Model):
    
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=200,default="")
    avatar = models.ForeignKey(Avatar,on_delete=models.CASCADE,null=True,related_name="avatar")
    objects = UserManager()
   
    def __str__(self):
        return self.email
