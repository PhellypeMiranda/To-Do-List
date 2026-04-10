from infrastructure.repositories.repository_json import RepositoryJson
from interface.ui import TodoUI
from use_cases.add_task import AddTask
from use_cases.remove_task import RemoveTask
from use_cases.modify_task import ModifyTask
from use_cases.mark_task import MarkTask
from use_cases.clear_list import ClearList


def main():
    repository = RepositoryJson()
    todo_list = repository.load()

    add_task = AddTask(todo_list=todo_list, repository=repository)
    remove_task = RemoveTask(todo_list=todo_list, repository=repository)
    modify_task = ModifyTask(todo_list=todo_list, repository=repository)
    mark_task = MarkTask(todo_list=todo_list, repository=repository)
    clear_list = ClearList(todo_list=todo_list, repository=repository)

    app = TodoUI(todo_list, add_task, remove_task, modify_task, mark_task, clear_list)
    app.run()

if __name__ == "__main__":
    main()