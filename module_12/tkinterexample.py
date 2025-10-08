import tkinter as tk
from tkinter import messagebox
from challenge import Adult, Child

def calculate_bmi():
    name = name_entry.get()
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for age, weight, and height.")
        return

    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    result = (
        f"--- BMI Report for {person.name} ---\n"
        f"Age: {person.age}\n"
        f"Weight: {person.weight} kg\n"
        f"Height: {person.height} m\n"
        f"BMI: {person.bmi}\n"
        f"Category: {person.get_bmi_category()}"
    )
    messagebox.showinfo("BMI Result", result)

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# GUI Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0, pady=5, padx=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Age:").grid(row=1, column=0, pady=5, padx=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, pady=5, padx=5)

tk.Label(root, text="Weight (kg):").grid(row=2, column=0, pady=5, padx=5, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Height (m):").grid(row=3, column=0, pady=5, padx=5, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=3, column=1, pady=5, padx=5)

# Calculate Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=4, columnspan=2, pady=15)

# Start GUI
root.mainloop()
