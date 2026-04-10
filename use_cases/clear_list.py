class ClearList:
    def __init__(self, repository, todo_list):
        self.repository = repository
        self.todo_list = todo_list

    def execute(self):
        self.todo_list.clear()
        self.repository.save(self.todo_list)