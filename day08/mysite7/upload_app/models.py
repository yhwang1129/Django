from django.db import models

# Create your models here.
class Content(models.Model):

    title = models.CharField('文章名字', max_length=11)
    picture = models.FileField(upload_to='picture')

