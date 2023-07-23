import tkinter as tk

def on_checkbox_click():
    selected_hobbies = [hobby_var.get() for hobby_var in hobbies_vars]
    print("Selected Hobbies:", ", ".join(selected_hobbies))

# List of hobbies
hobbies = ["Reading", "Gardening", "Painting", "Cooking", "Sports"]

# Create the main application window
app = tk.Tk()
app.title("Hobbies Checkboxes")

# Create tkinter IntVars to store the values of the check boxes
hobbies_vars = [tk.StringVar() for _ in range(len(hobbies))]

# Create the check boxes
for i, hobby in enumerate(hobbies):
    checkbox = tk.Checkbutton(app, text=hobby, variable=hobbies_vars[i], onvalue=hobby, offvalue="")
    checkbox.pack(anchor=tk.W)

# Create a button to display the selected hobbies
show_button = tk.Button(app, text="Show Hobbies", command=on_checkbox_click)
show_button.pack()

# Start the tkinter main event loop
app.mainloop()
