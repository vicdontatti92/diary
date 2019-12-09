from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from task_tracker.models import TaskItem


def tasks_view(request: WSGIRequest) -> HttpResponse:
    all_task_items = TaskItem.objects.all()
    return render(request, 'index.html', {'all_items': all_task_items})


def add_task(request: WSGIRequest) -> HttpResponseRedirect:
    new_item = TaskItem(
        task_name=request.POST['task_name'],
        task_discription=request.POST['task_discription'],
    )
    new_item.save()
    return HttpResponseRedirect('/')


def delete_task(request: WSGIRequest, task_id: int) -> HttpResponseRedirect:
    item_to_delete = TaskItem.objects.get(id=task_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
