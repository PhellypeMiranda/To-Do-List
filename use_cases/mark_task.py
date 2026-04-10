class MarkTask:
    def __init__(self, repository, todo_list):
        self.repository = repository
        self.todo_list = todo_list

    def execute(self, index):
        self.todo_list[index].toggle()
        self.repository.save(self.todo_list)
