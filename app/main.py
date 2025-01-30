import customtkinter as ctk
import settings

root = ctk.CTk()

root.title(settings.APPLICATION_TITLE)

root.geometry(f"{settings.APPLICATION_WIDTH}x{settings.APPLICATION_HEIGHT}")

root.resizable(False,False) if settings.APPLICATION_RESIZABLE == False else root.resizable(True, True)

def add_todo(todo: str, fg_color: str):
    def complete_todo():
        todo_frame.destroy()

    def change_todo_size(button):
        button_fg_color = button.cget("fg_color")

        if button_fg_color == settings.TODO_SMALL_COLOR:
            button.configure(fg_color=settings.TODO_MEDIUM_COLOR)
            button.configure(hover_color=settings.TODO_MEDIUM_COLOR)
        elif button_fg_color == settings.TODO_MEDIUM_COLOR:
            button.configure(fg_color=settings.TODO_LARGE_COLOR)
            button.configure(hover_color=settings.TODO_LARGE_COLOR)
        elif button_fg_color == settings.TODO_LARGE_COLOR:
            button.configure(fg_color=settings.TODO_SMALL_COLOR)
            button.configure(hover_color=settings.TODO_SMALL_COLOR)


    todo_frame = ctk.CTkFrame(root)
    todo_frame.pack(pady=7)

    todo_entry = ctk.CTkEntry(todo_frame, width=200)
    todo_entry.insert(0, todo)
    todo_entry.grid(column=1, row=0)

    todo_complete_btn = ctk.CTkButton(todo_frame, 25,25, text="✔", command=complete_todo)
    todo_complete_btn.grid(column=3, row=0, padx=(5,0))

    todo_size_btn = ctk.CTkButton(todo_frame, 25,25, fg_color=fg_color, hover_color=fg_color,text="", command=lambda:change_todo_size(todo_size_btn))
    todo_size_btn.grid(column=0, row=0, padx=(0,5))


def load_saved_todos():
    with open("todos.txt", "r") as file:
        todos = [line.strip() for line in file.readlines()]
        todos_size = load_saved_todos_size()

        for todo_index in range(len(todos)):
            add_todo(todos[todo_index], todos_size[todo_index])


def save_todos():
    todos_list = []

    # get todos
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkFrame):
            for nested_widget in widget.winfo_children():
                if isinstance(nested_widget, ctk.CTkEntry):
                    todos_list.append(nested_widget.get())


    # write todos to file
    with open("todos.txt", "w") as file:
        for todo in todos_list:
            file.write(todo + "\n")


def load_saved_todos_size():
    with open("todos_size.txt", "r") as file:
        todos_size = [line.strip() for line in file.readlines()]

    return todos_size


def save_todos_size():
    all_buttons_list = []

    # get todos_size
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkFrame):
            for nested_widget in widget.winfo_children():
                if isinstance(nested_widget, ctk.CTkButton):
                    all_buttons_list.append(nested_widget.cget("fg_color"))

    all_buttons_list.pop(0) # first entry is the add todo button

    todos_size_list = []
    for button_index in range(len(all_buttons_list)):
        if button_index % 2 != 0: # every second button in the 'all button list' is the button we want
            todos_size_list.append(all_buttons_list[button_index])

    # write colors to file    
    with open("todos_size.txt", "w") as file:
        for todos_size in todos_size_list:
            file.write(todos_size + "\n")

def add_todo_on_enter(event):
    if event.keysym == "Return":
        add_todo("", settings.TODO_SMALL_COLOR)


def close_application_and_save():
    save_todos()
    save_todos_size()
    root.destroy()


main_btns_frame = ctk.CTkFrame(root)
main_btns_frame.pack(pady=5)

if settings.APPLICATION_LANGUAGE == "EN":
    add_todo_btn = ctk.CTkButton(main_btns_frame, 100, 50, text="Add task", command=lambda:add_todo("", settings.TODO_SMALL_COLOR), bg_color="#f0ecec")
    add_todo_btn.grid(column=0, row=0)
elif settings.APPLICATION_LANGUAGE == "DE":
    add_todo_btn = ctk.CTkButton(main_btns_frame, 100, 50, text="Aufgabe hinzufügen", command=lambda:add_todo("", settings.TODO_SMALL_COLOR), bg_color="#f0ecec")
    add_todo_btn.grid(column=0, row=0)
elif settings.APPLICATION_LANGUAGE == "ES":
    add_todo_btn = ctk.CTkButton(main_btns_frame, 100, 50, text="Agregar tarea", command=lambda:add_todo("", settings.TODO_SMALL_COLOR), bg_color="#f0ecec")
    add_todo_btn.grid(column=0, row=0)
elif settings.APPLICATION_LANGUAGE == "CH":
    add_todo_btn = ctk.CTkButton(main_btns_frame, 100, 50, text="添加任务", command=lambda:add_todo("", settings.TODO_SMALL_COLOR), bg_color="#f0ecec")
    add_todo_btn.grid(column=0, row=0)
else:
    add_todo_btn = ctk.CTkButton(main_btns_frame, 100, 50, text="Add task", command=lambda:add_todo("", settings.TODO_SMALL_COLOR), bg_color="#f0ecec")
    add_todo_btn.grid(column=0, row=0)

load_saved_todos()
root.bind("<KeyRelease>", add_todo_on_enter)
root.protocol("WM_DELETE_WINDOW", close_application_and_save)
root.mainloop()
