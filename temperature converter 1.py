import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius:.2f} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        result_label.config(text="Invalid input")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit:.2f} Fahrenheit is equal to {celsius:.2f} Celsius")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter App")

# Celsius to Fahrenheit conversion
celsius_label = tk.Label(window, text="Celsius:")
celsius_label.pack()
celsius_entry = tk.Entry(window)
celsius_entry.pack()
celsius_to_fahrenheit_button = tk.Button(window, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
celsius_to_fahrenheit_button.pack()

# Fahrenheit to Celsius conversion
fahrenheit_label = tk.Label(window, text="Fahrenheit:")
fahrenheit_label.pack()
fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.pack()
fahrenheit_to_celsius_button = tk.Button(window, text="Convert to Celsius", command=fahrenheit_to_celsius)
fahrenheit_to_celsius_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
