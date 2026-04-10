class RemoveTask:
    def __init__(self, repository, todo_list):
        self.repository = repository
        self.todo_list = todo_list

    def execute(self, index):
        self.todo_list.remove_item(index)
        self.repository.save(self.todo_list)
