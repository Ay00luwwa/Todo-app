from django.urls import path
from views import index, add_list, add_task, complete_task

urlpatterns = [
    path('', views.index, name='index'),
    path('add_list/', views.add_list, name='add_list'),
    path('<int:list_id>/add_task/', views.add_task, name='add_task'),
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
]
