import tkinter as tk
from PIL import Image, ImageTk


def load_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Resize the image to fit the frame
    photo = ImageTk.PhotoImage(img)
    return photo


def update_image():
    photo = load_image("E:\code_academy\App\images/colorful-heart.jpg")
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection


# Create the main application window
root = tk.Tk()
root.title("Image Viewer")

# Create a frame to hold the image
frame = tk.Frame(root, width=300, height=300)
frame.pack()

# Load and display the initial image
initial_photo = load_image("E:\code_academy\App\images/colorful-heart.jpg")
image_label = tk.Label(frame, image=initial_photo)
image_label.pack()

# Create a button to update the image
update_button = tk.Button(root, text="Update Image", command=update_image)
update_button.pack()

# Start the GUI event loop
root.mainloop()
