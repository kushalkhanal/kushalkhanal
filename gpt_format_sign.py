from tkinter import *
from PIL import ImageTk, Image


def toggle_password_visibility():
    if Password_entry["show"] == "*":
        Password_entry["show"] = ""
        eye.configure(image=eye1)
    else:
        Password_entry["show"] = "*"
        eye.configure(image=eye2)


def add_selected_option():
    selected_indices = listbox.curselection()
    selected_options = [listbox.get(index) for index in selected_indices]
    for opt in selected_options:
        if opt not in selected_listbox.get(0, END):
            selected_listbox.insert(END, opt)


def add_selected_option2():
    selected_indices = listbox2.curselection()
    selected_options = [listbox2.get(index) for index in selected_indices]
    for opt in selected_options:
        if opt not in selected_listbox2.get(0, END):
            selected_listbox2.insert(END, opt)


def next1():
    frame1.place_forget()
    frame2.place(x=0, y=0)
    frame2.pack_propagate()


def before1():
    frame2.place_forget()
    frame1.place(x=0, y=0)
    frame1.pack_propagate()


def next2():
    frame2.place_forget()
    frame3.place(x=0, y=0)
    frame3.pack_propagate()


def before2():
    frame3.place_forget()
    frame2.place(x=0, y=0)
    frame2.pack_propagate()


def next3():
    frame3.place_forget()
    frame4.place(x=0, y=0)
    frame4.pack_propagate()


def before3():
    frame4.place_forget()
    frame3.place(x=0, y=0)
    frame3.pack_propagate()


app = Tk()
app.geometry('670x735')
app.resizable(False, False)

# Creating first frames for signUp
frame1 = LabelFrame(app, width=670, height=735, relief='flat')
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

