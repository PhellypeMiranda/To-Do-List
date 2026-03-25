class ToDoList:
    def __init__(self):
        self.tasks = []

    def __str__(self):
        return str(self.tasks)

    def __iter__(self):
        return iter(self.tasks)

    def __repr__(self):
        return str(self.tasks)

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, index):
        return self.tasks[index]

    def __setitem__(self, index, value):
        self.tasks[index] = value

    def add_item(self, task):
        self.tasks.append(task)

    def remove_item(self, index):
        del self.tasks[index]

    def insert_item(self, value, task):
        self.tasks.insert(value, task)

    def change_item(self, index, task):
        self.tasks[index].name = task

    def clear(self):
        self.tasks.clear()