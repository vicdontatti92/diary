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
    DjangoTasks().add(task=et)
    return HttpResponseRedirect(reverse('tracker_root'))  # noqa: WPS226


def task_delete(request: WSGIRequest, id_: int) -> HttpResponseRedirect:
    DjangoTasks().delete(id)
    return HttpResponseRedirect(reverse('tracker_root'))  # noqa: WPS226


def task_complete(request: WSGIRequest, id_: int) -> HttpResponseRedirect:
    DjangoTasks().complete(id)
    return HttpResponseRedirect(reverse('tracker_root'))  # noqa: WPS226


def task_uncomplete(request: WSGIRequest, id_: int) -> HttpResponseRedirect:
    DjangoTasks().uncomplete(id)
    return HttpResponseRedirect(reverse('tracker_root'))  # noqa: WPS226
