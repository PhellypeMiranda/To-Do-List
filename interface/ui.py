from tkinter import messagebox
from tkinter import *

class TodoUI:
    def __init__(self, todo_list, add_task, remove_task, modify_task, mark_task, clear_list):
        self.todo_list = todo_list
        self.case_add_task = add_task
        self.case_remove_task = remove_task
        self.case_modify_task = modify_task
        self.case_clear_list = clear_list
        self.case_mark_task = mark_task

        # window config
        self.window = Tk()
        self.window.geometry('600x600')
        self.window.resizable(False, False)
        self.window.title('To Do List')
        self.icon = PhotoImage(file="src/img/list_icon.png")
        self.window.iconphoto(True, self.icon)

        # Body
        self.body = Frame(self.window)
        self.body.pack(fill="both", expand=True)

        # Header
        self.header = Frame(self.body, height=60)
        self.header.pack(fill="x")

        # title
        self.title = Label(self.header, text="To Do List")
        self.title.config(font=("Arial", 40, "italic"))
        self.title.pack(expand=True)

        # Left (MENU)
        self.left = Frame(self.body, width=200)
        self.left.configure(relief="solid", bd=1, pady=25, )
        self.left.pack(side="left", fill="y")
        self.left.pack_propagate(False)
        self.icon = PhotoImage(file="src/img/list_icon.png")
        self.img = Label(self.left, image=self.icon)
        self.img.pack()

        # Frame of the buttons
        self.buttons_frame = Frame(self.left)
        self.buttons_frame.pack(side="bottom")

        # Entries
        self.add_entry = Entry(self.buttons_frame, width=0, justify="center")
        self.add_entry.pack(fill="x", padx=10, pady=5)

        # Menu Buttons
        self.add_button = Button(self.buttons_frame, width=15, text="Add task")
        self.add_button.config(command=self.add_task)
        self.add_button.pack(fill="x", padx=10, pady=5)

        self.remove_button = Button(self.buttons_frame, width=15, text="Remove task")
        self.remove_button.config(command=self.remove_task)
        self.remove_button.pack(fill="x", padx=10, pady=5)

        self.modify_button = Button(self.buttons_frame, width=15, text="Modify task name")
        self.modify_button.config(command=self.modify_task)
        self.modify_button.pack(fill="x", padx=10, pady=5)

        self.mark_button = Button(self.buttons_frame, width=15, text="Mark task")
        self.mark_button.config(command=self.mark_task)
        self.mark_button.pack(fill="x", padx=10, pady=5)

        self.clear_button = Button(self.buttons_frame, width=15, text="Clear list")
        self.clear_button.config(command=self.clear_tasks)
        self.clear_button.pack(fill="x", padx=10, pady=5)

        self.exit_button = Button(self.buttons_frame, width=15, text="Exit")
        self.exit_button.config(command=self.exit)
        self.exit_button.pack(fill="x", padx=10, pady=5)

        # right (LIST)
        self.right = Frame(self.body, width=400)
        self.right.configure(relief="solid",
                         bd=1)
        self.right.pack(side="right", fill="y")
        self.right.pack_propagate(False)

        self.listbox = Listbox(self.right)
        self.listbox.config(font=("Courier", 16))
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.show_list()

    def run(self):
        self.window.mainloop()

    def show_list(self):
        if not self.todo_list:
            print(f"{"The list is empty!:^35"}")
        else:
            count = 1
            for item in self.todo_list:
                if item.checked:
                    self.listbox.insert(END, f"{count:>2} - [x] {item}")
                else:
                    self.listbox.insert(END, f"{count:>2} - [ ] {item}")
                count += 1

    def add_task(self):
        name = self.add_entry.get()
        if name:
            self.case_add_task.execute(name)
            self.update_list()
            self.add_entry.delete(0, END)

    def remove_task(self):
        selected = self.listbox.curselection()

        if selected:
            confirm = self.confirm_operation("delete")
            if confirm:
                index = selected[0]
                self.case_remove_task.execute(index)
                self.update_list()

    def modify_task(self):
        selected = self.listbox.curselection()
        name = self.add_entry.get()

        if selected and name:
            confirm = self.confirm_operation("modify")
            if confirm:
                index = selected[0]
                self.case_modify_task.execute(index, name)
                self.update_list()
                self.add_entry.delete(0, END)

    def mark_task(self):
        selected = self.listbox.curselection()

        if selected:
            index = selected[0]
            self.case_mark_task.execute(index)
            self.update_list()

    def clear_tasks(self):
        if self.todo_list:
            confirm = self.confirm_operation("clear list")
            if confirm:
                self.case_clear_list.execute()
                self.update_list()

    def exit(self):
        confirm = self.confirm_operation("exit")
        if confirm:
            self.window.destroy()

    def update_list(self):
        self.listbox.delete(0, END)  # limpa tudo
        self.show_list()

    @staticmethod
    def confirm_operation(operation):
        confirm = messagebox.askyesno(
            f"Confirm {operation}",
            f"Are you sure you want to {operation}?"
        )
        if confirm:
            return True
        else:
            return False