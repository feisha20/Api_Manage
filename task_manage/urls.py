from django.urls import path
from task_manage import views

app_name = 'task_manage'
urlpatterns = [
    path('task_list/', views.task_list),
    path('task_manage/', views.tasks),
    path('add_task', views.add_task),
    path('to_task1.html', views.to_task1),
    path('to_task2.html', views.to_task2),
    path('to_task0.html', views.to_task0),
    path('to_task3.html', views.to_task3),
    path('to_task4.html', views.to_task4),
    path('tasksearch/', views.task_search),
]