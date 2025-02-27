"""mysite3 URL Configuration

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
from django.urls import path, include
from . import views# .代表当前目录

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_static', views.test_static),
    # http://127.0.0.1:8000/music/index
    path('music/', include('music.urls')),#主路由利用incldue可以转到子路由也就是app
    path('news/', include('news.urls')),
    path('sport/', include('sport.urls')),
    path('bookstore/', include('bookstore.urls'))
]
