import tkinter as tk


def on_checkbox_click():
    selected_hobbies = [hobby_var.get()
                        for hobby_var in hobbies_vars if hobby_var.get() != ""]
    print("Selected Hobbies:", ", ".join(selected_hobbies))


# List of hobbies
hobbies_list = ['Playing', 'Singing', 'Dancing', 'Reading', 'Writing']

# Create the main application window
app = tk.Tk()
app.title("Profile Frame with Hobbies")

# ... (your previous code for creating the profile_frame and other widgets) ...

# Function to create check buttons for hobbies


def create_hobbies_checkboxes():
    hobbies_frame = Frame(profile_frame, bg="#DB005C")
    # Adjust the position as per your requirement
    hobbies_frame.place(x=500, y=535)

    hobbies_vars = [tk.StringVar() for _ in range(len(hobbies_list))]

    for i, hobby in enumerate(hobbies_list):
        checkbox = tk.Checkbutton(
            hobbies_frame, text=hobby, variable=hobbies_vars[i], onvalue=hobby, offvalue="")
        checkbox.pack(anchor=tk.W)

    return hobbies_vars


hobbies_vars = create_hobbies_checkboxes()

# Creating the "Show Hobbies" button
show_hobbies_btn = tk.Button(
    profile_frame, text="Show Hobbies", command=on_checkbox_click)
# Adjust the position as per your requirement
show_hobbies_btn.place(x=650, y=570)

# Start the tkinter main event loop
app.mainloop()
