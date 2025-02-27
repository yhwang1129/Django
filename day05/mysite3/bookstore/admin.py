from django.contrib import admin
from .models import Book, Author
# Register your models here.
# 将book和author放到admin后台方便查看

class BookManager(admin.ModelAdmin):
    #列表页显示那些字段的列
    list_display = ('id', 'title', 'pub', 'price')
    #控制list_display中的字段，哪些可以链接到修改页
    list_display_links = ['title']
    #过滤器的添加
    list_filter = ['pub']
    #添加搜索框[模糊查询]
    search_fields = ['title']
    #添加可在列表页编辑的字段,这个字段与links的字段互斥
    list_editable = ['price']

class AuthorManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email')
    list_editable = ['age']
    list_display_links = ['name']

admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)