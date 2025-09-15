import tkinter as tk
from tkinter import messagebox

# Dummy credentials and item data
users = {"worker1": "1234", "worker2": "abcd"}
items = {
    "M001": "Zone A - Near Assembly Line",
    "M002": "Zone B - Storage Area",
    "M003": "Zone C - Loading Dock"
}

# ---------------- Login Page ----------------
def login():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()
    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()          # close login window
        open_search_page()      # go to search page
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ---------------- Search Page ----------------
def open_search_page():
    search_win = tk.Tk()
    search_win.title("Material Search")
    search_win.geometry("500x350")
    search_win.config(bg="lightgray")

    # Centered white box
    frame = tk.Frame(search_win, bg="white", bd=3, relief="ridge", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Search Material", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

    tk.Label(frame, text="Enter Material ID", font=("Arial", 12), bg="white").pack(pady=5)
    entry = tk.Entry(frame, font=("Arial", 13), width=28, bd=2, relief="solid")
    entry.pack(pady=5)

    result_label = tk.Label(frame, text="Location: -", font=("Arial", 13), bg="white")
    result_label.pack(pady=10)

    def search_item():
        item_id = entry.get().strip()
        location = items.get(item_id, "Not Found")
        result_label.config(text=f"Location: {location}")

    tk.Button(frame, text="Search", font=("Arial", 13, "bold"),
              bg="blue", fg="white", width=14, command=search_item).pack(pady=15)

    # Hint for demo
    tk.Label(frame, text="Demo IDs: M001, M002, M003",
             font=("Arial", 10), bg="white", fg="gray").pack()

    search_win.mainloop()

# ---------------- Root (Login Window) ----------------
root = tk.Tk()
root.title("Worker Login")
root.geometry("400x300")
root.config(bg="lightgray")

frame = tk.Frame(root, bg="white", bd=3, relief="ridge", padx=25, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Worker Login", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

tk.Label(frame, text="Username", font=("Arial", 12), bg="white").pack(pady=5)
entry_user = tk.Entry(frame, font=("Arial", 12), width=25, bd=2, relief="solid")
entry_user.pack(pady=5)

tk.Label(frame, text="Password", font=("Arial", 12), bg="white").pack(pady=5)
entry_pass = tk.Entry(frame, font=("Arial", 12), width=25, bd=2, relief="solid", show="*")
entry_pass.pack(pady=5)

tk.Button(frame, text="Login", font=("Arial", 12, "bold"),
          bg="green", fg="white", width=12, command=login).pack(pady=15)

root.mainloop()
