import customtkinter as ctk

root = ctk.CTk()

root.title("Tägliche Aufgaben")

root.geometry("500x500")

# add todo button
def add_todo():
    def delete_todo():
        todo_frame.destroy()

    def complete_todo():
        todo_frame.destroy()

    def change_time_to_complete(button):
        fg_color = button.cget("fg_color")

        if fg_color == "green":
            button.configure(fg_color="yellow")
        elif fg_color == "yellow":
            button.configure(fg_color="red")
        elif fg_color == "red":
            button.configure(fg_color="green")


    todo_frame = ctk.CTkFrame(root)
    todo_entry = ctk.CTkEntry(todo_frame, width=200)
    todo_delete_btn = ctk.CTkButton(todo_frame, 25,25, text="🗑", command=delete_todo)
    todo_complete_btn = ctk.CTkButton(todo_frame, 25,25, text="✔", command=complete_todo)
    todo_time_btn = ctk.CTkButton(todo_frame, 25,25, fg_color="green", text="", command=lambda:change_time_to_complete(todo_time_btn))

    todo_time_btn.grid(column=0, row=0, padx=(0,5))
    todo_entry.grid(column=1, row=0)
    todo_delete_btn.grid(column=2, row=0, padx=(5,0))
    todo_complete_btn.grid(column=3, row=0, padx=(5,0))

    todo_frame.pack(pady=7)

def save_todos():
    todos_list = []
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkFrame):
            for nested_widget in widget.winfo_children():
                if isinstance(nested_widget, ctk.CTkEntry):
                    todos_list.append(nested_widget.get())

    def write_todos_to_file():
        with open("app/todos.txt", "r+") as file:
            for todo in todos_list:
                file.write(todo + "\n")

    write_todos_to_file()

main_btns_frame = ctk.CTkFrame(root)

add_todo_btn = ctk.CTkButton(main_btns_frame, 100, 50, text="Aufgabe hinzufügen", command=add_todo)
add_todo_btn.grid(column=0, row=0, padx=(0,5))

save_todos_btn = ctk.CTkButton(main_btns_frame, 50, 50, text="✎", command=save_todos, font=(None, 30))
save_todos_btn.grid(column=1, row=0)

main_btns_frame.pack(pady=5)

root.mainloop()
