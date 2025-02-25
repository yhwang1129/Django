from random import random

from django.db import models
import random

def default_sign():

    signs = ['这个人很神秘，什么都没写。。。', '神秘人']
    return random.choice(signs)


# Create your models here.
class UserProfile(models.Model):

    username = models.CharField(max_length=11, verbose_name='用户名', primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    password = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='avatar', null=True)
    sign = models.CharField(max_length=50, verbose_name='个人签名', default=default_sign)
    info = models.CharField(max_length=150, verbose_name='个人简介', default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'user_user_profile'