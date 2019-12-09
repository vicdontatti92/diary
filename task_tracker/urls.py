from django.contrib import admin
from django.urls import path

from task_tracker.views import add_task, delete_task, tasks_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks_view),
    path('addTask/', add_task),
    path('deleteTask/<int:task_id>/', delete_task),
]
