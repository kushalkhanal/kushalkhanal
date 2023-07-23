import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

global listbox, selected_listbox, listbox2, selected_listbox2
global frame1, frame2, frame3, frame4, frame5
global signin


def add_selected_option():
    # for kind of partner
    selected_indices = listbox.curselection()
    count1 = len(selected_indices)
    print(count1)
    selected_options = [listbox.get(index) for index in selected_indices]
    for opt in selected_options:
        if opt not in selected_listbox.get(0, END):
            selected_listbox.insert(END, opt)


def add_selected_option2():
    selected_indices = listbox2.curselection()
    # for kind of hobbies
    count2 = len(selected_indices)
    print(count2)
    selected_options = [listbox2.get(index) for index in selected_indices]
    for opt in selected_options:
        if opt not in selected_listbox2.get(0, END):
            selected_listbox2.insert(END, opt)


def next1():
    frame1.place_forget()
    frame2.place(x=0, y=0)
    frame2.pack_propagate()


def next2():
    frame2.place_forget()
    frame3.place(x=0, y=0)
    frame3.pack_propagate()


def before1():
    frame2.place_forget()
    frame1.place(x=0, y=0)
    frame1.pack_propagate()


def next3():
    frame3.place_forget()
    frame4.place(x=0, y=0)
    frame4.pack_propagate()


def before2():
    frame3.place_forget()
    frame2.place(x=0, y=0)
    frame2.pack_propagate()


def next4():
    frame4.place_forget()
    frame5.place(x=0, y=0)
    frame5.pack_propagate()


def before3():
    frame4.place_forget()
    frame3.place(x=0, y=0)
    frame3.pack_propagate()


def before4():
    frame5.place_forget()
    frame4.place(x=0, y=0)
    frame4.pack_propagate()


def login_home():
    signin.destroy()
    messagebox.showinfo("You have successfully logged in. 'Welcome!!!'")


def toggle_password_visibility():
    if Password_entry["show"] == "*":
        Password_entry["show"] = ""
        eye.configure(image=eye1)
    else:
        Password_entry["show"] = "*"
        eye.configure(image=eye2)


