from tkinter import *
from PIL import ImageTk, Image

app = Tk()
w = app.winfo_screenwidth()
h = app.winfo_screenheight()
app.geometry(str(w) + "x" + str(h))
app.resizable(False, False)
app.state("zoomed")

# '''Creating a logo_frame'''
logo_frame = LabelFrame(app, width=205, height=105, borderwidth=0, relief="flat")
logo_frame.place(x=0, y=0)

i1 = ImageTk.PhotoImage(Image.open('trial/a1.png'))
l1 = Label(logo_frame, image=i1)
l1.place(x=0, y=0)

# '''Creating a LabelFrame.---sidebar---'''
side_bar = LabelFrame(app, width=205, height=650, borderwidth=0, relief="flat")
side_bar.place(x=0, y=107)

i2 = ImageTk.PhotoImage(Image.open('trial/a2.png'))
l2 = Label(side_bar, image=i2)
l2.place(x=0, y=0)

'''
Creating LabelFrame home_frame and adding other widgets for "home" option
'''
home_frame = LabelFrame(app, height=h - 30, width=w - 180, relief="flat")
home_frame.configure(width=1188, height=745, borderwidth=0, relief='flat')
home_frame.pack_propagate()

# Adding background image to home_frame
bg_home = ImageTk.PhotoImage(Image.open('Home/home_Mask2.png'))
home_bg_label = Label(home_frame, image=bg_home, bg="#EEEEEE")
home_bg_label.place(x=1, y=-1)
#
# # Adding girl image to home_frame
# girl_image = Image.open("Home/girlph.jpg")
# girl_image_res = girl_image.resize((345, 568))
# girl_image_tk = ImageTk.PhotoImage(girl_image_res)
# girl_label = Label(home_frame, image=girl_image_tk)
# girl_label.image = girl_image_tk  # Keep a reference to prevent garbage collection
# girl_label.place(x=35, y=32)
#
# # Adding left and right button for image_viewer
# left_btn_img = ImageTk.PhotoImage(Image.open("Icons/right-arrow.png"))
# left_button = Button(home_frame, image=left_btn_img)
# left_button.place(x=398, y=186)
#
# right_btn_img = ImageTk.PhotoImage(Image.open("Icons/left-arrow.png"))
# right_button = Button(home_frame, image=right_btn_img)
# right_button.place(x=398, y=240)
#
# # Adding Social Media icons
# facebook = ImageTk.PhotoImage(Image.open("Icons/facebook.png"))
# messenger = ImageTk.PhotoImage(Image.open("Icons/messenger.png"))
# instagram = ImageTk.PhotoImage(Image.open("Icons/instagram.png"))
# twitter = ImageTk.PhotoImage(Image.open("Icons/twitter.png"))
# snapchat = ImageTk.PhotoImage(Image.open("Icons/snapchat.png"))
# whatsapp = ImageTk.PhotoImage(Image.open("Icons/whatsapp.png"))
#
# facebook_label = Label(home_frame, image=facebook)
# messenger_label = Label(home_frame, image=messenger)
# instagram_label = Label(home_frame, image=instagram)
# twitter_label = Label(home_frame, image=twitter)
# snapchat_label = Label(home_frame, image=snapchat)
# whatsapp_label = Label(home_frame, image=whatsapp)
#
# facebook_label.place(x=740, y=36)
# messenger_label.place(x=834, y=36)
# instagram_label.place(x=928, y=36)
# twitter_label.place(x=740, y=130)
# snapchat_label.place(x=834, y=130)
# whatsapp_label.place(x=928, y=130)

'''
Creating Frame profile_frame and adding other widgets for "profile" option
'''
profile_frame = Frame(app)
profile_frame.configure(width=1188, height=745, borderwidth=0, relief='flat')
profile_frame.pack_propagate()

# Adding background image to home_frame
bg_profile = ImageTk.PhotoImage(Image.open('Profile/profile_Mask1.png'))
profile_bg_label = Label(profile_frame, image=bg_profile)
profile_bg_label.place(x=1, y=-1)

'''
Creating Frame chat_frame and adding other widgets for "chat" option
'''
chat_frame = Frame(app)
chat_frame.configure(width=1188, height=745, borderwidth=0, relief='flat')
chat_frame.pack_propagate()

