from datetime import date, timedelta


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.finished = False


task = Task('bake birthday cake', date(2023, 10, 1))
print(task.due_date)
task.finished = True
print(task.finished)


class TaskList:
    def __init__(self):
        self.task_list = []

    def __len__(self):
        return len(self.task_list)

    def add_task(self, task):
        self.task_list.append(task)
        if task.due_date < date.today():
            raise ValueError('Task due_date must be in the future')

    @property
    def finished_tasks(self):
        finished_tasks = []
        for task in self.task_list:
            if task.finished:
                finished_tasks.append(task)
        return finished_tasks

    @property
    def due_tasks(self):
        unfinished_tasks = []
        for task in self.task_list:
            if task.finished is False:
                unfinished_tasks.append(task)

        return unfinished_tasks

    @property
    def overdue_tasks(self):
        overdue_tasks = []
        for task in self.due_tasks:
            if task.due_date < date.today() and not task.finished:
                overdue_tasks.append(task)
        return overdue_tasks


tasks = TaskList()
print(len(tasks))

from datetime import date, timedelta

tomorrow = date.today() + timedelta(days=1)
yesterday = date.today() - timedelta(days=1)

task_in_future = Task('some description', tomorrow)

print(tasks.add_task(task_in_future))
print(len(tasks))
print(tasks.overdue_tasks)