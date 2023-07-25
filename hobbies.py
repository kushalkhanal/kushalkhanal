from tkinter import *
from pymongo import *

hobbies_window = Tk()
hobbies_window.title('Hobbies')
hobbies_window.resizable(0, 0)
hobbies_window.geometry('300x400')
hobbies_window.config(bg="#DB005C")

client = MongoClient('mongodb://localhost:27017')
database = client['matchmaker']
hobbies_collection = database['users_hobbies']

def create_hobbies_check_btns(hobbies_window, hobby, x, y):
    # Use IntVar to represent the state of the Checkbutton (0 for unchecked, 1 for checked)
    CheckVar = IntVar()
    check_btns = Checkbutton(hobbies_window, text=hobby, width=10, font=('', 12, 'bold'), bg="#DB005C", variable=CheckVar,onvalue=1,offvalue=0)
    check_btns.configure(anchor='w')
    check_btns.place(x=x, y=y)
    return CheckVar

def save_submit():
    pass

hobbies_list = []
hobbies_list.append(create_hobbies_check_btns(hobbies_window, "Playing", 10, 30))
hobbies_list.append(create_hobbies_check_btns(hobbies_window, "Reading", 10, 60))
hobbies_list.append(create_hobbies_check_btns(hobbies_window, "Music", 10, 90))

# Store the IntVar objects associated with the Checkbuttons in a separate list
hobbies_check_vars = [CheckVar for CheckVar in hobbies_list]

submit_btn = Button(hobbies_window, text="Submit", font=('', 14, 'bold'), bg='#DB005C', command=save_submit)
submit_btn.place(x=40, y=150)

hobbies_window.mainloop()
