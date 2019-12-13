from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from tracker.repositories import DjangoTasks, entity


def tasks_catalogue(request: WSGIRequest) -> HttpResponse:
    all_tasks = DjangoTasks().catalogue()
    return render(request, 'tracker/tracker.html', {'all_items': all_tasks})


def task_add(request: WSGIRequest) -> HttpResponseRedirect:
    et = entity.Task(
        name=request.POST['name'], description=request.POST['description'],
    )
    print(et)
    DjangoTasks().add(task=et)
    return HttpResponseRedirect(reverse('tracker_root'))


def task_delete(request: WSGIRequest, id: int) -> HttpResponseRedirect:
    DjangoTasks().delete(id)
    return HttpResponseRedirect(reverse('tracker_root'))


def task_complete(request: WSGIRequest, id: int) -> HttpResponseRedirect:
    DjangoTasks().complete(id)
    return HttpResponseRedirect(reverse('tracker_root'))


def task_uncomplete(request: WSGIRequest, id: int) -> HttpResponseRedirect:
    DjangoTasks().uncomplete(id)
    return HttpResponseRedirect(reverse('tracker_root'))
