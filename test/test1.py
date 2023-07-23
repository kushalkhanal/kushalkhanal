import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

frame1 = tk.Frame(root, bg="red", width=400, height=200)
frame2 = tk.Frame(root, bg="green", width=400, height=200)
frame3 = tk.Frame(root, bg="blue", width=400, height=200)
frame4 = tk.Frame(root, bg="yellow", width=400, height=200)

frames = [frame1, frame2, frame3, frame4]
current_frame = 0

def show_frame(frame_index):
    frames[current_frame].place_forget()
    frames[frame_index].place(x=0, y=0)
    frames[frame_index].pack_propagate(False)

def next_frame():
    global current_frame
    new_frame = (current_frame + 1) % len(frames)
    show_frame(new_frame)
    current_frame = new_frame

def before_frame():
    global current_frame
    new_frame = (current_frame - 1) % len(frames)
    show_frame(new_frame)
    current_frame = new_frame

show_frame(0)

button_next = tk.Button(root, text="Next", command=next_frame)
button_next.place(x=10, y=170)

button_before = tk.Button(root, text="Before", command=before_frame)
button_before.place(x=70, y=170)

root.mainloop()
