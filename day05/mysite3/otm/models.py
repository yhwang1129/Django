from django.db import models

# Create your models here.
class Publisher(models.Model):
    #出版社 【一】
    name = models.CharField('出版社名称', max_length=50)

class Book(models.Model):
    #书名 【多】
    title = models.CharField('书名', max_length=11)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)