# Creating labelFrame for below chat_list
chat_list = LabelFrame(chat_frame)
chat_list.configure(width=290, height=745, borderwidth=0, relief='flat')
chat_list.place(x=1, y=-1)

# Adding background image to chat-frame
bg_chat = ImageTk.PhotoImage(Image.open('Chat/chat_list1.png'))
chat_bg_label = Label(chat_list, image=bg_chat)
chat_bg_label.place(x=0, y=0)

########################
# Creating Label_Frame for below chat_wind
chat_window = LabelFrame(chat_frame)
chat_window.configure(width=793, height=745, borderwidth=0, relief='flat')
chat_window.place(x=295, y=-1)

# Adding image=chat_wind
bg_wind = ImageTk.PhotoImage(Image.open('Chat/chat_Window.png'))
bg_wind_label = Label(chat_window, image=bg_wind, borderwidth=0, relief='flat')
bg_wind_label.place(x=0, y=0)

# Adding image=chat_top
chat_top = ImageTk.PhotoImage(Image.open('Chat/chat_top.png'))
chat_top_label = Label(chat_window, image=chat_top, borderwidth=0, relief='flat')
chat_top_label.place(x=0, y=0)

# Adding image=chat_bottom
chat_bottom = ImageTk.PhotoImage(Image.open('Chat/chat_Bottom.png'))
chat_bottom_label = Label(chat_window, image=chat_bottom, borderwidth=0, relief='flat')
chat_bottom_label.place(x=0, y=644)

# Creating canvas on chat_top, chat_name and chat_bottom, microphone_frame, chat_type
chat_name = Canvas(chat_window, width=265, height=55, bg="#FFFFFF", borderwidth=0, relief='flat')
chat_name.place(x=18, y=15)

microphone_frame = Canvas(chat_window, width=72, height=72, bg="#FEA1A1", borderwidth=0, relief='flat')
microphone_frame.place(x=18, y=653)


def chat_mic():
    pass


def chat_send():
    pass


# Chat microphone button
chat_mic_pic = (Image.open('Chat/mic.png'))
chat_mic_resize = chat_mic_pic.resize((52, 55))
chat_microphone = ImageTk.PhotoImage(chat_mic_resize)
chat_mic_button = Button(chat_window, image=chat_microphone, command=chat_mic)
chat_mic_button.place(x=28, y=660)

chat_type = Canvas(chat_window, width=652, height=66, bg="#D9D9D9", borderwidth=0, relief='flat')
chat_type.place(x=120, y=656)

# Chat send button
chat_send_pic = Image.open('Chat/send.png')
chat_send_resize = chat_send_pic.resize((52, 55))
chat_Send = ImageTk.PhotoImage(chat_send_resize)
chat_Send_button = Button(chat_window, image=chat_Send, command=chat_send)
chat_Send_button.place(x=710, y=660)

'''
Creating LabelFrame match_frame and adding other widgets for "match" option
'''
match_frame = Frame(app)
match_frame.configure(width=1188, height=745, bg='#EEEEEE', borderwidth=0, relief='flat')
match_frame.pack_propagate()

# Adding background image to home_frame
bg_match = ImageTk.PhotoImage(Image.open('Matches/match_bg.png'))
match_bg_label = Label(match_frame, image=bg_match)
match_bg_label.place(x=1, y=-1)

'''
Creating LabelFrame search_frame and adding other widgets for "search" option
'''
search_frame = Frame(app)
search_frame.configure(width=1190, height=745, borderwidth=0, relief='flat', bg='#EEEEEE')
search_frame.pack_propagate()

bg_search = ImageTk.PhotoImage(Image.open('Search/bg_search.png'))
search_bg_label = Label(search_frame, image=bg_search)
search_bg_label.place(x=1, y=-1)
'''
Creating LabelFrame setting_frame and adding other widgets for "setting" option
'''
setting_frame = Frame(app)
setting_frame.configure(width=1188, height=745, bg='#EEEEEE', borderwidth=0, relief='flat')
setting_frame.pack_propagate()

# Creating a labelFrame to put setting_list Label
setting_list_frame = LabelFrame(setting_frame)
setting_list_frame.configure(width=294, height=745, bg='#EEEEEE', borderwidth=0, relief='flat')
setting_list_frame.place(x=2, y=-1)

