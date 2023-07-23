from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

global Password_entry
global eye1
global eye
global eye2


def signup():
    messagebox.showinfo("Signup has not been made yet. PLease wait for next update")


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
