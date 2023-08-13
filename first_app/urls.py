from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('assign_new_task/', views.assign_tasks, name="assign_tasks"),
    path('show_tasks/', views.show_tasks, name="show_tasks"),
    path('delete_task/<int:id>', views.delete_task, name="delete_task"),
    path('edit_task/<int:id>', views.edit_task, name="edit_task"),
    path('complete_task/<int:id>', views.complete_task, name='complete_task'),
    path('completed_tasks', views.completed_tasks, name='completed_tasks')

]
