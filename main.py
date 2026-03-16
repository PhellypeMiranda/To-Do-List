import funcs

# this function calls from funcs.py the required action from the user
def choices(choice, items_list):
    match choice:
        case 1:
            funcs.add_item(items_list)
        case 2:
            funcs.remove_item(items_list)
        case 3:
            funcs.clear_list(items_list)
        case 4:
            funcs.save_and_exit(items_list)
        case _:
            input("Invalid option, please try again!")

# This is the main function, it works has a main menu of the program
# where the user see the list and decide what to do.
def main():
    items_list = funcs.get_list()
    while True:
        try:
            funcs.show_list(items_list)
            menu = int(input("\nWhat do you want to do?\n"
                            "1 - Add item to the list\n"
                            "2 - Remove item from the list\n"
                            "3 - Clear list\n"
                            "4 - Save and exit\n"
                            "Type a number: "))
            choices(menu, items_list)
        except (ValueError, IndexError):
            input("\nInvalid value, try again!\n ")
main()