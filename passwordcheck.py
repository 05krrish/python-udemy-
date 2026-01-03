import tkinter as tk
from tkinter import messagebox

# ------------------ USER DATABASE ------------------
users = {
    "admin": "Admin@123",
    "user": "User@123"
}

# ------------------ PASSWORD STRENGTH ------------------
def check_strength(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    return has_upper and has_lower and has_digit and has_symbol

# ------------------ LOGIN FUNCTION ------------------
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    if username in users and users[username] == password:
        if check_strength(password):
            messagebox.showinfo("Success", f"Welcome {username}!")
        else:
            messagebox.showwarning(
                "Weak Password",
                "Password should contain:\n• Uppercase\n• Lowercase\n• Number\n• Symbol\n• Min 8 characters"
            )
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ------------------ SHOW / HIDE PASSWORD ------------------
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# ------------------ UI SETUP ------------------
root = tk.Tk()
root.title("Login System")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="LOGIN", font=("Arial", 18, "bold")).pack(pady=10)

# Username
tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password
tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Show password checkbox
show_var = tk.IntVar()
show_check = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password
)
show_check.pack()

# Login button
tk.Button(root, text="Login", width=15, command=login).pack(pady=15)

root.mainloop()
