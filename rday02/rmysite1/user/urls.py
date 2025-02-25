from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:user_id>', views.user_detail),
    path('update', views.user_update)
]