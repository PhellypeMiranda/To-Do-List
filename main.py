from services.todo_services import Services

def choices(menu, services):

    match menu:
        case 1:
            services.add_item()
        case 2:
            services.remove_item()
        case 3:
            services.modify_item()
        case 4:
            services.reorder_item()
        case 5:
            services.mark_item()
        case 6:
            services.clear_list()
        case 7:
            services.exit_program()
        case _:
            input("invalid input, try again!")

def main():
    services = Services()
    services.load_on_menu()
    while True:
        services.show_list()
        try:
            menu = int(input("\nMenu:\n"
                             "1 - Add an item to the list.\n"
                             "2 - Remove an item from the list.\n"
                             "3 - Modify an item from the list.\n"
                             "4 - Reorder an item from the list.\n"
                             "5 - Mark/Unmark the item as checked.\n"
                             "6 - Clear to do list.\n"
                             "7 - Exit.\n"
                             "Select an option: "))

            choices(menu, services)

        except ValueError:
            input("invalid input, try again!")
            continue

main()