# Adding background image to home_frame
bg_search = ImageTk.PhotoImage(Image.open('Setting/setting_list.png'))
setting_list_label = Label(setting_list_frame, image=bg_search)
setting_list_label.place(x=0, y=0)

# Creating frame to keep each tab content
setting_window_frame = LabelFrame(setting_frame)
setting_window_frame.configure(width=883, height=745, bg='#EEEEEE', borderwidth=0, relief='flat')
setting_window_frame.place(x=298, y=-1)

bg_window = ImageTk.PhotoImage(Image.open('Setting/setting_Window.png'))
window_bg_label = Label(setting_window_frame, image=bg_window)
window_bg_label.place(x=0, y=0)


def hide_frames(show_frame):
    frames = [home_frame, profile_frame, chat_frame, match_frame, search_frame, setting_frame]
    for frame in frames:
        if frame != show_frame:
            frame.place_forget()


def show_home():
    hide_frames(home_frame)
    home_frame.place(x=175, y=0)


def show_profile():
    hide_frames(profile_frame)
    profile_frame.place(x=175, y=0)


def show_chat():
    hide_frames(chat_frame)
    chat_frame.place(x=175, y=0)


def show_matches():
    hide_frames(match_frame)
    match_frame.place(x=175, y=0)


def show_search():
    hide_frames(search_frame)
    search_frame.place(x=175, y=0)


def show_settings():
    hide_frames(setting_frame)
    setting_frame.place(x=175, y=0)


show_home()

# Creating and placing ???Home???
home_image = Image.open('images/hodas.png')
resized_home = home_image.resize((30, 30))
home = ImageTk.PhotoImage(resized_home)
lab_home = Label(side_bar, image=home, bg="#B7B7B7")
lab_home.place(x=20, y=102)
home_label = Label(side_bar, text="Home", font=("Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
home_label.place(x=55, y=110)
lab_home.bind("<Button-1>", lambda event: show_home())
home_label.bind("<Button-1>", lambda event: show_home())

# Creating and Placing ???Profile???
profile_image = Image.open('images/profile.png')
resized_profile = profile_image.resize((30, 30))
profile = ImageTk.PhotoImage(resized_profile)
lab_profile = Label(side_bar, image=profile, bg="#B7B7B7")
lab_profile.place(x=20, y=35)
profile_label = Label(side_bar, text="Profile", font=("Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
profile_label.place(x=55, y=40)
profile_label.bind("<Button-1>", lambda event: show_profile())

# Creating and Placing ???Chat???
chat_image = Image.open("images/speak.png")
resized_chat = chat_image.resize((30, 30))
chat = ImageTk.PhotoImage(resized_chat)
lab_chat = Label(side_bar, image=chat, bg="#B7B7B7")
lab_chat.place(x=20, y=173)
chat_label = Label(side_bar, text="Chat", font=("Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
chat_label.place(x=55, y=180)
chat_label.bind("<Button-1>", lambda event: show_chat())

# Creating and Placing ???Matches???
match_image = Image.open("images/hearts.png")
resized_heart = match_image.resize((30, 30))
match = ImageTk.PhotoImage(resized_heart)
lab_heart = Label(side_bar, image=match, bg="#B7B7B7")
lab_heart.place(x=20, y=245)
match_label = Label(side_bar, text="Matches", font=("Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
match_label.place(x=55, y=250)
match_label.bind("<Button-1>", lambda event: show_matches())

# Creating and Placing ???search???
search_image = Image.open("images/seo.png")
resized_search = search_image.resize((30, 30))
search = ImageTk.PhotoImage(resized_search)
lab_search = Label(side_bar, image=search, bg="#B7B7B7")
lab_search.place(x=20, y=315)
search_label = Label(side_bar, text="Search", font=("Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
search_label.place(x=55, y=320)
search_label.bind("<Button-1>", lambda event: show_search())

# Creating and Placing ???setting???
setting_image = Image.open("images/setting_gear.png")
resized_setting = setting_image.resize((30, 30))
setting = ImageTk.PhotoImage(resized_setting)
lab_setting = Label(side_bar, image=setting, bg="#B7B7B7")
lab_setting.place(x=20, y=530)
setting_label = Label(side_bar, text="Setting", font=("Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
setting_label.place(x=55, y=530)
setting_label.bind("<Button-1>", lambda event: show_settings())

app.mainloop()
