import tkinter as tk

def display_user_data(user_data):
    root = tk.Tk()
    root.title("User Data")

    # Create Labels and Entries for each key-value pair in the user_data dictionary
    for i, (key, value) in enumerate(user_data.items()):
        label = tk.Label(root, text=key)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

        entry = tk.Entry(root, width=30)
        entry.insert(0, value)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    user_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "address": "123 Main Street",
        "city": "New York",
        "country": "USA"
    }
    display_user_data(user_data)
