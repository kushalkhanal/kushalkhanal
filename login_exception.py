import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# from datetime import date

global listbox
global selected_listbox
global listbox2
global selected_listbox2

global frame1
global frame2
global frame3
global frame4

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
    # try:
    #     username_entry.get() ==
    frame3.place_forget()
    frame4.place(x=0, y=0)
    frame4.pack_propagate()


def before2():
    frame3.place_forget()
    frame2.place(x=0, y=0)
    frame2.pack_propagate()


def before3():
    frame4.place_forget()
    frame3.place(x=0, y=0)
    frame3.pack_propagate()


def home_page():
    signin.destroy()
    messagebox.showinfo("You have successfully logged in. 'Welcome!!!'")


def signup():
    global Password_entry
    global eye1
    global eye
    global eye2
    global listbox
    global selected_listbox
    global listbox2
    global selected_listbox2

    global frame1
    global frame2
    global frame3
    global frame4

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

    Date_Of_Birth = Label(frame1, text="Birth Date", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Date_Of_Birth.place(x=120, y=450)
    Date_Of_Birth_entry = Entry(frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    Date_Of_Birth_entry.place(x=300, y=450)
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
    username_entry = Entry(frame2, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    username_entry.place(x=300, y=250)
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
    Gender = Label(frame3, text="Gender", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Gender.place(x=120, y=250)

    genders = ["Male", "Female", "Other"]
    gender_var = StringVar(frame3)
    gender_var.set(genders[0])  # Set the initial selected gender

    gender_menu = OptionMenu(frame3, gender_var, *genders)
    gender_menu.place(x=350, y=250)

    Seeking = Label(frame3, text="Seeking", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Seeking.place(x=120, y=350)

    seeking_var = StringVar(frame3)
    seeking_var.set(genders[0])  # Set the initial selected gender

    seeking_menu = OptionMenu(frame3, seeking_var, *genders)
    seeking_menu.place(x=350, y=360)

    Location = Label(frame3, text="Location", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Location.place(x=120, y=450)
    Location_entry = Entry(frame3, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    Location_entry.place(x=300, y=450)
    canvas3.create_line(30, 270, 270, 270, fill="#8294C4", width=3)

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
               'Pubs'
        , 'World Peace', 'Volunteering', 'Ice Cream', 'Jiu-jitsu', 'Skiing', 'Metaverse', 'Swimming',
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
    before_frame3 = ImageTk.PhotoImage(Image.open('login_signup/before_button.png'))
    before_button3 = Button(frame4, image=before_frame3, bg="#DBDFEA", command=before3, borderwidth=0)
    before_button3.place(x=500, y=620)

    tick = (Image.open('login_signup/tick_mark.png'))
    tick_res = tick.resize((69, 69))
    tick_mark = ImageTk.PhotoImage(tick_res)
    tick_comp = Button(frame4, image=tick_mark, bg="#DBDFEA", command=home_page, borderwidth=0)
    tick_comp.place(x=570, y=620)

    signin.mainloop()


global Password_entry
global eye1
global eye
global eye2


def toggle_password_visibility():
    if Password_entry["show"] == "*":
        Password_entry["show"] = ""
        eye.configure(image=eye1)
    else:
        Password_entry["show"] = "*"
        eye.configure(image=eye2)


login = Tk()
login.configure()
login.title("Match-Maker")
login.geometry("900x560")
login.resizable(False, False)


def Login():
    if username_entry.get() == "admin" and password_entry.get() == "12345":
        # import dashboard as dash
        messagebox.showinfo("Logging in successful")
        login.destroy()

    else:
        messagebox.showerror("Error", "Invalid Password / Username")


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

# Creating signUp Widgets
signUp_button = Button(login_frame, text="Sign Up", fg="#116D6E", bg="lightblue", font=("Ariel", 10, "bold"),
                       borderwidth=0, cursor="heart", command=signup)
signUp_button.place(x=270, y=10)

login_name = Label(login_frame, text="Match-Maker", fg="#F79327", bg="#DB005B", font=("Ariel", 21, "bold"))
# login_name.config(font=("Ariel", 21, "bold"))
login_name.place(x=82, y=100)

login_welcome = Label(login_frame, text="The dating login that's more than just a swipe")
login_welcome.config(font=("Ariel", 13), fg="#FFE569", bg="#DB005B")
login_welcome.place(x=10, y=160)

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
login_button.place(x=90, y=430, width=170)

login.mainloop()
