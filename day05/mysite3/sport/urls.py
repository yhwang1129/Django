from django.urls import path
from . import views# .代表当前目录

urlpatterns = [
    # http://127.0.0.1:8000/music/index
    path('index', views.index_view)
]