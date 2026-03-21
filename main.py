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
            services.mark_item()
        case 5:
            services.clear_list()
        case 6:
            services.save()
        case 7:
            services.exit()
        case _:
            input("invalid input, try again!")

def main():
    services = Services()
    while True:
        services.show_list()
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

            choices(menu, services)

        except ValueError:
            input("invalid input, try again!")
            continue


main()