# Creating widgets (Label, Entry, Canvas=>line) to be placed in "frame1"
firstname = Label(frame1, text="first Name", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
firstname.place(x=120, y=250)
firstname_entry = Entry(frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
firstname_entry.place(x=300, y=250)
canvas1.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

lastname = Label(frame1, text="last Name", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
lastname.place(x=120, y=310)
lastname_entry = Entry(frame1, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
lastname_entry.place(x=300, y=310)
canvas1.create_line(30, 140, 270, 140, fill="#8294C4", width=3)

# Creating buttons in "frame1"
next_button1 = Button(frame1, text="Next", font=('Ariel', 15, "bold"), fg="white", bg="#007AFF", bd=0, padx=30, pady=2,
                      command=next1)
next_button1.place(x=460, y=600)

# Creating second frames for signUp
frame2 = LabelFrame(app, width=670, height=735, relief='flat')
frame2.place_forget()
frame2.pack_propagate()

# Adding login_frame image
image2 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
image2_label = Label(frame2, image=image2)
image2_label.place(x=-4, y=-5)

# sign_up label widget
signup2 = Label(frame2, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
signup2.place(x=220, y=30)

# Creating widgets (Label, Entry, Canvas=>line) to be placed in "frame2"
email = Label(frame2, text="Email", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
email.place(x=120, y=250)
email_entry = Entry(frame2, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
email_entry.place(x=300, y=250)
canvas1.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

password = Label(frame2, text="Password", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
password.place(x=120, y=310)
Password_entry = Entry(frame2, show='*', width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
Password_entry.place(x=300, y=310)
canvas1.create_line(30, 140, 270, 140, fill="#8294C4", width=3)

eye1 = ImageTk.PhotoImage(Image.open('login_signup/eye.png'))
eye2 = ImageTk.PhotoImage(Image.open('login_signup/invisible.png'))
eye = Button(frame2, image=eye1, relief='flat', bg="#DBDFEA", bd=0, activebackground="#DBDFEA",
             command=toggle_password_visibility)
eye.place(x=530, y=320)

# Creating buttons in "frame2"
before_button1 = Button(frame2, text="Previous", font=('Ariel', 15, "bold"), fg="white", bg="#007AFF", bd=0, padx=10,
                        pady=2, command=before1)
before_button1.place(x=250, y=600)

next_button2 = Button(frame2, text="Next", font=('Ariel', 15, "bold"), fg="white", bg="#007AFF", bd=0, padx=30, pady=2,
                      command=next2)
next_button2.place(x=460, y=600)

# Creating third frames for signUp
frame3 = LabelFrame(app, width=670, height=735, relief='flat')
frame3.place_forget()
frame3.pack_propagate()

# Adding login_frame image
image3 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
image3_label = Label(frame3, image=image3)
image3_label.place(x=-4, y=-5)

# sign_up label widget
signup3 = Label(frame3, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
signup3.place(x=220, y=30)

# Creating widgets (Label, Entry, Canvas=>line) to be placed in "frame3"
phone = Label(frame3, text="Phone", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
phone.place(x=120, y=250)
phone_entry = Entry(frame3, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
phone_entry.place(x=300, y=250)
canvas1.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

address = Label(frame3, text="Address", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
address.place(x=120, y=310)
address_entry = Entry(frame3, width=20, font='Ariel, 15', borderwidth=0, bg='#DBDFEA', fg='#ACB1D6')
address_entry.place(x=300, y=310)
canvas1.create_line(30, 140, 270, 140, fill="#8294C4", width=3)

# Creating buttons in "frame3"
before_button2 = Button(frame3, text="Previous", font=('Ariel', 15, "bold"), fg="white", bg="#007AFF", bd=0, padx=10,
                        pady=2, command=before2)
before_button2.place(x=250, y=600)

next_button3 = Button(frame3, text="Next", font=('Ariel', 15, "bold"), fg="white", bg="#007AFF", bd=0, padx=30, pady=2,
                      command=next3)
next_button3.place(x=460, y=600)

# Creating fourth frames for signUp
frame4 = LabelFrame(app, width=670, height=735, relief='flat')
frame4.place_forget()
frame4.pack_propagate()

# Adding login_frame image
image4 = ImageTk.PhotoImage(Image.open('login_signup/signup_frame.png'))
image4_label = Label(frame4, image=image4)
image4_label.place(x=-4, y=-5)

# sign_up label widget
signup4 = Label(frame4, text="Sign Up", font=('Ariel', 45, "italic", "underline"), fg="#007AFF", bg="#DBDFEA")
signup4.place(x=220, y=30)

# Creating widgets (Label, Entry, Canvas=>line) to be placed in "frame4"
languages = Label(frame4, text="Languages", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
languages.place(x=120, y=250)

listbox = Listbox(frame4, font=('Ariel', 12), selectmode=MULTIPLE, width=20, height=4, bg='#DBDFEA', fg='#ACB1D6')
listbox.insert(END, "English")
listbox.insert(END, "Spanish")
listbox.insert(END, "French")
listbox.place(x=300, y=250)

selected_listbox = Listbox(frame4, font=('Ariel', 12), width=20, height=4, bg='#DBDFEA', fg='#ACB1D6')
selected_listbox.place(x=540, y=250)

add_button = Button(frame4, text="Add", font=('Ariel', 12, "bold"), fg="white", bg="#007AFF", bd=0, padx=10, pady=2,
                    command=add_selected_option)
add_button.place(x=460, y=320)

remove_button = Button(frame4, text="Remove", font=('Ariel', 12, "bold"), fg="white", bg="#007AFF", bd=0, padx=10,
                       pady=2)
remove_button.place(x=620, y=250)

canvas1.create_line(30, 70, 270, 70, fill="#8294C4", width=3)

interests = Label(frame4, text="Interests", font=('Ariel', 15), fg="#8294C4", bg="#DBDFEA")
interests.place(x=120, y=390)

listbox2 = Listbox(frame4, font=('Ariel', 12), selectmode=MULTIPLE, width=20, height=4, bg='#DBDFEA', fg='#ACB1D6')
listbox2.insert(END, "Music")
listbox2.insert(END, "Sports")
listbox2.insert(END, "Books")
listbox2.place(x=300, y=390)

selected_listbox2 = Listbox(frame4, font=('Ariel', 12), width=20, height=4, bg='#DBDFEA', fg='#ACB1D6')
selected_listbox2.place(x=540, y=390)

add_button2 = Button(frame4, text="Add", font=('Ariel', 12, "bold"), fg="white", bg="#007AFF", bd=0, padx=10, pady=2,
                     command=add_selected_option2)
add_button2.place(x=460, y=460)

remove_button2 = Button(frame4, text="Remove", font=('Ariel', 12, "bold"), fg="white", bg="#007AFF", bd=0, padx=10,
                        pady=2)
remove_button2.place(x=620, y=390)

canvas1.create_line(30, 140, 270, 140, fill="#8294C4", width=3)

# Creating buttons in "frame4"
before_button3 = Button(frame4, text="Previous", font=('Ariel', 15, "bold"), fg="white", bg="#007AFF", bd=0, padx=10,
                        pady=2, command=before3)
before_button3.place(x=250, y=600)

submit_button = Button(frame4, text="Submit", font=('Ariel', 15, "bold"), fg="white", bg="#007AFF", bd=0, padx=30,
                       pady=2)
submit_button.place(x=460, y=600)

app.mainloop()
