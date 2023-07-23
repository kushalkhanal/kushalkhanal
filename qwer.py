import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
from pymongo import MongoClient
from base64 import *
import re, io

client = MongoClient('mongodb://localhost:27017')
database = client['matchmaker']
collection = database['users']
upload_collection = database['uploaded_pic']

app = Tk()
w = app.winfo_screenwidth()
h = app.winfo_screenheight()
app.title("Matchmaker")
app.geometry(str(w) + "x" + str(h))
app.resizable(False, False)
app.state("zoomed")


with open("phone.txt", "r") as file:
    phone = file.read().strip()
    user_data = collection.find_one({'phone': phone})


# Media icons
facebook1 = (Image.open("Icons/facebook.png"))
r_facebook = facebook1.resize((50, 50))
facebook = ImageTk.PhotoImage(r_facebook)

twitter1 = (Image.open("Icons/twitter.png"))
r_twitter = twitter1.resize((50, 50))
twitter = ImageTk.PhotoImage(r_twitter)

snapchat1 = (Image.open("Icons/snapchat.png"))
r_snapchat = snapchat1.resize((50, 50))
snapchat = ImageTk.PhotoImage(r_snapchat)

'''Creating a logo_frame'''
logo_frame = LabelFrame(app, width=205, height=105,
                        borderwidth=0, relief="flat")
logo_frame.place(x=0, y=0)

i1 = ImageTk.PhotoImage(Image.open('trial/a1.png'))
l1 = Label(logo_frame, image=i1)
l1.place(x=0, y=0)

'''Creating a LabelFrame.---sidebar---'''
side_bar = LabelFrame(app, width=205, height=650,
                      borderwidth=0, relief="flat")
side_bar.place(x=0, y=107)

i2 = ImageTk.PhotoImage(Image.open('trial/a2.png'))
l2 = Label(side_bar, image=i2)
l2.place(x=0, y=0)

def upload_picture():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        with open(file_path, "rb") as image_file:
            encoded_image = b64encode(image_file.read())
        upload_collection.insert_one({'phone':user_data['phone'],'image':encoded_image})
with open("phone.txt", "r") as file:
    phone = file.read().strip()
    image_data = upload_collection.find_one({'phone': phone})
def show_picture():
    global image_data
    encoded_image = image_data["image"]
    image_data = b64decode(encoded_image)
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((200,150))
    # Convert the image to a Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image)
    # Create a Tkinter label and display the image
    image_label = Label(home_frame, image = tk_image)
    image_label.image = tk_image
    image_label.place(x = 10,y = 10)
    


'''
Creating LabelFrame home_frame and adding other widgets for "home" option
This includes all a image viewer user info, type of relationship, interest and hobbies and social media.
'''
home_frame = LabelFrame(app)
home_frame.configure(width=1188, height=745, borderwidth=0, relief='flat')
home_frame.pack_propagate()

# Adding background image to home_frame
bg_home = ImageTk.PhotoImage(Image.open('Home/home.png'))
home_bg_label = Label(home_frame, image=bg_home, bg="#EEEEEE")
home_bg_label.place(x=1, y=-1)

# Image viewer code
girl_image = Image.open("Home/girlph.jpg")
girl_image_res = girl_image.resize((345, 568))
girl_image_tk = ImageTk.PhotoImage(girl_image_res)
girl_label = Label(home_frame, image=girl_image_tk)
girl_label.image = girl_image_tk  # Keep a reference to prevent garbage collection
girl_label.place(x=35, y=32)

# left_button
left_btn_img = ImageTk.PhotoImage(Image.open("Icons/right-arrow.png"))
left_button = Button(home_frame, image=left_btn_img, relief="flat")
left_button.place(x=399, y=174)

# right_button
right_btn_img = ImageTk.PhotoImage(Image.open("Icons/left-arrow.png"))
right_button = Button(home_frame, image=right_btn_img, relief="flat")
right_button.place(x=399, y=228)



# like_button
like_button_img = ImageTk.PhotoImage(Image.open("Home/like.png"))
like_button = Button(home_frame, image=like_button_img)
like_button.place(x=395, y=370)

