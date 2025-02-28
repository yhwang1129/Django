from . import views
from django.urls import path

urlpatterns = [

    path('add', views.add_note),
    path('all', views.list_view),
    path('update/<int:note_id>', views.update_view),
    path('delete', views.delete_view)

]