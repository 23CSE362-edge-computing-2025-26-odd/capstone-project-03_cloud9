import tkinter as tk
from tkinter import messagebox

def confirm_found():
    messagebox.showinfo("Confirmation", "Item has been marked as found!")

root = tk.Tk()
root.title("Item Found")
root.geometry("400x250")
root.config(bg="lightgray")

# Box (Frame)
frame = tk.Frame(root, bg="white", bd=3, relief="ridge", padx=30, pady=30)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Confirm Item Location", font=("Arial", 16, "bold"), bg="white").pack(pady=15)

tk.Button(frame, text="Item Found", font=("Arial", 14, "bold"),
          bg="green", fg="white", width=18, height=2,
          command=confirm_found).pack(pady=20)

root.mainloop()
