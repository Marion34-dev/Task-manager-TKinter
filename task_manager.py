import tkinter as tk
from tkinter import messagebox


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        # Set the background color
        self.master.configure(bg="light blue")

        # Create the 'username label' and entry field
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack(padx=10, pady=5)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(padx=10, pady=5)

        # Create the 'password label' and entry field
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack(padx=10, pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(padx=10, pady=5)

        # Create the login button
        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack(padx=10, pady=5)

        # Dictionary to store usernames and passwords
        self.users = {
            "admin": "password",
            "user1": "pass1",
            "user2": "pass2"
        }

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password match
        if username in self.users and self.users[username] == password:
            self.master.destroy()  # Close the login window
            TaskManagerWindow(username)  # Open the task manager window with the logged-in username
        else:
            messagebox.showerror("Login", "Invalid username or password.")


class TaskManagerWindow:
    def __init__(self, username):
        self.username = username

        self.master = tk.Tk()
        self.master.title("Task Manager")

        # Set the background color
        self.master.configure(bg="light green")

        # Create the task list display box
        self.task_list = tk.Listbox(self.master)
        self.task_list.grid(row=0, column=0, padx=10, pady=10, rowspan=6)

        # Create the 'type' entry field
        self.task_entry = tk.Entry(self.master)
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)
        self.task_entry.insert(tk.END, "type...")
        self.task_entry.bind("<FocusIn>", self.clear_entry)

        # Create the 'username' entry field
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        self.username_entry.insert(tk.END, "username...")
        self.username_entry.bind("<FocusIn>", self.clear_username_entry)

        # Create the add button
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=6, column=0, padx=10, pady=5)

        # Create the delete button
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=6, column=1, padx=10, pady=5)

        # Create the view mine button
        self.view_mine_button = tk.Button(self.master, text="View Mine", command=self.view_mine)
        self.view_mine_button.grid(row=7, column=0, padx=30, pady=5)

        # Create the view all button
        self.view_all_button = tk.Button(self.master, text="View All", command=self.view_all)
        self.view_all_button.grid(row=7, column=1, padx=30, pady=5)

        # List to store tasks
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        username = self.username_entry.get()
        if task and task != "type..." and username and username != "username...":
            self.tasks.append({"task": task, "user": username})
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, "type...")
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(tk.END, "username...")
        else:
            messagebox.showwarning("Task Manager", "Please enter a task and username.")

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)
        else:
            messagebox.showwarning("Task Manager", "Please select a task to delete.")

    def clear_entry(self, event):
        current_value = self.task_entry.get()
        if current_value == "type...":
            self.task_entry.delete(0, tk.END)

    def clear_username_entry(self, event):
        current_value = self.username_entry.get()
        if current_value == "username...":
            self.username_entry.delete(0, tk.END)

    def view_mine(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            if task['user'] == self.username:
                self.task_list.insert(tk.END, task['task'])

    def view_all(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task['task'])

    def run(self):
        self.master.mainloop()


def main():
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