# dislike_button
dislike_button_img = ImageTk.PhotoImage(Image.open("Home/dislike.png"))
dislike_button = Button(home_frame, image=dislike_button_img)
dislike_button.place(x=395, y=455)

upload_button = Button(home_frame, text="Upload your picture",command=upload_picture)
upload_button.place(x=395, y=530)

show_button = Button(home_frame, text="Picture",command=show_picture)
show_button.place(x=395, y=590)

def picture():
    global encoded_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        with open(file_path, "rb") as image_file:
            encoded_image = b64encode(image_file.read())
    






# '''Creating Entries to display user info'''
'''
Creating Frame profile_frame and adding other widgets for "profile" option
'''
profile_frame = Frame(app)
profile_frame.configure(width=1188, height=745,
                        borderwidth=0, relief='flat')
profile_frame.place(x=100, y=10)

# Adding background image to home_frame
# bg_profile = ImageTk.PhotoImage(Image.open('Profile/profile_Mask.png'))
# profile_bg_label = Label(profile_frame, image=bg_profile)
# profile_bg_label.place(x=1, y=-1)
profile_frame.config(bg="#DB005C")

# Adding profile image
profile_img = Image.open("Home/girlph.jpg")
profile_img_res = profile_img.resize((345, 568))
profile_img_tk = ImageTk.PhotoImage(profile_img_res)
profile_label = Label(profile_frame, image=profile_img_tk)
# Keep a reference to prevent garbage collection
profile_label.image = girl_image_tk
profile_label.place(x=35, y=32)

# '''Creating a multiline widget to put user preferred relation type'''
relation_type = Text(profile_frame, height=6, width=10, font=(
    "Ariel", 16), bg="#DB005C", relief="flat")
relation_type.place(x=520, y=50)


# Creating social-media buttons
facebook_btn11 = Button(profile_frame, image=facebook)
twitter_btn11 = Button(profile_frame, image=twitter)
snapchat_btn11 = Button(profile_frame, image=snapchat)

facebook_btn11.place(x=399, y=52)
twitter_btn11.place(x=399, y=125)
snapchat_btn11.place(x=399, y=199)


user_info = Canvas(profile_frame, width=230, height=330,
                   bg="#DB005C", highlightthickness=0)
user_info.place(x=640, y=200-150)

