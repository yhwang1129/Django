from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField('书名', max_length=50, default='', unique=True)
    pub = models.CharField('出版社', max_length=100, default='')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('售价', max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField('是否活跃（伪删除）', default=True)

    def __str__(self):
        return '%s_%s_%s_%s'%(self.title, self.pub, self.price, self.market_price)

    class Meta:
        db_table = 'book'#改数据库表名
        verbose_name = '图书'#改后台admin名字
        verbose_name_plural = verbose_name

class Author(models.Model):

    name = models.CharField('姓名', max_length=11, default='')
    age = models.IntegerField('年龄', default='1')
    email = models.EmailField('邮箱', null=True)

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name