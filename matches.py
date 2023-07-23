from tkinter import *
from PIL import ImageTk, Image

app = Tk()
app.configure(bg="white")
w = app.winfo_screenwidth()
h = app.winfo_screenheight()
app.geometry(str(w) + "x" + str(h))
app.resizable(False, False)
app.state("zoomed")

# Creating a logo_frame
logo_frame = LabelFrame(app, width=170, height=100, bg="#EEEEEE", borderwidth=2, relief="raised")
logo_frame.place(x=0, y=0)

# Creating a LabelFrame.sidebar
side_bar = LabelFrame(app, width=170, height=650, borderwidth=2, relief="raised")
side_bar.place(x=0, y=100)

# /////////////////////////////////////////////////////////////////////
# Creating match1 LabelFrame
match_frame1 = LabelFrame(app, bg="white", height=h - 30, width=380, relief="flat")
# match_frame1.place(x=173, y=0)
match_frame1.pack_propagate(False)

# Adding image=match_list
match_list = ImageTk.PhotoImage(Image.open('Chat/chat_list.png'))
match_list_label = Label(match_frame1, image=match_list)
match_list_label.place(x=0, y=0)

# Creating a user_profile in chat_frame1>chat_list
user1_profile = Canvas(match_frame1, width=62, height=62, bg="white")
user1_profile.place(x=20, y=20)


def match_window(event):
    # Hide or destroy the match_frame1 when username1 label is clicked
    match_frame1.destroy()
    match_frame2.place(x=175, y=0)


# Creating a user Label in chat_frame1>chat_list
username1 = Label(match_frame1, text="Rahul038", font='Ariel, 17', cursor="hand2")
username1.place(x=115, y=40)

# Bind the hide_match_frame function to the username1 label
username1.bind("<Button-1>", match_window)

# Creating chat2 LabelFrame
match_frame2 = LabelFrame(app, height=h - 30, width=1186, relief="flat")
match_frame2.pack_propagate(False)

# Adding image=match_wind
match_wind = ImageTk.PhotoImage(Image.open('Matches/matches2.jpg'))
match_wind_label = Label(match_frame2, image=match_wind)
match_wind_label.place(x=0, y=0)


def match1_frame(event):
    # Show the chat_frame1 when the button is clicked
    match_frame1.place(x=173, y=0)


# Creating and Placing ???Matches???
match_image = Image.open("images/hearts.png")
resized_match = match_image.resize((30, 30))
match = ImageTk.PhotoImage(resized_match)
lab_match = Label(side_bar, image=match)
lab_match.place(x=20, y=245)
match_label = Label(side_bar, text="Matches", font="Ariel, 15", fg="grey")
match_label.place(x=55, y=250)

match_label.bind("<Button-1>", match1_frame)
lab_match.bind("<Button-1>", match1_frame)


app.mainloop()