username = Label(profile_frame, text="Username", font=(
    "Arial", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
username.place(x=500, y=210-150)
user_info.create_line(10, 45, 220, 45, fill="#164B60", width=3)
user_username = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                      fg="#FFA41B")
user_username.place(x=650, y=210-150)
user_username.insert(
    0, user_data['Last Name']+user_data['First Name']+phone[0:3])
user_username.config(state="readonly")

name = Label(profile_frame, text="Name", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
name.place(x=500, y=265-150)
user_info.create_line(10, 95, 220, 95, fill="#164B60", width=3)
user_name = Entry(profile_frame, width=18, font="Arial, 15",
                  borderwidth=0, readonlybackground="#DB005C", fg="#FFA41B")
user_name.place(x=650, y=260-150)
user_name.insert(0, user_data['First Name'] + ' '+user_data['Last Name'])
user_name.config(state="readonly")

age = Label(profile_frame, text="Date of Birth", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
age.place(x=500, y=320-150)
user_info.create_line(10, 150, 220, 150, fill="#164B60", width=3)
user_age = Entry(profile_frame, width=18, font="Arial, 15",
                 borderwidth=0, readonlybackground="#DB005C", fg="#FFA41B")
user_age.place(x=650, y=315-150)
user_age.insert(0, user_data['DOB'])
user_age.config(state="readonly")

address = Label(profile_frame, text="Address", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
address.place(x=500, y=375-150)
user_info.create_line(10, 205, 220, 205, fill="#164B60", width=3)
user_address = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                     fg="#FFA41B")
user_address.place(x=650, y=370-150)
user_address.insert(0, user_data['location'])
user_address.config(state="readonly")

gender = Label(profile_frame, text="I'm a", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
gender.place(x=500, y=430-150)
user_info.create_line(10, 260, 220, 260, fill="#164B60", width=3)
user_gender = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                    fg="#FFA41B")
user_gender.place(x=650, y=425-150)
user_gender.insert(0, user_data['gender'])
user_gender.config(state="readonly")

seeking = Label(profile_frame, text="Looking for ", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
seeking.place(x=500, y=485-150)
user_info.create_line(10, 312, 220, 312, fill="#164B60", width=3)
user_seeking = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                     fg="#FFA41B")
user_seeking.place(x=650, y=480-150)
user_seeking.insert(0, user_data['seeking gender'])
user_seeking.config(state="readonly")


def add_hobbies():
    hobbies_frame = Frame(profile_frame, height=100, width=50, bg='white')
    home_frame.place(x=10, y=30)


add_hobbies_btn = Button(profile_frame, text="Add Hobbies",
                         font=("Ariel", 17, "bold"), bg="#DB005C", command=add_hobbies)
add_hobbies_btn.place(x=650, y=400)

# arrows for a frame
# right_arrow = ImageTk.PhotoImage(Image.open("Icons/right_aro.png"))
# right_btn1 = Button(profile_frame, image=right_arrow, bg="#ADD8E6", width=45, height=30, cursor="circle",
#                     relief="flat", borderwidth=0)
# right_btn1.place(x=1007, y=554)

# left_arrow = ImageTk.PhotoImage(Image.open("Icons/left_aro.png"))
# left_btn1 = Button(profile_frame, image=left_arrow, bg="#ADD8E6", width=45, height=30, cursor="circle",
#                    relief="flat", borderwidth=0)
# left_btn1.place(x=897, y=456)


# creating Entries to display user_interest and a scrollbar
# user_interest = LabelFrame(
#     profile_frame, width=220, height=365, bg="blue", borderwidth=0)
# user_interest.place(x=910, y=40)

# scrollbar = Scrollbar(user_interest)
# scrollbar.place(x=80, y=0, height=200)

# mylist = Listbox(user_interest, font=("Arial", 17),
#                  yscrollcommand=scrollbar.set, relief="flat", bg="#DB005C")
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))

# mylist.place(x=0, y=0, width=220, height=380)
# scrollbar.config(command=mylist.yview)

'''
Creating Frame chat_frame and adding other widgets for "chat" option
'''
chat_frame = Frame(app)
chat_frame.configure(width=1188, height=745, borderwidth=0, relief='flat')
chat_frame.pack_propagate()


def chat_wind():
    chat_window.place(x=295, y=-1)


# Creating labelFrame for below chat_list
chat_list = LabelFrame(chat_frame)
chat_list.configure(width=290, height=745, borderwidth=0, relief='flat')
chat_list.place(x=1, y=-1)

# Adding background image to chat-frame
bg_chat = ImageTk.PhotoImage(Image.open('Chat/chat_list1.png'))
chat_bg_label = Label(chat_list, image=bg_chat)
chat_bg_label.place(x=0, y=0)

userprofile = Canvas(chat_frame, bg="red", height=54,
                     width=54, bd=0, relief="ridge", highlightthickness=0)
userprofile.place(x=20, y=30)

user_name = Entry(chat_frame, font=("Ariel", 17),
                  width=14, cursor="circle")
user_name.place(x=80, y=52)
user_Name = 'Raul054'
user_name.insert(END, user_Name)
user_name.config(state=DISABLED)
user_name.bind('<Button-1>', lambda event: chat_wind())

########################
# Creating Label_Frame for below chat_wind
chat_window = LabelFrame(chat_frame)
chat_window.configure(width=793, height=745, borderwidth=0, relief='flat')
# chat_window.place(x=295, y=-1)

# Adding image=chat_wind
bg_wind = ImageTk.PhotoImage(Image.open('Chat/chat_Window.png'))
bg_wind_label = Label(chat_window, image=bg_wind,
                      borderwidth=0, relief='flat')
bg_wind_label.place(x=0, y=0)

# Adding image=chat_top
chat_top = ImageTk.PhotoImage(Image.open('Chat/chat_top.png'))
chat_top_label = Label(chat_window, image=chat_top,
                       borderwidth=0, relief='flat')
chat_top_label.place(x=0, y=0)

# Adding image=chat_bottom
chat_bottom = ImageTk.PhotoImage(Image.open('Chat/chat_Bottom.png'))
chat_bottom_label = Label(
    chat_window, image=chat_bottom, borderwidth=0, relief='flat')
chat_bottom_label.place(x=0, y=644)

# Creating canvas on chat_top, chat_name and chat_bottom, microphone_frame, chat_type
chat_name = Canvas(chat_window, width=200, height=55,
                   bg="#FFFFFF", borderwidth=0, relief='flat')
chat_name.place(x=18, y=15)

user_detail = Entry(chat_window, font=(
    "Ariel", 19), width=13, relief="flat")
user_detail.place(x=25, y=30)
user_Detail = 'Raul, 19'
user_detail.insert(END, user_Detail)
user_detail.config(state=DISABLED)

microphone_frame = Canvas(
    chat_window, width=72, height=72, bg="#FEA1A1", borderwidth=0, relief='flat')
microphone_frame.place(x=18, y=653)


def chat_mic():
    pass


def chat_send():
    pass


# Chat microphone button
chat_mic_pic = (Image.open('Chat/mic.png'))
chat_mic_resize = chat_mic_pic.resize((52, 55))
chat_microphone = ImageTk.PhotoImage(chat_mic_resize)
chat_mic_button = Button(
    chat_window, image=chat_microphone, command=chat_mic)
chat_mic_button.place(x=28, y=660)

chat_type = Canvas(chat_window, width=652, height=66,
                   bg="#D9D9D9", borderwidth=0, relief='flat')
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
match_frame.configure(width=1188, height=745,
                      bg='#EEEEEE', borderwidth=0, relief='flat')
match_frame.pack_propagate()


def match_wind():
    match_user_list.place_forget()
    match_user_frame.place(x=1, y=-1)


def back_list():
    match_user_frame.place_forget()
    match_user_list.place(x=1, y=-1)


# Creating labelFrame for below chat_list
match_user_list = LabelFrame(match_frame)
match_user_list.configure(width=290, height=745,
                          borderwidth=0, relief='flat')
match_user_list.place(x=1, y=-1)

# Adding background image to home_frame
bg_match = ImageTk.PhotoImage(Image.open('Matches/match_List.png'))
match_bg_label = Label(match_user_list, image=bg_match)
match_bg_label.place(x=0, y=0)

match_profile = Canvas(match_frame, bg="red", height=54,
                       width=54, bd=0, relief="ridge", highlightthickness=0)
match_profile.place(x=20, y=30)

match_name = Entry(match_frame, font=(
    "Ariel", 17), width=14, cursor="circle")
match_name.place(x=80, y=52)
match_Name = 'Raul054'  # Actual matched username
match_name.insert(END, match_Name)
match_name.config(state=DISABLED)
match_name.bind('<Button-1>', lambda event: match_wind())

# Now for match window
match_user_frame = LabelFrame(match_frame)
match_user_frame.configure(
    width=1200, height=745, borderwidth=0, relief='flat')

bg_match_window = ImageTk.PhotoImage(
    Image.open("Matches/match_Window.png"))
match_window_label = Label(match_user_frame, image=bg_match_window)
match_window_label.place(x=0, y=0)

# Creating social-media buttons
facebook_btn12 = Button(match_user_frame, image=facebook)
twitter_btn12 = Button(match_user_frame, image=twitter)
snapchat_btn12 = Button(match_user_frame, image=snapchat)

facebook_btn12.place(x=311, y=63)
twitter_btn12.place(x=311, y=136)
snapchat_btn12.place(x=311, y=209)

# '''Creating Entries to display user info'''
match_user_info = LabelFrame(match_user_frame)
match_user_info.configure(width=388, height=366,
                          bg="#DB005C", borderwidth=0)
match_user_info.place(x=393, y=65)

user_info = Canvas(match_user_info, width=230, height=330,
                   bg="#DB005C", highlightthickness=0)
user_info.place(x=150, y=14)

username = Label(match_user_info, text="Username", font=(
    "Arial", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
username.place(x=15, y=20)
user_username = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                      fg="#FFA41B")
user_username.place(x=165, y=20)
# user_username.insert(0, "Raul05dxfcgvhjjrxtcfyvgbhrdxfcvghjb")
user_username.config(state="readonly")
user_info.create_line(10, 40, 220, 40, fill="#164B60", width=3)

name = Label(match_user_info, text="Name", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
name.place(x=15, y=73)
user_name = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                  fg="#FFA41B")
user_name.place(x=165, y=73)
# user_name.insert(0, "Rasuoboac ad")
user_name.config(state="readonly")
user_info.create_line(10, 95, 220, 95, fill="#164B60", width=3)

age = Label(match_user_info, text="Age", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
age.place(x=15, y=128)
user_info.create_line(10, 150, 220, 150, fill="#164B60", width=3)
user_age = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                 fg="#FFA41B")
user_age.place(x=165, y=128)
user_age.insert(0, "19")
user_age.config(state="readonly")

address = Label(match_user_info, text="Address", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
address.place(x=15, y=185)
user_info.create_line(10, 205, 220, 205, fill="#164B60", width=3)
user_address = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                     fg="#FFA41B")
user_address.place(x=165, y=185)
user_address.insert(0, "Ulaanbaatar")
user_address.config(state="readonly")

gender = Label(match_user_info, text="I'm a", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
gender.place(x=15, y=240)
user_info.create_line(10, 260, 220, 260, fill="#164B60", width=3)
user_gender = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                    fg="#FFA41B")
user_gender.place(x=165, y=240)
user_gender.insert(0, "Male")
user_gender.config(state="readonly")

seeking = Label(match_user_info, text="Looking for ", font=(
    "Ariel", 17, "bold"), bg="#DB005C", fg="#3AA6B9")
seeking.place(x=15, y=295)
user_info.create_line(10, 312, 220, 312, fill="#164B60", width=3)
user_seeking = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#DB005C",
                     fg="#FFA41B")
user_seeking.place(x=165, y=295)
user_seeking.insert(0, "Female")
user_seeking.config(state="readonly")

# creating Entries to display user_interest and a scrollbar
user_interest = LabelFrame(
    match_user_frame, width=220, height=365, bg="blue", borderwidth=0)
user_interest.place(x=830, y=70)

scrollbar = Scrollbar(user_interest)
scrollbar.place(x=80, y=0, height=200)

mylist = Listbox(user_interest, font=("Arial", 17),
                 yscrollcommand=scrollbar.set, relief="flat", bg="#DB005C")
for line in range(100):
    mylist.insert(END, "This is line number " + str(line))

mylist.place(x=0, y=0, width=220, height=380)
scrollbar.config(command=mylist.yview)

# Creating back button to go back to match_list
btn_match_back = ImageTk.PhotoImage(Image.open("Icons/back-arrow.png"))
back_match_btn = Button(match_user_frame, image=btn_match_back, bg="#ADD8E6", relief="flat", borderwidth=0,
                        command=back_list)
back_match_btn.place(x=18, y=13)

# Creating chat button
btn_next_win = ImageTk.PhotoImage(Image.open("Icons/right_aro.png"))

match_chat_btn = Button(match_user_frame, width=42, height=38, image=btn_next_win, bg="#ADD8E6", relief="flat",
                        borderwidth=0)
match_chat_btn.place(x=524, y=479)

match_album_btn = Button(match_user_frame, width=42, height=38, image=btn_next_win, bg="#ADD8E6", relief="flat",
                         borderwidth=0)
match_album_btn.place(x=759, y=612)

'''
Creating LabelFrame search_frame and adding other widgets for "search" option
'''
search_frame = Frame(app)
search_frame.configure(width=1190, height=745,
                       borderwidth=0, relief='flat', bg='#EEEEEE')
search_frame.pack_propagate()

bg_search = ImageTk.PhotoImage(Image.open('Search/bg_search.png'))
search_bg_label = Label(search_frame, image=bg_search)
search_bg_label.place(x=1, y=-1)
'''
Creating LabelFrame setting_frame and adding other widgets for "setting" option
'''
setting_frame = Frame(app)
setting_frame.configure(width=1188, height=745,
                        bg='#EEEEEE', borderwidth=0, relief='flat')
setting_frame.pack_propagate()

# Creating a labelFrame to put setting_list Label
setting_list_frame = LabelFrame(setting_frame)
setting_list_frame.configure(
    width=294, height=745, bg='#EEEEEE', borderwidth=0, relief='flat')
setting_list_frame.place(x=2, y=-1)

# Adding background image to home_frame
bg_setting = ImageTk.PhotoImage(Image.open('Setting/setting_list.png'))
setting_list_label = Label(setting_list_frame, image=bg_setting)
setting_list_label.place(x=0, y=0)

# Creating frame to keep each tab content
setting_window_frame = LabelFrame(setting_frame)
setting_window_frame.configure(
    width=883, height=745, bg='#EEEEEE', borderwidth=0, relief='flat')
setting_window_frame.place(x=298, y=-1)

bg_window = ImageTk.PhotoImage(Image.open('Setting/setting_Window.png'))
window_bg_label = Label(setting_window_frame, image=bg_window)
window_bg_label.place(x=0, y=0)


def hide_frames(show_frame):
    frames = [home_frame, profile_frame, chat_frame,
              match_frame, search_frame, setting_frame]
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

# Creating and placing ???profile???
profile_image = Image.open('images/profile.png')
resized_profile = profile_image.resize((30, 30))
profile = ImageTk.PhotoImage(resized_profile)
lab_profile = Label(side_bar, image=profile, bg="#B7B7B7")
lab_profile.place(x=20, y=102)
profile_label = Label(side_bar, text="Profile", font=(
    "Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
profile_label.place(x=55, y=110)
lab_profile.bind("<Button-1>", lambda event: show_profile())
profile_label.bind("<Button-1>", lambda event: show_profile())

# Creating and Placing ???home???
home_img = Image.open('images/hodas.png')
resized_home = home_img.resize((30, 30))
home = ImageTk.PhotoImage(resized_home)
lab_home = Label(side_bar, image=home, bg="#B7B7B7")
lab_home.place(x=20, y=35)
home_label = Label(side_bar, text="Home", font=(
    "Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
home_label.place(x=55, y=40)
home_label.bind("<Button-1>", lambda event: show_home())

# Creating and Placing ???Chat???
chat_image = Image.open("images/speak.png")
resized_chat = chat_image.resize((30, 30))
chat = ImageTk.PhotoImage(resized_chat)
lab_chat = Label(side_bar, image=chat, bg="#B7B7B7")
lab_chat.place(x=20, y=173)
chat_label = Label(side_bar, text="Chat", font=(
    "Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
chat_label.place(x=55, y=180)
chat_label.bind("<Button-1>", lambda event: show_chat())

# Creating and Placing ???Matches???
match_image = Image.open("images/hearts.png")
resized_heart = match_image.resize((30, 30))
match = ImageTk.PhotoImage(resized_heart)
lab_heart = Label(side_bar, image=match, bg="#B7B7B7")
lab_heart.place(x=20, y=245)
match_label = Label(side_bar, text="Matches", font=(
    "Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
match_label.place(x=55, y=250)
match_label.bind("<Button-1>", lambda event: show_matches())

# Creating and Placing ???search???
search_image = Image.open("images/seo.png")
resized_search = search_image.resize((30, 30))
search = ImageTk.PhotoImage(resized_search)
lab_search = Label(side_bar, image=search, bg="#B7B7B7")
lab_search.place(x=20, y=315)
search_label = Label(side_bar, text="Search", font=(
    "Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
search_label.place(x=55, y=320)
search_label.bind("<Button-1>", lambda event: show_search())

# Creating and Placing ???setting???
setting_image = Image.open("images/setting_gear.png")
resized_setting = setting_image.resize((30, 30))
setting = ImageTk.PhotoImage(resized_setting)
lab_setting = Label(side_bar, image=setting, bg="#B7B7B7")
lab_setting.place(x=20, y=530)
setting_label = Label(side_bar, text="Setting", font=(
    "Ariel", 15, "bold"), fg="#F0F0F0", bg="#B7B7B7")
setting_label.place(x=55, y=530)
setting_label.bind("<Button-1>", lambda event: show_settings())

app.mainloop()
