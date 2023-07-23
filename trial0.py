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

# Creating Frames for labels
dashboard_frame = Frame(app, bg="red")
# dashboard_frame.place(x=200, y=150, width=800, height=550)

profile_frame = Frame(app, bg="green")
# profile_frame.place(x=200, y=150, width=800, height=550)

chat_frame = Frame(app, bg="blue")
# chat_frame.place(x=200, y=150, width=800, height=550)

match_frame = Frame(app, bg="indigo")
# match_frame.place(x=200, y=150, width=800, height=550)

search_frame = Frame(app, bg="lightblue")
# search_frame.place(x=200, y=150, width=800, height=550)

setting_frame = Frame(app, bg="pink")


# setting_frame.place(x=200, y=150, width=800, height=550)


def hide_all_frames():
    dashboard_frame.place_forget()
    profile_frame.place_forget()
    chat_frame.place_forget()
    match_frame.place_forget()
    search_frame.place_forget()
    setting_frame.place_forget()


def show_dashboard():
    hide_all_frames()
    dashboard_frame.place(x=200, y=150, width=800, height=550)


def show_profile():
    hide_all_frames()
    profile_frame.place(x=200, y=150, width=800, height=550)


def show_chat():
    hide_all_frames()
    chat_frame.place(x=200, y=150, width=800, height=550)


def show_matches():
    hide_all_frames()
    match_frame.place(x=200, y=150, width=800, height=550)


def show_search():
    hide_all_frames()
    search_frame.place(x=200, y=150, width=800, height=550)


def show_settings():
    hide_all_frames()
    setting_frame.place(x=200, y=150, width=800, height=550)


show_dashboard()

# Creating and placing "Home"
dashboard_image = Image.open('images/hodas.png')
resized_dashboard = dashboard_image.resize((30, 30))
dashboard = ImageTk.PhotoImage(resized_dashboard)
lab_dashboard = Label(side_bar, image=dashboard)
lab_dashboard.place(x=20, y=102)
dashboard_label = Label(side_bar, text="Home", font="Arial, 15", fg="grey")
dashboard_label.place(x=55, y=110)
dashboard_label.bind("<Button-1>", lambda event: show_dashboard())
dashboard_frame.tkraise()

# Creating and Placing "Profile"
profile_image = Image.open('images/profile.png')
resized_profile = profile_image.resize((30, 30))
profile = ImageTk.PhotoImage(resized_profile)
lab_profile = Label(side_bar, image=profile)
lab_profile.place(x=20, y=35)
profile_label = Label(side_bar, text="Profile", font="Arial, 15", fg="grey")
profile_label.place(x=55, y=40)
profile_label.bind("<Button-1>", lambda event: show_profile())

# Creating and Placing "Chat"
chat_image = Image.open("images/speak.png")
resized_chat = chat_image.resize((30, 30))
chat = ImageTk.PhotoImage(resized_chat)
lab_chat = Label(side_bar, image=chat)
lab_chat.place(x=20, y=173)
chat_label = Label(side_bar, text="Chat", font="Arial, 15", fg="grey")
chat_label.place(x=55, y=180)
chat_label.bind("<Button-1>", lambda event: show_chat())

# Creating and Placing "Matches"
match_image = Image.open("images/hearts.png")
resized_heart = match_image.resize((30, 30))
match = ImageTk.PhotoImage(resized_heart)
lab_heart = Label(side_bar, image=match)
lab_heart.place(x=20, y=245)
match_label = Label(side_bar, text="Matches", font="Arial, 15", fg="grey")
match_label.place(x=55, y=250)
match_label.bind("<Button-1>", lambda event: show_matches())

# Creating and Placing "Search"
search_image = Image.open("images/seo.png")
resized_search = search_image.resize((30, 30))
search = ImageTk.PhotoImage(resized_search)
lab_search = Label(side_bar, image=search)
lab_search.place(x=20, y=315)
search_label = Label(side_bar, text="Search", font="Arial, 15", fg="grey")
search_label.place(x=55, y=320)
search_label.bind("<Button-1>", lambda event: show_search())

# Creating and Placing "Setting"
setting_image = Image.open("images/setting_gear.png")
resized_setting = setting_image.resize((30, 30))
setting = ImageTk.PhotoImage(resized_setting)
lab_setting = Label(side_bar, image=setting)
lab_setting.place(x=20, y=530)
setting_label = Label(side_bar, text="Setting", font="Arial, 15", fg="grey")
setting_label.place(x=55, y=530)
setting_label.bind("<Button-1>", lambda event: show_settings())

# Creating and placing "Home" label in dashboard_frame
dashboard_label = Label(dashboard_frame, text="Home", font="Arial, 15", fg="white")
dashboard_label.place(x=20, y=20)

# Creating and placing "Profile" label in profile_frame
profile_label = Label(profile_frame, text="Profile", font="Arial, 15", fg="white")
profile_label.place(x=20, y=20)

# Creating and placing "Chat" label in chat_frame
chat_label = Label(chat_frame, text="Chat", font="Arial, 15", fg="white")
chat_label.place(x=20, y=20)

# Creating and placing "Matches" label in match_frame
match_label = Label(match_frame, text="Matches", font="Arial, 15", fg="white")
match_label.place(x=20, y=20)

# Creating and placing "Search" label in search_frame
search_label = Label(search_frame, text="Search", font="Arial, 15", fg="white")
search_label.place(x=20, y=20)

# Creating and placing "Setting" label in setting_frame
setting_label = Label(setting_frame, text="Setting", font="Arial, 15", fg="white")
setting_label.place(x=20, y=20)

app.mainloop()
