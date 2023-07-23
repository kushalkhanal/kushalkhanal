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


# Creating chat1 LabelFrame
chat_frame1 = LabelFrame(app, bg="white", height=h - 30, width=380, relief="flat")
chat_frame1.place(x=173, y=0)
chat_frame1.pack_propagate(False)

# Adding image=chat_list
chat_list = ImageTk.PhotoImage(Image.open('Chat/chat_list.png'))
chat_list_label = Label(chat_frame1, image=chat_list)
chat_list_label.place(x=0, y=0)

# Creating a user_profile in chat_frame1>chat_list
user1_profile = Canvas(chat_frame1, width=62, height=62, bg="white")
user1_profile.place(x=20, y=20)

# Creating a user Label in chat_frame1>chat_list
username1 = Label(chat_frame1, text="Rahul038", font='Ariel, 17', cursor="hand2")
username1.place(x=115, y=40)


def chat1_frame(event):
    # Show the chat_frame1 when the button is clicked
    chat_frame1.place(x=173, y=0)


# Creating and Placing "Chat"
chat_image = Image.open("images/speak.png")
resized_chat = chat_image.resize((30, 30))
chat = ImageTk.PhotoImage(resized_chat)
lab_chat = Label(side_bar, image=chat)
lab_chat.place(x=20, y=173)
chat_label = Label(side_bar, text="Chat", font="Ariel, 15", fg="grey")
chat_label.place(x=55, y=180)

# Binding function to chat_label and lab_chat
chat_label.bind("<Button-1>", chat1_frame)
lab_chat.bind("<Button-1>", chat1_frame)

# Creating chat2 LabelFrame
chat_frame2 = LabelFrame(app, height=h - 30, width=799, relief="flat")
# chat_frame2.place(x=560, y=0)
chat_frame2.pack_propagate(False)


def chat_window(event):
    if chat_frame2.winfo_ismapped():
        chat_frame2.place_forget()  # Hide chat_frame2
    else:
        chat_frame2.place(x=560, y=0)  # Show chat_frame2


# Binding chat_window to username1
username1.bind("<Button-1>", chat_window)

# Adding image=chat_wind
chat_wind = ImageTk.PhotoImage(Image.open('Chat/chat_wind.png'))
chat_wind_label = Label(chat_frame2, image=chat_wind)
chat_wind_label.place(x=0, y=0)

# Adding image=chat_top
chat_top = ImageTk.PhotoImage(Image.open('Chat/chat_top.png'))
chat_top_label = Label(chat_frame2, image=chat_top)
chat_top_label.place(x=0, y=0)

# Adding image=chat_bottom
chat_bottom = ImageTk.PhotoImage(Image.open('Chat/chat_bottom.png'))
chat_bottom_label = Label(chat_frame2, image=chat_bottom)
chat_bottom_label.place(x=0, y=644)

# Creating canvas on chat_top, chat_name and chat_bottom, microphone_frame, chat_type
chat_name = Canvas(chat_frame2, width=265, height=55, bg="#F99417")
chat_name.place(x=18, y=15)

microphone_frame = Canvas(chat_frame2, width=72, height=72, bg="#D9D9D9")
microphone_frame.place(x=18, y=653)


def chat_mic():
    pass


def chat_send():
    pass


# Chat microphone button
chat_mic_pic = (Image.open('Chat/mic.png'))
chat_mic_resize = chat_mic_pic.resize((52, 55))
chat_microphone = ImageTk.PhotoImage(chat_mic_resize)
chat_mic_button = Button(chat_frame2, image=chat_microphone, command=chat_mic)
chat_mic_button.place(x=28, y=660)

chat_type = Canvas(chat_frame2, width=652, height=66, bg="#D9D9D9")
chat_type.place(x=120, y=656)

# Chat send button
chat_send_pic = Image.open('Chat/send.png')
chat_send_resize = chat_send_pic.resize((52, 55))
chat_Send = ImageTk.PhotoImage(chat_send_resize)
chat_Send_button = Button(chat_frame2, image=chat_Send, command=chat_send)
chat_Send_button.place(x=710, y=660)

# /////////////////////////////////////////////////////////////////////
# Creating and placing ???Home???
dashboard_image = Image.open('images/hodas.png')
resized_dashboard = dashboard_image.resize((30, 30))
dashboard = ImageTk.PhotoImage(resized_dashboard)
lab_dashboard = Label(side_bar, image=dashboard)
lab_dashboard.place(x=20, y=102)
dashboard_label = Label(side_bar, text="Home", font="Ariel, 15", fg="grey")
dashboard_label.place(x=55, y=110)

# Creating and Placing ???Profile???
profile_image = Image.open('images/profile.png')
resized_profile = profile_image.resize((30, 30))
profile = ImageTk.PhotoImage(resized_profile)
lab_profile = Label(side_bar, image=profile)
lab_profile.place(x=20, y=35)
profile_label = Label(side_bar, text="Profile", font="Ariel, 15", fg="grey")
profile_label.place(x=55, y=40)

# Creating and Placing ???Chat???
chat_image = Image.open("images/speak.png")
resized_chat = chat_image.resize((30, 30))
chat = ImageTk.PhotoImage(resized_chat)
lab_chat = Label(side_bar, image=chat)
lab_chat.place(x=20, y=173)
chat_label = Label(side_bar, text="Chat", font="Ariel, 15", fg="grey")
chat_label.place(x=55, y=180)

# Creating and Placing ???Matches???
match_image = Image.open("images/hearts.png")
resized_heart = match_image.resize((30, 30))
match = ImageTk.PhotoImage(resized_heart)
lab_heart = Label(side_bar, image=match)
lab_heart.place(x=20, y=245)
match_label = Label(side_bar, text="Matches", font="Ariel, 15", fg="grey")
match_label.place(x=55, y=250)

# Creating and Placing ???search???
search_image = Image.open("images/seo.png")
resized_search = search_image.resize((30, 30))
search = ImageTk.PhotoImage(resized_search)
lab_search = Label(side_bar, image=search)
lab_search.place(x=20, y=315)
search_label = Label(side_bar, text="Search", font="Ariel, 15", fg="grey")
search_label.place(x=55, y=320)

# Creating and Placing ???setting???
setting_image = Image.open("images/setting_gear.png")
resized_setting = setting_image.resize((30, 30))
setting = ImageTk.PhotoImage(resized_setting)
lab_setting = Label(side_bar, image=setting)
lab_setting.place(x=20, y=530)
setting_label = Label(side_bar, text="Setting", font="Ariel, 15", fg="grey")
setting_label.place(x=55, y=530)

app.mainloop()

# # Adding image=chat_name
# chat_name = ImageTk.PhotoImage(Image.open('Chat/chat_name.png'))
# chat_name_label = Label(chat_frame, image=chat_name)
# chat_name_label.place(x=390, y=2)
