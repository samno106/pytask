
from django.urls import path

from . import views


urlpatterns = [
    path('admin/login/', views.login, name="login"),
    path('', views.index),
    path('search/', views.search_task, name="search"),
    path('create/', views.create_task, name="create-task"),
    path('delete/<int:id>/', views.task_delete, name='task-delete'),
    path('update-status/<int:id>/', views.task_update_status, name='task-update-status'),
    path('edit/<int:id>/', views.task_edit, name='task-edit'),
    path('update/<int:id>/', views.task_update, name='task-update'),
    
]
