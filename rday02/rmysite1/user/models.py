from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField('用户姓名', max_length=11)
    desc = models.CharField('个人描述', max_length=120)