import customtkinter as ctk

root = ctk.CTk()

root.title("MinimalDo")

root.geometry("500x500")

root.resizable(False,False)

def add_todo(todo: str):
    def complete_todo():
        todo_frame.destroy()

    def change_time_to_complete(button):
        fg_color = button.cget("fg_color")

        if fg_color == "green":
            button.configure(fg_color="yellow")
            button.configure(hover_color="yellow")
        elif fg_color == "yellow":
            button.configure(fg_color="red")
            button.configure(hover_color="red")
        elif fg_color == "red":
            button.configure(fg_color="green")
            button.configure(hover_color="green")


    todo_frame = ctk.CTkFrame(root)
    todo_frame.pack(pady=7)

    todo_entry = ctk.CTkEntry(todo_frame, width=200)
    todo_entry.insert(0, todo)
    todo_entry.grid(column=1, row=0)

    todo_complete_btn = ctk.CTkButton(todo_frame, 25,25, text="✔", command=complete_todo)
    todo_complete_btn.grid(column=3, row=0, padx=(5,0))

    todo_time_btn = ctk.CTkButton(todo_frame, 25,25, fg_color="green", hover_color="green" ,text="", command=lambda:change_time_to_complete(todo_time_btn))
    todo_time_btn.grid(column=0, row=0, padx=(0,5))


def load_saved_todos():
    with open("todos.txt", "r") as file:
        todos = [line.strip() for line in file.readlines()]
        
        for todo in todos:
            add_todo(todo)


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



def close_application_and_save():
    save_todos()
    root.destroy()


main_btns_frame = ctk.CTkFrame(root)
main_btns_frame.pack(pady=5)

add_todo_btn = ctk.CTkButton(main_btns_frame, 100, 50, text="Aufgabe hinzufügen", command=lambda:add_todo(""), bg_color="#f0ecec")
add_todo_btn.grid(column=0, row=0)


load_saved_todos()
root.protocol("WM_DELETE_WINDOW", close_application_and_save)
root.mainloop()
