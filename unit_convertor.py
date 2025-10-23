
import tkinter as tk
from tkinter import ttk, messagebox

def convert():
    category = category_var.get()
    value = entry_value.get()

    if not value:
        messagebox.showwarning("Input Error", "Please enter a value.")
        return

    try:
        value = float(value)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")
        return

    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    result = None

    if category == "Length":
        units = {"Meter": 1, "Centimeter": 0.01, "Kilometer": 1000, "Inch": 0.0254, "Foot": 0.3048}
        result = value * units[from_unit] / units[to_unit]

    elif category == "Weight":
        units = {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592}
        result = value * units[from_unit] / units[to_unit]

    elif category == "Temperature":
        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        else:
            messagebox.showerror("Error", "Invalid temperature conversion.")
            return

    label_result.config(text=f"Result: {round(result, 4)} {to_unit}")

def update_units(event=None):
    category = category_var.get()
    if category == "Length":
        units = ["Meter", "Centimeter", "Kilometer", "Inch", "Foot"]
    elif category == "Weight":
        units = ["Kilogram", "Gram", "Pound"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit"]
    else:
        units = []

    from_unit_menu['values'] = units
    to_unit_menu['values'] = units
    from_unit_var.set(units[0])
    to_unit_var.set(units[1])

root = tk.Tk()
root.title("Unit Converter")
root.geometry("480x620")
root.resizable(False, False)
root.configure(bg="#F7FAFC")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#F7FAFC", font=("Segoe UI", 12))
style.configure("TCombobox", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 13))
style.configure("TButton", font=("Segoe UI", 13, "bold"), padding=6)

title = tk.Label(root, text="Unit Converter", font=("Segoe UI", 22, "bold"), bg="#F7FAFC", fg="#2C3E50")
title.pack(pady=20)

card = tk.Frame(root, bg="white", bd=2, height=500)
card.pack(padx=15, pady=10)

tk.Label(card, text="Select Category:", font=("Segoe UI", 13, "bold"), bg="white").pack(pady=(25, 5))
category_var = tk.StringVar()
category_menu = ttk.Combobox(card, textvariable=category_var, values=["Length", "Weight", "Temperature"], state="readonly", width=20)
category_menu.pack(pady=(0, 20))
category_menu.bind("<<ComboboxSelected>>", update_units)
category_menu.current(0)

tk.Label(card, text="Enter Value:", font=("Segoe UI", 13, "bold"), bg="white").pack(pady=(10, 5))
entry_value = ttk.Entry(card, font=("Segoe UI", 13), width=25, justify="center")
entry_value.pack(pady=(0, 20))

tk.Label(card, text="From Unit:", font=("Segoe UI", 13, "bold"), bg="white").pack(pady=(10, 5))
from_unit_var = tk.StringVar()
from_unit_menu = ttk.Combobox(card, textvariable=from_unit_var, state="readonly", width=20)
from_unit_menu.pack(pady=(0, 20))

tk.Label(card, text="To Unit:", font=("Segoe UI", 13, "bold"), bg="white").pack(pady=(10, 5))
to_unit_var = tk.StringVar()
to_unit_menu = ttk.Combobox(card, textvariable=to_unit_var, state="readonly", width=20)
to_unit_menu.pack(pady=(0, 25))

convert_btn = ttk.Button(card, text="Convert", command=convert)
convert_btn.pack(pady=10)

label_result = tk.Label(card, text="Result:", font=("Segoe UI", 15, "bold"), bg="white", fg="#2C3E50")
label_result.pack(pady=15)

update_units()

root.mainloop()
