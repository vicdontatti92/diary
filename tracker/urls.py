from django.urls import path

from tracker.views import (
    task_add,
    task_complete,
    task_delete,
    task_uncomplete,
    tasks_catalogue,
)

urlpatterns = [
    path('', tasks_catalogue, name='tracker_root'),
    path('add/', task_add, name='tracker_task_add'),
    path('delete/<int:id_>/', task_delete, name='tracker_task_delete'),
    path('complete/<int:id_>/', task_complete, name='tracker_task_complete'),
    path(
        'uncomplete/<int:id_>/',
        task_uncomplete,
        name='tracker_task_uncomplete',
    ),
]
