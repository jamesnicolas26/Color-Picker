import tkinter as tk
from tkinter import colorchooser

def pick_color():
    """Open color chooser and update the color label."""
    color = colorchooser.askcolor()[1]
    if color:
        label_color.config(text=color, bg=color)

# Create the main window
root = tk.Tk()
root.title("Color Picker")

# Create and place widgets
button_pick = tk.Button(root, text="Pick Color", command=pick_color)
button_pick.pack()

label_color = tk.Label(root, text="No color selected", width=20)
label_color.pack()

# Start the main loop
root.mainloop()
