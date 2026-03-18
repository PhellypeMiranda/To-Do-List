from todo_list import ToDoList
import services
from storage import Storage

def choices(menu, items_list):
    match menu:
        case 1:
            services.add_item(items_list)
        case 2:
            services.remove_item(items_list)
        case 3:
            services.modify_item(items_list)
        case 4:
            services.mark_item(items_list)
        case 5:
            services.clear_list(items_list)
        case 6:
            services.save(items_list)
        case 7:
            services.exit(items_list)
        case _:
            input("invalid input, try again!")

def main():
    items_list = services.load_list()
    while True:
        services.show_list(items_list)
        try:
            menu = int(input("\nMenu:\n"
                             "1 - Add an item to the list.\n"
                             "2 - Remove an item from the list.\n"
                             "3 - Modify an item from the list.\n"
                             "4 - Mark/Unmark the item as checked.\n"
                             "5 - Clear to do list.\n"
                             "6 - Save list.\n"
                             "7 - Exit.\n"
                             "Select an option: "))

            choices(menu, items_list)

        except ValueError:
            input("invalid input, try again!")
            continue


main()