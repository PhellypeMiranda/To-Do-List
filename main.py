import funcs

# this function calls from funcs.py the required action from the user
def choices(choice, items_list):
    match choice:
        case 1:
            funcs.add_item(items_list)
        case 2:
            funcs.mark_as_checked(items_list)
        case 3:
            funcs.change_item(items_list)
        case 4:
            funcs.remove_item(items_list)
        case 5:
            funcs.clear_list(items_list)
        case 6:
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
            count = funcs.count(items_list)
            print(f"\nFinished {count[0]}, unfinished {count[1]}!")
            menu = int(input("\nWhat do you want to do?\n"
                            "1 - Add item to the list\n"
                            "2 - Mark/Unmark item\n"
                            "3 - Change item\n"
                            "4 - Remove item from the list\n"
                            "5 - Clear list\n"
                            "6 - Save and exit\n"
                            "Type a number: "))
            choices(menu, items_list)
        except (ValueError, IndexError):
            input("\nInvalid value, try again!\n ")
main()