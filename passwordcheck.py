import tkinter as tk

root = tk.Tk()
root.title("Password Checker")
root.geometry("300x200")

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
    else:
        password_entry.config(show="")

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

toggle_btn = tk.Button(root, text="Show / Hide", command=toggle_password)
toggle_btn.pack()

root.mainloop()
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

show_var = tk.IntVar()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

show_check = tk.Checkbutton(root, text="Show Password",
                            variable=show_var,
                            command=toggle_password)
show_check.pack()
