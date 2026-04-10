from dominio.entities.tasks import Task

class AddTask:
    def __init__(self, repository, todo_list):
        self.repository = repository
        self.todo_list = todo_list

    def execute(self, name):
        new_task = Task(name=name)
        self.todo_list.add_item(new_task)
        self.repository.save(self.todo_list)
