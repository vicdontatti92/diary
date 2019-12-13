import typing

from tracker import entity
from tracker.models import Task


class DjangoTasks:
    def catalogue(self) -> typing.List[entity.Task]:
        tasks_list = []
        django_task = Task.objects.all()
        for tasks in django_task:
            tasks_list.append(
                entity.Task(
                    tasks.name, tasks.description, tasks.complete, tasks.id,
                ),
            )
        return tasks_list

    def add(self, *, task: entity.Task) -> entity.Task:
        django_task = Task.objects.create(
            name=task.name, description=task.description,
        )

        return entity.Task(
            name=django_task.name, description=django_task.description,
        )

    def complete(self, id_: int) -> None:
        complete_item = Task.objects.get(id=id_)
        complete_item.complete = True
        complete_item.save()

    def uncomplete(self, id_: int) -> None:
        uncomplete_item = Task.objects.get(id=id_)
        uncomplete_item.complete = False
        uncomplete_item.save()

    def delete(self, id_: int) -> None:
        Task.objects.get(id=id_).delete()
