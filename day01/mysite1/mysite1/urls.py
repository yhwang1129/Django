"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/page/2003/
    path('page/2003/', views.page_2003_views),# xxx_view 视图函数用于接收游览器请求def xxx_view(request[,其他参数]):   return HeetResponse
    #http://127.0.0.1:8000/
    path('', views.index_view),
    path('page/1', views.page1_view),
    path('page/2', views.page2_view),
    #http://127.0.0.1:8000/3-100
    path('page/<int:pg>', views.pagen_view),# path转换器有str int 常用
    # re_path()可以使用正则表达式进行精确匹配
    # http://127.0.0.1:8000/整数(1到2 位)/操作字符串[add/sub/mul]/整数
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal_view),
    # http://127.0.0.1:8000/整数/操作字符串[add/sub/mul]/整数
    path('<int:num1>/<str:op>/<int:num2>', views.simple_math),
    # http://127.0.0.1.8000/年四位/月两位/日两位
    re_path(r'^birthday/(?P<x>\d{4})/(?P<y>\d{1,2})/(?P<z>\d{1,2})$', views.birthday_view)
]
