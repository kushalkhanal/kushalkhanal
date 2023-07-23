from tkinter import *
from PIL import ImageTk, Image

profile = Tk()
profile.state("zoomed")

# matched account image scroller
image_viewer = LabelFrame(profile, bg='lightblue')
image_viewer.place(x=1050, y=0)

# profile_img = Frame(profile,bg='lightblue')
# profile_img.place(x=1050, y=0)

my_img1 = Image.open("files/a (1).jpg")
my_img2 = Image.open("files/a (2).jpg")
my_img3 = Image.open("files/a (3).jpg")
my_img4 = Image.open("files/a (4).jpg")
my_img5 = Image.open("files/a (5).jpg")
my_img6 = Image.open("files/a (6).jpg")

re_image1 = my_img1.resize((300, 300))
re_image2 = my_img2.resize((300, 300))
re_image3 = my_img3.resize((300, 300))
re_image4 = my_img4.resize((300, 300))
re_image5 = my_img5.resize((300, 300))
re_image6 = my_img6.resize((300, 300))

image1 = ImageTk.PhotoImage(re_image1)
image2 = ImageTk.PhotoImage(re_image2)
image3 = ImageTk.PhotoImage(re_image3)
image4 = ImageTk.PhotoImage(re_image4)
image5 = ImageTk.PhotoImage(re_image5)
image6 = ImageTk.PhotoImage(re_image6)

image_list = [image1, image2, image3, image4, image5, image6]

my_label = Label(image_viewer, image=image1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image_viewer, image=image_list[image_number - 1])
    button_forward = Button(image_viewer, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(image_viewer, text="<<", command=lambda: back(image_number - 1))

    if image_number == 6:
        button_forward = Button(image_viewer, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image_viewer, image=image_list[image_number - 1])
    button_forward = Button(image_viewer, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(image_viewer, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(image_viewer, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(image_viewer, text="<<", command=back)  # as image will already be on the first one
button_exit = Button(image_viewer, text="Exit Program", command=profile.destroy)
button_forward = Button(image_viewer, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

profile.mainloop()
