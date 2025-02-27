from . import views
from django.urls import path

urlpatterns = [
    path('all_book', views.all_books)
]