import tkinter as tk
from tkinter import messagebox, ttk

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()

    if not (name and roll and marks):
        messagebox.showerror("Error", "All fields are required")
        return

    if not marks.isdigit():
        messagebox.showerror("Error", "Marks must be a number")
        return

    try:
        with open("students.txt", "a") as f:
            f.write(f"{name},{roll},{marks}\n")
        messagebox.showinfo("Success", "Student added successfully!")
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        marks_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Error saving student: {e}")

def view_students():
    try:
        with open("students.txt", "r") as f:
            records = f.readlines()

        if not records:
            messagebox.showinfo("Records", "No students found.")
            return

        # ---- New Window for Table ----
        top = tk.Toplevel(window)
        top.title("Student Records")
        top.geometry("450x300")

        tree = ttk.Treeview(top, columns=("Name", "Roll", "Marks"), show="headings")
        tree.heading("Name", text="Name")
        tree.heading("Roll", text="Roll Number")
        tree.heading("Marks", text="Marks")

        tree.column("Name", width=150)
        tree.column("Roll", width=100, anchor="center")
        tree.column("Marks", width=80, anchor="center")

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Insert records in table
        for line in records:
            name, roll, marks = line.strip().split(",")
            tree.insert("", "end", values=(name, roll, marks))

        # Scrollbar
        scrollbar = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    except FileNotFoundError:
        messagebox.showwarning("Warning", "No records file found!")

# ------------------ GUI SETUP ------------------
window = tk.Tk()
window.title("Student Record System")
window.geometry("420x280")
window.configure(bg="#f0f0f0")

title_label = tk.Label(window, text="📘 Student Record System", 
                       font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

form_frame = tk.Frame(window, bg="#f0f0f0")
form_frame.pack(pady=10)

# Labels + Entries
tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Roll Number:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="e")
roll_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
roll_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Marks:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5, sticky="e")
marks_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
marks_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(window, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Student", command=add_student, 
          font=("Arial", 11), bg="#4CAF50", fg="white", width=12).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="View Students", command=view_students, 
          font=("Arial", 11), bg="#2196F3", fg="white", width=12).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Exit", command=window.quit, 
          font=("Arial", 11), bg="#f44336", fg="white", width=12).grid(row=0, column=2, padx=5)

window.mainloop()