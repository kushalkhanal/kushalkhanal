import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from pymongo import MongoClient
import re

client = MongoClient('mongodb://localhost:27017')
database = client['matchmaker']
collection = database['users']


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
    global signin, phone_entry

    signin = tkinter.Toplevel()
    signin.geometry('670x735')
    signin.resizable(False, False)

    def signup_function():
        fname = firstname_entry.get()
        lname = lastname_entry.get()
        dob = date_Of_Birth_entry.get()
        phone = phone_entry.get()
        email = mail_id_entry.get()
        password = password_entry.get()
        gender = gender_var.get()
        seeking = seeking_var.get()
        location = Location_entry.get()
        # if fname == '' or lname == '' or dob == '' or phone == '' or email == '' or password == '' or gender == '' or seeking == '' or location == '':
        #     messagebox.showinfo('Registration', 'No fields can be empty.')
        if collection.find_one({'phone': phone}):
            messagebox.showinfo('Registration', 'This number already exists.')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            messagebox.showinfo('Registration', 'Invalid Email.')
        elif not re.match(r'^\d{10}$', phone):
            messagebox.showinfo('Registration', 'Invalid Number')
        elif len(password) > 7:
            messagebox.showinfo('Registration', 'Weak Password.')
        else:
            collection.insert_one({'First Name': fname, 'Last Name': lastname_entry.get(), "DOB": date_Of_Birth_entry.get(
            ), 'phone': phone_entry.get(), 'email': mail_id_entry.get(), 'password': password_entry.get(), 'gender': gender_var.get(), 'seeking gender': seeking_var.get(), 'location': Location_entry.get()})
            messagebox.showinfo('Registration', 'Registration Successful')

    # Creating first frames for signUp
    frame1 = LabelFrame(signin, width=670, height=735, relief='flat')
    frame1.place(x=0, y=0)
    frame1.pack_propagate()

    # Adding login_frame image
    image1 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
    image1_label = Label(frame1, image=image1)
    image1_label.place(x=-4, y=-5)

    # sign_up label widget
    signup1 = Label(frame1, text="Sign Up", font=(
        'Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup1.place(x=220, y=30)

    # Creating canvas for line
    canvas1 = Canvas(frame1, width=300, height=300,
                     bg="#DBDFEA", highlightthickness=0)
    canvas1.place(x=260, y=210)

    # Creating widgets (Label, Entry, Canvas=>line) be placed in "frame1"
    firstname = Label(frame1, text="first Name", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    firstname.place(x=120, y=250)
    firstname_entry = Entry(
        frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    firstname_entry.place(x=300, y=250)
    canvas1.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

    lastname = Label(frame1, text="last Name", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    lastname.place(x=120, y=350)
    lastname_entry = Entry(frame1, width=20, font='Ariel, 15',
                           borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    lastname_entry.place(x=300, y=350)
    canvas1.create_line(30, 170, 270, 170, fill="#8294C4", width=3)

    date_Of_Birth = Label(frame1, text="Birth Date", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    date_Of_Birth.place(x=120, y=450)
    date_Of_Birth_entry = Entry(
        frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    date_Of_Birth_entry.place(x=300, y=450)
    canvas1.create_line(30, 270, 270, 270, fill="#8294C4", width=3)

    # Creating second frames for signUp
    frame2 = LabelFrame(signin, width=670, height=735, relief='flat')

    # Adding login_frame image
    image2 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
    image2_label = Label(frame2, image=image2)
    image2_label.place(x=-4, y=-5)

    # sign_up label widget
    signup2 = Label(frame2, text="Sign Up", font=(
        'Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup2.place(x=220, y=30)

    # Creating canvas for line
    canvas2 = Canvas(frame2, width=300, height=300,
                     bg="#DBDFEA", highlightthickness=0)
    canvas2.place(x=260, y=210)

    # Creating widgets (Label, Entry, Canvas=>line) be placed in "frame1"
    phone = Label(frame2, text="Phone Number", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    phone.place(x=120, y=250)
    phone_entry = Entry(frame2, width=20, font='Ariel, 15',
                        borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    phone_entry.place(x=300, y=250)
    canvas2.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

    mail_id = Label(frame2, text="E-mail", font=('Ariel', 15),
                    fg="#8294C4", bg="#DBDFEA")
    mail_id.place(x=120, y=350)
    mail_id_entry = Entry(frame2, width=20, font='Ariel, 15',
                          borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    mail_id_entry.place(x=300, y=350)
    canvas2.create_line(30, 170, 270, 170, fill="#8294C4", width=3)

    Password = Label(frame2, text="Password", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Password.place(x=120, y=450)
    Password_entry = Entry(frame2, width=20, font='Ariel, 15',
                           borderwidth=0, bg='#DBDFEA', fg='#ACB1D6', show='*')
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
    signup3 = Label(frame3, text="Sign Up", font=(
        'Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
    signup3.place(x=220, y=30)

    # Creating canvas for line
    canvas3 = Canvas(frame3, width=300, height=300,
                     bg="#DBDFEA", highlightthickness=0)
    canvas3.place(x=260, y=210)

    # Creating widgets (Label, Entry, Canvas=>line) be placed in "frame1"
    genders = ["Male", "Female", "Other"]
    gender_var = StringVar()
    gender_var.set(genders[0])  # Setting initial selected gender

    seeking_var = StringVar()
    seeking_var.set(genders[1])  # Setting initial selected seeking gender

    # Creating widgets using Radiobutton
    Gender = Label(frame3, text="Gender", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Gender.place(x=120, y=250)

    for idx, gender in enumerate(genders):
        gender_radio = Radiobutton(
            frame3, text=gender, variable=gender_var, value=gender)
        gender_radio.place(x=350, y=250 + idx * 30)

    Seeking = Label(frame3, text="Seeking", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Seeking.place(x=120, y=350)

    for idx, gender in enumerate(genders):
        seeking_radio = Radiobutton(
            frame3, text=gender, variable=seeking_var, value=gender)
        seeking_radio.place(x=350, y=360 + idx * 30)

    Location = Label(frame3, text="Location", font=(
        'Ariel', 15), fg="#8294C4", bg="#DBDFEA")
    Location.place(x=120, y=470)
    Location_entry = Entry(frame3, width=20, font='Ariel, 15',
                           borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
    Location_entry.place(x=300, y=470)
    canvas3.create_line(30, 290, 270, 290, fill="#8294C4", width=3)

    # Creating next_frame button for frame1
    next_frame1 = ImageTk.PhotoImage(
        Image.open('login_signup/next_button.png'))
    next_button1 = Button(frame1, image=next_frame1,
                          bg="#DBDFEA", command=next1, borderwidth=0)
    next_button1.place(x=570, y=620)

    # Creating next_frame button for frame2
    before_frame1 = ImageTk.PhotoImage(
        Image.open('login_signup/before_button.png'))
    before_button1 = Button(frame2, image=before_frame1,
                            bg="#DBDFEA", command=before1, borderwidth=0)
    before_button1.place(x=500, y=620)

    next_frame2 = ImageTk.PhotoImage(
        Image.open('login_signup/next_button.png'))
    next_button2 = Button(frame2, image=next_frame2,
                          bg="#DBDFEA", command=next2, borderwidth=0)
    next_button2.place(x=570, y=620)

    # Creating next_frame button for frame3
    before_frame2 = ImageTk.PhotoImage(
        Image.open('login_signup/before_button.png'))
    before_button2 = Button(frame3, image=before_frame2,
                            bg="#DBDFEA", command=before2, borderwidth=0)
    before_button2.place(x=500, y=620)

    tick = (Image.open('login_signup/tick_mark.png'))
    tick_res = tick.resize((69, 69))
    tick_mark = ImageTk.PhotoImage(tick_res)
    tick_comp = Button(frame3, image=tick_mark, bg="#DBDFEA",
                       command=signup_function, borderwidth=0)
    tick_comp.place(x=570, y=620)

    signin.mainloop()


def login_data(phone):
    user = collection.find_one({'phone': phone})
    return user


def Login():
    phone = username_entry.get()
    password = password_entry.get()
    user_data = login_data(phone)
    if user_data:
        password_stored = user_data['password']
        if password_stored == password:
            login.destroy()
            with open("phone.txt", "w") as file:
                file.write(phone)
            import dash_board
            # import dashboard
        else:
            messagebox.showinfo('Login Result', 'Incorrect Password')
    else:
        messagebox.showinfo('Login Result', 'User not found')


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

image_frame_background = ImageTk.PhotoImage(
    Image.open('login_signup/login_image12.png'))
login_background_label = Label(image_frame, image=image_frame_background)
login_background_label.place(x=0, y=0)

# ##############################################
# Creating Second frame
login_frame = Frame(bg="#B7B7B7")
login_frame.config(height=950, width=348)
login_frame.place(x=551, y=0)

input_frame_background = ImageTk.PhotoImage(
    Image.open('login_signup/login_input_frame.png'))
input_background_label = Label(login_frame, image=input_frame_background)
input_background_label.place(x=0, y=0)

# Creating signUp, login, entry Widgets
login_name = Label(login_frame, text="Match-Maker",
                   fg="#F79327", bg="#DB005B", font=("Ariel", 35, "bold"))
# login_name.config(font=("Ariel", 21, "bold"))
login_name.place(x=35, y=80)

login_welcome = Label(
    login_frame, text="The dating login that's more than just a swipe")
login_welcome.config(font=("Ariel", 11, "bold"), fg="#FFE569", bg="#DB005B")
login_welcome.place(x=10, y=140)

username_label = Label(login_frame, text="User name", font=(
    "Ariel", 10, "bold"), fg="#116D6E", bg="#B7B7B7")
username_label.place(x=70, y=250)
username_entry = Entry(login_frame, fg="#116D6E", borderwidth=0, width=20, font="Ariel, 14",
                       bg="white")  # cursor="heart"
username_entry.place(x=70, y=280)

password_label = Label(login_frame, text="Password", font=(
    "Ariel", 10, "bold"), fg="#116D6E", bg="#B7B7B7")
password_label.place(x=70, y=310)
password_entry = Entry(login_frame, fg="#116D6E", borderwidth=0, width=20, show="*", font="Ariel, 14",
                       bg="white")  # , cursor="heart"
password_entry.place(x=70, y=340)

# Creating a Login Button
login_button = Button(login_frame, text="Login", fg="#116D6E", bg="lightblue", font=("Ariel", 19, "bold"),
                      borderwidth=0, cursor="heart", command=Login)
login_button.place(x=90, y=410, width=170)

# Creating signup button
new_label = Label(login_frame, text="New to Match-Maker?",
                  fg="#F79327", bg="#DB005B", font=("Ariel", 11, "bold"))
new_label.place(x=30, y=470)
signUp_button = Button(login_frame, text="Sign Up", fg="#116D6E", bg="lightblue", font=("Ariel", 8, "bold"),
                       borderwidth=0, cursor="heart", command=signup)
signUp_button.place(x=200, y=470)
now_label = Label(login_frame, text="! NOW !", fg="#F79327",
                  bg="#DB005B", font=("Ariel", 12, "bold"))
now_label.place(x=260, y=470)

login.mainloop()
