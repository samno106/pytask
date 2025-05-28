
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('search/', views.search_task, name="search"),
    path('create/', views.create_task, name="create-task"),
    path('delete/<int:id>', views.task_delete, name='task-delete'),
]