def signup():
    global Password_entry, eye1, eye, eye2
    global listbox, selected_listbox, listbox2, selected_listbox2
    global frame1, frame2, frame3, frame4, frame5
    global signin

    signin = tkinter.Toplevel()
    signin.geometry('670x735')
    signin.resizable(False, False)

    # current_date = date.today()

    # Creating first frames for signUp
    frame1 = LabelFrame(signin, width=670, height=735, relief='flat')
    frame1.place(x=0, y=0)
    frame1.pack_propagate()

    # Adding login_frame image
    image1 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
    image1_label = Label(frame1, image=image1)
    image1_label.place(x=-4, y=-5)

    # sign_up label widget
    signup1 = Label(frame1, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup1.place(x=220, y=30)

    # Creating canvas for line
    canvas1 = Canvas(frame1, width=300, height=300, bg="#DBDFEA", highlightthickness=0)
    canvas1.place(x=260, y=210)

    # Creating widgets (Label, Entry, Canvas=>line) be placed in "frame1"
    firstname = Label(frame1, text="first Name", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    firstname.place(x=120, y=250)
    firstname_entry = Entry(frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    firstname_entry.place(x=300, y=250)
    canvas1.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

    lastname = Label(frame1, text="last Name", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    lastname.place(x=120, y=350)
    lastname_entry = Entry(frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    lastname_entry.place(x=300, y=350)
    canvas1.create_line(30, 170, 270, 170, fill="#8294C4", width=3)

    date_Of_Birth = Label(frame1, text="Birth Date", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    date_Of_Birth.place(x=120, y=450)
    date_Of_Birth_entry = Entry(frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    date_Of_Birth_entry.place(x=300, y=450)
    canvas1.create_line(30, 270, 270, 270, fill="#8294C4", width=3)

    # Creating second frames for signUp
    frame2 = LabelFrame(signin, width=670, height=735, relief='flat')

    # Adding login_frame image
    image2 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
    image2_label = Label(frame2, image=image2)
    image2_label.place(x=-4, y=-5)

    # sign_up label widget
    signup2 = Label(frame2, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup2.place(x=220, y=30)

    # Creating canvas for line
    canvas2 = Canvas(frame2, width=300, height=300, bg="#DBDFEA", highlightthickness=0)
    canvas2.place(x=260, y=210)

    # Creating widgets (Label, Entry, Canvas=>line) be placed in "frame1"
    username = Label(frame2, text="Username", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    username.place(x=120, y=250)
    usernameentry = Entry(frame2, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    usernameentry.place(x=300, y=250)
    canvas2.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

    mail_id = Label(frame2, text="E-mail", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    mail_id.place(x=120, y=350)
    mail_id_entry = Entry(frame2, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    mail_id_entry.place(x=300, y=350)
    canvas2.create_line(30, 170, 270, 170, fill="#8294C4", width=3)

    Password = Label(frame2, text="Password", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Password.place(x=120, y=450)
    Password_entry = Entry(frame2, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6', show='*')
    Password_entry.place(x=300, y=450)
    canvas2.create_line(30, 270, 270, 270, fill="#8294C4", width=3)

    eye1 = ImageTk.PhotoImage(Image.open('login_signup/eye.png'))
    eye2 = ImageTk.PhotoImage(Image.open('login_signup/invisible.png'))

    eye = Label(frame2, image=eye2, bg='#DBDFEA', cursor="hand2")
    eye.place(x=530, y=450)
    eye.bind("<Button-1>", lambda event: toggle_password_visibility())

    # Creating third frames for signUp
    frame3 = LabelFrame(signin, width=670, height=735, relief='flat')

    # Adding login_frame image
    image3 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
    image3_label = Label(frame3, image=image3)
    image3_label.place(x=-4, y=-5)

    # sign_up label widget
    signup3 = Label(frame3, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup3.place(x=220, y=30)

    # Creating canvas for line
    canvas3 = Canvas(frame3, width=300, height=300, bg="#DBDFEA", highlightthickness=0)
    canvas3.place(x=260, y=210)

    # Creating widgets (Label, Entry, Canvas=>line) be placed in "frame1"
    genders = ["Male", "Female", "Other"]
    gender_var = StringVar()
    gender_var.set(genders[0])  # Setting initial selected gender

    seeking_var = StringVar()
    seeking_var.set(genders[1])  # Setting initial selected seeking gender

    # Creating widgets using Radiobutton
    Gender = Label(frame3, text="Gender", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Gender.place(x=120, y=250)

    for idx, gender in enumerate(genders):
        gender_radio = Radiobutton(frame3, text=gender, variable=gender_var, value=gender)
        gender_radio.place(x=350, y=250 + idx * 30)

    Seeking = Label(frame3, text="Seeking", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Seeking.place(x=120, y=350)

    for idx, gender in enumerate(genders):
        seeking_radio = Radiobutton(frame3, text=gender, variable=seeking_var, value=gender)
        seeking_radio.place(x=350, y=360 + idx * 30)

    Location = Label(frame3, text="Location", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Location.place(x=120, y=470)
    Location_entry = Entry(frame3, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    Location_entry.place(x=300, y=470)
    canvas3.create_line(30, 290, 270, 290, fill="#8294C4", width=3)

    # Creating fourth frames for signUp
    frame4 = LabelFrame(signin, width=670, height=735, relief='flat')

    # Adding login_frame image
    image4 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
    image4_label = Label(frame4, image=image4)
    image4_label.place(x=-4, y=-5)

    # sign_up label widget
    signup4 = Label(frame4, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup4.place(x=220, y=30)

    personality = Label(frame4, text="What kind of Partner you want?")
    hobby = Label(frame4, text="What are your our hobbies / interests?")
    personality.place(x=100, y=150)
    hobby.place(x=380, y=150)

    personalities = ['cheerful', 'honest', 'adaptable', 'affectionate', 'reserved', 'domestic', 'humorous',
                     'natural', 'serious', 'empathetic', 'spirited', 'frugal', 'nature-loving', 'optimistic', 'sporty',
                     'capable', 'fond of children', 'self-disciplined', 'attractive', 'warm-hearted', 'educated',
                     'ethical',
                     'well-mannered', 'thoughtful', 'independent', 'tolerant', 'spontaneous', 'self-assured',
                     'imaginative',
                     'career-driven', 'reliable', 'domestic', 'nature loving']

    hobbies = ['Jogging', 'Equestrian', 'Ice Skating', 'Broadway', 'Trap Music', 'Pig Roast', 'Country Music', 'Cars',
               'Pentathlon', 'Songwriter', 'Rollerskating', '90s Kid', 'Active Lifestyle', 'Content Creation',
               'Cosplay',
               'K-Pop', 'Exchange Program', 'Musical Instrument', 'Investing', 'Social Media', 'Travel',
               'Skateboarding',
               'Memes', 'Rugby', 'NFTS', 'Tango', 'NBA', 'Hot Springs', 'DIY', 'Exhibition', 'Marvel', 'Rock', 'Disney',
               'Environmental Protection', 'Art', 'Soccer', 'Cricket', 'Catan', 'Dancing', 'Harry Potter', 'Archery',
               'Pubs', 'World Peace', 'Volunteering', 'Ice Cream', 'Jiu-jitsu', 'Skiing', 'Metaverse', 'Swimming',
               'Binge-Watching TV shows', 'Comedy', 'Funk music', 'BTS', 'Paragliding', 'Jogging', 'Equestrian',
               'Ice Skating', 'Gym', 'House Parties', 'Surfing', 'Poetry', 'Coffee', 'Car Racing', 'Indoor Activities',
               'Gymnastics', 'Climbing', 'Podcasts', 'Jet-ski', 'Sushi', 'Snowboarding', 'Killing time', 'Crossfit',
               'Freelance', 'Blogging', 'Virtual Reality', 'Musical Writing', 'Martial Arts', 'Walking Tour',
               'Instagram',
               'Brunch', 'Entrepreneurship', 'Shopping', 'Pub Quiz', 'Film Festival', 'Running', 'Festivals',
               'Pole Dancing', 'Sci-Fi', 'Walking', 'Football', 'Fishing', 'Gardening', 'Fashion', 'Korean Food',
               'Artistic Gymnastics',
               'Trying New Things', 'Canoeing', 'Anime', 'Xbox', 'Social Development', 'Bar Hopping', 'Start ups',
               'Bollywood', 'Language Exchange', 'Trivia', 'Literature', 'Motorcycling', 'Sauna', 'Coffee Stall',
               'Electronic Music', 'Art Galleries', 'Among Us', 'Twitch', 'Netflix', 'Expositions', 'Motorcycles',
               'Real Estate', 'Drummer', 'Meditation', 'Clubbing', 'Picnicking', 'Sneakers', 'Baking', 'Hip Hop',
               'Theater',
               'Skincare', 'Pho', '90s Brit-pop', 'E-Sports', 'Up-cycling', 'Capella', 'Sailing', 'Road Trips',
               'Ballet',
               'Singing', 'Dungeons & Dragons', 'Hot Yoga', 'Rock Climbing', 'Cafe hopping', 'Fencing',
               'Motorbike Racing',
               'Bar Chilling', 'Tea', 'Working out', 'Inline Skate', 'Stand up Comedy', 'Manga', 'Band', 'Tarot',
               'Cooking',
               'Drawing', 'Concerts', 'Pinterest', 'Hiking', 'Wine', 'Politics', 'Baseball', 'YouTube', 'Outdoors',
               'Escape Cafe', 'Karaoke', 'Drive Thru Cinema', 'Movies', 'Cheerleading', 'Yoga', 'Board Games',
               'Free Diving', 'Astrology', 'Cycling', 'Volleyball', 'Boba tea', 'Writing', 'Online Games',
               'Battle Ground',
               'Music', 'PlayStation', 'Nightlife', 'Horror Movies', 'Tattoos', 'Weightlifting', 'Aquarium', 'Fortnite',
               'Bowling', 'League of Legends', 'Vegan Cooking', 'Spa', 'Heavy Metal', 'Reading', 'Street Food',
               'Marathon',
               'West End Musicals', 'Investment', 'Motor Sports', 'Pilates', 'Sports', 'Boxing', 'Parties', 'Shashi',
               'Beach Tennis', 'Basketball', 'Town Festivities', 'Home Workout', 'Walking Dog', 'Camping', 'Blackpink',
               'Stock Exchange', 'Military', 'Guitarists', 'Mountains', 'Sake', 'Voter Rights', 'Online Shopping',
               'Choir',
               'Painting', 'Foodie Tour', 'Hockey', 'Samba', 'Museum', 'Wrestling', 'Live Music', 'Vintage fashion',
               'Photography', 'Saxophonist', 'Climate Change', 'Youth Empowerment', 'Beach Bars', 'Vlogging']

    # Creating first set of listbox and scrollbar
    listbox = Listbox(frame4, selectmode=MULTIPLE, width=25)
    scrollbar1 = Scrollbar(frame4, orient=VERTICAL, command=listbox.yview)
    listbox.configure(yscrollcommand=scrollbar1.set)
    for option in personalities:
        listbox.insert(END, option)
    listbox.place(x=100, y=200)
    scrollbar1.place(x=230, y=202, height=160)

    button = Button(frame4, text="Add Selected personalities", command=add_selected_option)
    button.place(x=100, y=380)

    selected_listbox = Listbox(frame4)
    scrollbar2 = Scrollbar(frame4, orient=VERTICAL, command=selected_listbox.yview)
    selected_listbox.configure(yscrollcommand=scrollbar2.set)
    selected_listbox.place(x=100, y=430, width=160)
    scrollbar2.place(x=235, y=432, height=160)

    # Creating second set of listbox and scrollbar
    listbox2 = Listbox(frame4, selectmode=MULTIPLE, width=25)
    scrollbar3 = Scrollbar(frame4, orient=VERTICAL, command=listbox2.yview)
    listbox2.configure(yscrollcommand=scrollbar3.set)
    for option in hobbies:
        listbox2.insert(END, option)
    listbox2.place(x=400, y=200)
    scrollbar3.place(x=530, y=202, height=160)

    button2 = Button(frame4, text="Add Selected hobbies", command=add_selected_option2)
    button2.place(x=400, y=380)

    selected_listbox2 = Listbox(frame4)
    scrollbar4 = Scrollbar(frame4, orient=VERTICAL, command=selected_listbox2.yview)
    selected_listbox2.configure(yscrollcommand=scrollbar4.set)
    selected_listbox2.place(x=400, y=430, width=160)
    scrollbar4.place(x=535, y=432, height=160)

    # '''Creating a frame 5 for user to input at least 3 images and a tick butom to confirm account creation'''
    frame5 = LabelFrame(signin, width=670, height=735, relief='flat')
    frame5.pack_propagate()

    # Adding login_frame image
    image5 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
    image5_label = Label(frame5, image=image5)
    image5_label.place(x=-4, y=-5)

    # sign_up label widget
    signup5 = Label(frame5, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup5.place(x=220, y=30)

    # Creating place for adding images
    label1 = Label(frame5, text="Get started with 3 of your recent pictures", font=("Ariel", 20, "bold"), bg="#DBDFEA")
    label1.place(x=70, y=130)

    # Creating next_frame button for frame1
    next_frame1 = ImageTk.PhotoImage(Image.open('login_signup/next_button.png'))
    next_button1 = Button(frame1, image=next_frame1, bg="#DBDFEA", command=next1, borderwidth=0)
    next_button1.place(x=570, y=620)

    # Creating next_frame button for frame2
    before_frame1 = ImageTk.PhotoImage(Image.open('login_signup/before_button.png'))
    before_button1 = Button(frame2, image=before_frame1, bg="#DBDFEA", command=before1, borderwidth=0)
    before_button1.place(x=500, y=620)

    next_frame2 = ImageTk.PhotoImage(Image.open('login_signup/next_button.png'))
    next_button2 = Button(frame2, image=next_frame2, bg="#DBDFEA", command=next2, borderwidth=0)
    next_button2.place(x=570, y=620)

    # Creating next_frame button for frame3
    before_frame2 = ImageTk.PhotoImage(Image.open('login_signup/before_button.png'))
    before_button2 = Button(frame3, image=before_frame2, bg="#DBDFEA", command=before2, borderwidth=0)
    before_button2.place(x=500, y=620)

    next_frame3 = ImageTk.PhotoImage(Image.open('login_signup/next_button.png'))
    next_button3 = Button(frame3, image=next_frame3, bg="#DBDFEA", command=next3, borderwidth=0)
    next_button3.place(x=570, y=620)

    # Creating next_frame button for frame4
    next_frame4 = ImageTk.PhotoImage(Image.open('login_signup/next_button.png'))
    next_button4 = Button(frame4, image=next_frame4, bg="#DBDFEA", command=next4, borderwidth=0)
    next_button4.place(x=570, y=620)

    before_frame3 = ImageTk.PhotoImage(Image.open('login_signup/before_button.png'))
    before_button3 = Button(frame4, image=before_frame3, bg="#DBDFEA", command=before3, borderwidth=0)
    before_button3.place(x=500, y=620)

    # Creating before_frame button for frame5
    before_frame4 = ImageTk.PhotoImage(Image.open('login_signup/before_button.png'))
    before_button4 = Button(frame5, image=before_frame4, bg="#DBDFEA", command=before4, borderwidth=0)
    before_button4.place(x=500, y=620)

    tick = (Image.open('login_signup/tick_mark.png'))
    tick_res = tick.resize((69, 69))
    tick_mark = ImageTk.PhotoImage(tick_res)
    tick_comp = Button(frame5, image=tick_mark, bg="#DBDFEA", command=login_home, borderwidth=0)
    tick_comp.place(x=570, y=620)

    signin.mainloop()


def home_page():
    app = Tk()
    w = app.winfo_screenwidth()
    h = app.winfo_screenheight()
    app.geometry(str(w) + "x" + str(h))
    app.resizable(False, False)
    app.state("zoomed")

    # Media icons
    facebook1 = (Image.open("Icons/facebook.png"))
    messenger1 = (Image.open("Icons/messenger.png"))
    instagram1 = (Image.open("Icons/instagram.png"))
    twitter1 = (Image.open("Icons/twitter.png"))
    snapchat1 = (Image.open("Icons/snapchat.png"))
    whatsapp1 = (Image.open("Icons/whatsapp.png"))

    r_facebook = facebook1.resize((50, 50))
    r_messenger = messenger1.resize((50, 50))
    r_instagram = instagram1.resize((50, 50))
    r_twitter = twitter1.resize((50, 50))
    r_snapchat = snapchat1.resize((50, 50))
    r_whatsapp = whatsapp1.resize((50, 50))

    facebook = ImageTk.PhotoImage(r_facebook)
    messenger = ImageTk.PhotoImage(r_messenger)
    instagram = ImageTk.PhotoImage(r_instagram)
    twitter = ImageTk.PhotoImage(r_twitter)
    snapchat = ImageTk.PhotoImage(r_snapchat)
    whatsapp = ImageTk.PhotoImage(r_whatsapp)

    '''Creating a logo_frame'''
    logo_frame = LabelFrame(app, width=205, height=105, borderwidth=0, relief="flat")
    logo_frame.place(x=0, y=0)

    i1 = ImageTk.PhotoImage(Image.open('trial/a1.png'))
    l1 = Label(logo_frame, image=i1)
    l1.place(x=0, y=0)

    '''Creating a LabelFrame.---sidebar---'''
    side_bar = LabelFrame(app, width=205, height=650, borderwidth=0, relief="flat")
    side_bar.place(x=0, y=107)

    i2 = ImageTk.PhotoImage(Image.open('trial/a2.png'))
    l2 = Label(side_bar, image=i2)
    l2.place(x=0, y=0)

    '''
    Creating LabelFrame home_frame and adding other widgets for "home" option
    This includes all a image viewer user info, type of relationship, interest and hobbies and social media.
    '''
    home_frame = LabelFrame(app)
    home_frame.configure(width=1188, height=745, borderwidth=0, relief='flat')
    home_frame.pack_propagate()

    # Adding background image to home_frame
    bg_home = ImageTk.PhotoImage(Image.open('Home/home_final.png'))
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

    # Adding Social Media icons
    facebook_btn = Button(home_frame, image=facebook)
    messenger_btn = Button(home_frame, image=messenger)
    instagram_btn = Button(home_frame, image=instagram)
    twitter_btn = Button(home_frame, image=twitter)
    snapchat_btn = Button(home_frame, image=snapchat)
    whatsapp_btn = Button(home_frame, image=whatsapp)

    facebook_btn.place(x=510, y=140)
    messenger_btn.place(x=590, y=140)
    instagram_btn.place(x=670, y=140)
    twitter_btn.place(x=750, y=140)
    snapchat_btn.place(x=830, y=140)
    whatsapp_btn.place(x=910, y=140)

    # '''Creating Entries to display user info'''
    user_info = Canvas(home_frame, width=230, height=330, bg="#FCE9F1", highlightthickness=0)
    user_info.place(x=640, y=240)

    username = Label(home_frame, text="Username", font=("Arial", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    username.place(x=500, y=250)
    user_info.create_line(10, 45, 220, 45, fill="#164B60", width=3)
    user_username = Entry(home_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                          fg="#FFA41B")
    user_username.place(x=650, y=250)
    user_username.insert(0, "Raul05dxfcgvhjjrxtcfyvgbhrdxfcvghjb")
    user_username.config(state="readonly")

    name = Label(home_frame, text="Name", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    name.place(x=500, y=305)
    user_info.create_line(10, 95, 220, 95, fill="#164B60", width=3)
    user_name = Entry(home_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1", fg="#FFA41B")
    user_name.place(x=650, y=300)
    user_name.insert(0, "Rasuoboac ad")
    user_name.config(state="readonly")

    age = Label(home_frame, text="Age", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    age.place(x=500, y=360)
    user_info.create_line(10, 150, 220, 150, fill="#164B60", width=3)
    user_age = Entry(home_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1", fg="#FFA41B")
    user_age.place(x=650, y=355)
    user_age.insert(0, "19")
    user_age.config(state="readonly")

    address = Label(home_frame, text="Address", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    address.place(x=500, y=415)
    user_info.create_line(10, 205, 220, 205, fill="#164B60", width=3)
    user_address = Entry(home_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                         fg="#FFA41B")
    user_address.place(x=650, y=410)
    user_address.insert(0, "Ulaanbaatar")
    user_address.config(state="readonly")

    gender = Label(home_frame, text="I'm a", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    gender.place(x=500, y=470)
    user_info.create_line(10, 260, 220, 260, fill="#164B60", width=3)
    user_gender = Entry(home_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                        fg="#FFA41B")
    user_gender.place(x=650, y=465)
    user_gender.insert(0, "Male")
    user_gender.config(state="readonly")

    seeking = Label(home_frame, text="Looking for ", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    seeking.place(x=500, y=525)
    user_info.create_line(10, 312, 220, 312, fill="#164B60", width=3)
    user_seeking = Entry(home_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                         fg="#FFA41B")
    user_seeking.place(x=650, y=520)
    user_seeking.insert(0, "Female")
    user_seeking.config(state="readonly")

    # creating Entries to display user_interest and a scrollbar
    user_interest = LabelFrame(home_frame, width=220, height=365, bg="blue", borderwidth=0)
    user_interest.place(x=920, y=226)

    scrollbar = Scrollbar(user_interest)
    scrollbar.place(x=80, y=0, height=200)

    mylist = Listbox(user_interest, font=("Arial", 17), yscrollcommand=scrollbar.set, relief="flat", bg="#FCE9F1")
    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))

    mylist.place(x=0, y=0, width=220, height=380)
    scrollbar.config(command=mylist.yview)

    '''
    Creating Frame profile_frame and adding other widgets for "profile" option
    '''
    profile_frame = Frame(app)
    profile_frame.configure(width=1188, height=745, borderwidth=0, relief='flat')
    profile_frame.pack_propagate()

    # Adding background image to home_frame
    bg_profile = ImageTk.PhotoImage(Image.open('Profile/profile_Mask.png'))
    profile_bg_label = Label(profile_frame, image=bg_profile)
    profile_bg_label.place(x=1, y=-1)

    # Adding profile image
    profile_img = Image.open("Home/girlph.jpg")
    profile_img_res = profile_img.resize((345, 568))
    profile_img_tk = ImageTk.PhotoImage(profile_img_res)
    profile_label = Label(profile_frame, image=profile_img_tk)
    profile_label.image = girl_image_tk  # Keep a reference to prevent garbage collection
    profile_label.place(x=35, y=32)

    # '''Creating a multiline widget to put user preferred relation type'''
    relation_type = Text(profile_frame, height=6, width=10, font=("Ariel", 16), bg="#FCE9F1", relief="flat")
    relation_type.place(x=520, y=50)

    insert_type = """
       Looking 
         for
      Long-term 
       Partner
    """
    relation_type.insert(END, insert_type)
    relation_type.config(state=DISABLED)

    # Creating social-media buttons
    facebook_btn11 = Button(profile_frame, image=facebook)
    messenger_btn11 = Button(profile_frame, image=messenger)
    instagram_btn11 = Button(profile_frame, image=instagram)
    twitter_btn11 = Button(profile_frame, image=twitter)
    snapchat_btn11 = Button(profile_frame, image=snapchat)
    whatsapp_btn11 = Button(profile_frame, image=whatsapp)

    facebook_btn11.place(x=399, y=52)
    messenger_btn11.place(x=399, y=125)
    instagram_btn11.place(x=399, y=199)
    twitter_btn11.place(x=399, y=274)
    snapchat_btn11.place(x=399, y=350)
    whatsapp_btn11.place(x=399, y=424)

    # arrows for a frame
    right_arrow = ImageTk.PhotoImage(Image.open("Icons/right_aro.png"))
    right_btn1 = Button(profile_frame, image=right_arrow, bg="#ADD8E6", width=45, height=30, cursor="circle",
                        relief="flat", borderwidth=0)
    right_btn1.place(x=1007, y=554)

    left_arrow = ImageTk.PhotoImage(Image.open("Icons/left_aro.png"))
    left_btn1 = Button(profile_frame, image=left_arrow, bg="#ADD8E6", width=45, height=30, cursor="circle",
                       relief="flat", borderwidth=0)
    left_btn1.place(x=897, y=456)

    # '''Creating Entries to display user info'''
    user_info = Canvas(profile_frame, width=230, height=330, bg="#FCE9F1", highlightthickness=0)
    user_info.place(x=630, y=250)

    username = Label(profile_frame, text="Username", font=("Arial", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    username.place(x=490, y=260)
    user_info.create_line(10, 45, 220, 45, fill="#164B60", width=3)
    user_username = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                          fg="#FFA41B")
    user_username.place(x=640, y=260)
    user_username.insert(0, "Raul05dxfcgvhjjrxtcfyvgbhrdxfcvghjb")
    user_username.config(state="readonly")

    name = Label(profile_frame, text="Name", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    name.place(x=490, y=315)
    user_info.create_line(10, 95, 220, 95, fill="#164B60", width=3)
    user_name = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                      fg="#FFA41B")
    user_name.place(x=640, y=310)
    user_name.insert(0, "Rasuoboac ad")
    user_name.config(state="readonly")

    age = Label(profile_frame, text="Age", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    age.place(x=490, y=370)
    user_info.create_line(10, 150, 220, 150, fill="#164B60", width=3)
    user_age = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                     fg="#FFA41B")
    user_age.place(x=640, y=365)
    user_age.insert(0, "19")
    user_age.config(state="readonly")

    address = Label(profile_frame, text="Address", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    address.place(x=490, y=425)
    user_info.create_line(10, 205, 220, 205, fill="#164B60", width=3)
    user_address = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                         fg="#FFA41B")
    user_address.place(x=640, y=420)
    user_address.insert(0, "Ulaanbaatar")
    user_address.config(state="readonly")

    gender = Label(profile_frame, text="I'm a", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    gender.place(x=490, y=480)
    user_info.create_line(10, 260, 220, 260, fill="#164B60", width=3)
    user_gender = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                        fg="#FFA41B")
    user_gender.place(x=640, y=475)
    user_gender.insert(0, "Male")
    user_gender.config(state="readonly")

    seeking = Label(profile_frame, text="Looking for ", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    seeking.place(x=490, y=535)
    user_info.create_line(10, 312, 220, 312, fill="#164B60", width=3)
    user_seeking = Entry(profile_frame, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                         fg="#FFA41B")
    user_seeking.place(x=640, y=530)
    user_seeking.insert(0, "Female")
    user_seeking.config(state="readonly")

    # creating Entries to display user_interest and a scrollbar
    user_interest = LabelFrame(profile_frame, width=220, height=365, bg="blue", borderwidth=0)
    user_interest.place(x=910, y=40)

    scrollbar = Scrollbar(user_interest)
    scrollbar.place(x=80, y=0, height=200)

    mylist = Listbox(user_interest, font=("Arial", 17), yscrollcommand=scrollbar.set, relief="flat", bg="#FCE9F1")
    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))

    mylist.place(x=0, y=0, width=220, height=380)
    scrollbar.config(command=mylist.yview)

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

    userprofile = Canvas(chat_frame, bg="red", height=54, width=54, bd=0, relief="ridge", highlightthickness=0)
    userprofile.place(x=20, y=30)

    user_name = Entry(chat_frame, font=("Ariel", 17), width=14, cursor="circle")
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
    chat_name = Canvas(chat_window, width=200, height=55, bg="#FFFFFF", borderwidth=0, relief='flat')
    chat_name.place(x=18, y=15)

    user_detail = Entry(chat_window, font=("Ariel", 19), width=13, relief="flat")
    user_detail.place(x=25, y=30)
    user_Detail = 'Raul, 19'
    user_detail.insert(END, user_Detail)
    user_detail.config(state=DISABLED)

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

    def match_wind():
        match_user_list.place_forget()
        match_user_frame.place(x=1, y=-1)

    def back_list():
        match_user_frame.place_forget()
        match_user_list.place(x=1, y=-1)

    # Creating labelFrame for below chat_list
    match_user_list = LabelFrame(match_frame)
    match_user_list.configure(width=290, height=745, borderwidth=0, relief='flat')
    match_user_list.place(x=1, y=-1)

    # Adding background image to home_frame
    bg_match = ImageTk.PhotoImage(Image.open('Matches/match_List.png'))
    match_bg_label = Label(match_user_list, image=bg_match)
    match_bg_label.place(x=0, y=0)

    match_profile = Canvas(match_frame, bg="red", height=54, width=54, bd=0, relief="ridge", highlightthickness=0)
    match_profile.place(x=20, y=30)

    match_name = Entry(match_frame, font=("Ariel", 17), width=14, cursor="circle")
    match_name.place(x=80, y=52)
    match_Name = 'Raul054'  # Actual matched username
    match_name.insert(END, match_Name)
    match_name.config(state=DISABLED)
    match_name.bind('<Button-1>', lambda event: match_wind())

    # Now for match window
    match_user_frame = LabelFrame(match_frame)
    match_user_frame.configure(width=1200, height=745, borderwidth=0, relief='flat')

    bg_match_window = ImageTk.PhotoImage(Image.open("Matches/match_Window.png"))
    match_window_label = Label(match_user_frame, image=bg_match_window)
    match_window_label.place(x=0, y=0)

    # Creating social-media buttons
    facebook_btn12 = Button(match_user_frame, image=facebook)
    messenger_btn12 = Button(match_user_frame, image=messenger)
    instagram_btn12 = Button(match_user_frame, image=instagram)
    twitter_btn12 = Button(match_user_frame, image=twitter)
    snapchat_btn12 = Button(match_user_frame, image=snapchat)
    whatsapp_btn12 = Button(match_user_frame, image=whatsapp)

    facebook_btn12.place(x=311, y=63)
    messenger_btn12.place(x=311, y=136)
    instagram_btn12.place(x=311, y=209)
    twitter_btn12.place(x=311, y=282)
    snapchat_btn12.place(x=311, y=353)
    whatsapp_btn12.place(x=311, y=424)

    # '''Creating Entries to display user info'''
    match_user_info = LabelFrame(match_user_frame)
    match_user_info.configure(width=388, height=366, bg="#FCE9F1", borderwidth=0)
    match_user_info.place(x=393, y=65)

    user_info = Canvas(match_user_info, width=230, height=330, bg="#FCE9F1", highlightthickness=0)
    user_info.place(x=150, y=14)

    username = Label(match_user_info, text="Username", font=("Arial", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    username.place(x=15, y=20)
    user_username = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                          fg="#FFA41B")
    user_username.place(x=165, y=20)
    user_username.insert(0, "Raul05dxfcgvhjjrxtcfyvgbhrdxfcvghjb")
    user_username.config(state="readonly")
    user_info.create_line(10, 40, 220, 40, fill="#164B60", width=3)

    name = Label(match_user_info, text="Name", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    name.place(x=15, y=73)
    user_name = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                      fg="#FFA41B")
    user_name.place(x=165, y=73)
    user_name.insert(0, "Rasuoboac ad")
    user_name.config(state="readonly")
    user_info.create_line(10, 95, 220, 95, fill="#164B60", width=3)

    age = Label(match_user_info, text="Age", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    age.place(x=15, y=128)
    user_info.create_line(10, 150, 220, 150, fill="#164B60", width=3)
    user_age = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                     fg="#FFA41B")
    user_age.place(x=165, y=128)
    user_age.insert(0, "19")
    user_age.config(state="readonly")

    address = Label(match_user_info, text="Address", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    address.place(x=15, y=185)
    user_info.create_line(10, 205, 220, 205, fill="#164B60", width=3)
    user_address = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                         fg="#FFA41B")
    user_address.place(x=165, y=185)
    user_address.insert(0, "Ulaanbaatar")
    user_address.config(state="readonly")

    gender = Label(match_user_info, text="I'm a", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    gender.place(x=15, y=240)
    user_info.create_line(10, 260, 220, 260, fill="#164B60", width=3)
    user_gender = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                        fg="#FFA41B")
    user_gender.place(x=165, y=240)
    user_gender.insert(0, "Male")
    user_gender.config(state="readonly")

    seeking = Label(match_user_info, text="Looking for ", font=("Ariel", 17, "bold"), bg="#FCE9F1", fg="#3AA6B9")
    seeking.place(x=15, y=295)
    user_info.create_line(10, 312, 220, 312, fill="#164B60", width=3)
    user_seeking = Entry(match_user_info, width=18, font="Arial, 15", borderwidth=0, readonlybackground="#FCE9F1",
                         fg="#FFA41B")
    user_seeking.place(x=165, y=295)
    user_seeking.insert(0, "Female")
    user_seeking.config(state="readonly")

    # creating Entries to display user_interest and a scrollbar
    user_interest = LabelFrame(match_user_frame, width=220, height=365, bg="blue", borderwidth=0)
    user_interest.place(x=830, y=70)

    scrollbar = Scrollbar(user_interest)
    scrollbar.place(x=80, y=0, height=200)

    mylist = Listbox(user_interest, font=("Arial", 17), yscrollcommand=scrollbar.set, relief="flat", bg="#FCE9F1")
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
    bg_setting = ImageTk.PhotoImage(Image.open('Setting/setting_list.png'))
    setting_list_label = Label(setting_list_frame, image=bg_setting)
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


def Login():
    if username_entry.get() == "admin" and password_entry.get() == "12345":
        # import dashboard as dash
        login.destroy()
        home_page()
        # messagebox.showinfo("Logging in successful")

    else:
        messagebox.showerror("Error", "Invalid Password / Username")


global Password_entry
global eye1
global eye
global eye2

login = Tk()
login.configure()
login.title("Match-Maker")
login.geometry("902x560")
login.resizable(False, False)

# Creating First frame
image_frame = Frame(bg="#B7B7B7")
image_frame.config(height=560, width=545)
image_frame.place(x=3, y=0)

image_frame_background = ImageTk.PhotoImage(Image.open('login_signup/login_image12.png'))
login_background_label = Label(image_frame, image=image_frame_background)
login_background_label.place(x=0, y=0)

# ##############################################
# Creating Second frame
login_frame = Frame(bg="#B7B7B7")
login_frame.config(height=950, width=348)
login_frame.place(x=551, y=0)

input_frame_background = ImageTk.PhotoImage(Image.open('login_signup/login_input_frame.png'))
input_background_label = Label(login_frame, image=input_frame_background)
input_background_label.place(x=0, y=0)

# Creating signUp, login, entry Widgets
login_name = Label(login_frame, text="Match-Maker", fg="#F79327", bg="#DB005B", font=("Ariel", 35, "bold"))
# login_name.config(font=("Ariel", 21, "bold"))
login_name.place(x=35, y=80)

login_welcome = Label(login_frame, text="The dating login that's more than just a swipe")
login_welcome.config(font=("Ariel", 11, "bold"), fg="#FFE569", bg="#DB005B")
login_welcome.place(x=10, y=140)

username_label = Label(login_frame, text="User name", font=("Ariel", 10, "bold"), fg="#116D6E", bg="#B7B7B7")
username_label.place(x=70, y=250)
username_entry = Entry(login_frame, fg="#116D6E", borderwidth=0, width=20, font="Ariel, 14",
                       bg="white")  # cursor="heart"
username_entry.place(x=70, y=280)

password_label = Label(login_frame, text="Password", font=("Ariel", 10, "bold"), fg="#116D6E", bg="#B7B7B7")
password_label.place(x=70, y=310)
password_entry = Entry(login_frame, fg="#116D6E", borderwidth=0, width=20, show="*", font="Ariel, 14",
                       bg="white")  # , cursor="heart"
password_entry.place(x=70, y=340)

# Creating a Login Button
login_button = Button(login_frame, text="Login", fg="#116D6E", bg="lightblue", font=("Ariel", 19, "bold"),
                      borderwidth=0, cursor="heart", command=Login)
login_button.place(x=90, y=410, width=170)

# Creating signup button
new_label = Label(login_frame, text="New to Match-Maker?", fg="#F79327", bg="#DB005B", font=("Ariel", 11, "bold"))
new_label.place(x=30, y=470)
signUp_button = Button(login_frame, text="Sign Up", fg="#116D6E", bg="lightblue", font=("Ariel", 8, "bold"),
                       borderwidth=0, cursor="heart", command=signup)
signUp_button.place(x=200, y=470)
now_label = Label(login_frame, text="! NOW !", fg="#F79327", bg="#DB005B", font=("Ariel", 12, "bold"))
now_label.place(x=260, y=470)

login.mainloop()
