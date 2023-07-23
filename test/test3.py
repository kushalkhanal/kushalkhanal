import tkinter as tk


def create_frame(root, row, column):
    frame = tk.Frame(root, width=100, height=100, borderwidth=1, relief="solid")
    frame.grid(row=row, column=column)
    return frame


# Create the main application window
root = tk.Tk()
root.title("Tkinter Grid with Frames")

# Create Label 1 with text "Add some pictures" in the first row
label1 = tk.Label(root, text="Add some pictures")
label1.grid(row=0, column=0, columnspan=3)

# Create Label 2 with text "3 are must" in the second row
label2 = tk.Label(root, text="3 are must")
label2.grid(row=1, column=0, columnspan=3)

# Create 8 frames in a 4x4 grid starting from the 4th row
frames = []
for row in range(3, 6):
    for col in range(3):
        frame = create_frame(root, row, col)
        frames.append(frame)

# Start the GUI event loop
root.mainloop()
