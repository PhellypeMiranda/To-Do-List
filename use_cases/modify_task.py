class ModifyTask:
    def __init__(self, repository, todo_list):
        self.repository = repository
        self.todo_list = todo_list

    def execute(self, index, name, ):
        self.todo_list.change_item(index, name)
        self.repository.save(self.todo_list)
