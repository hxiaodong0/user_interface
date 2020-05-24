from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

img1 = ImageTk.PhotoImage(Image.open("insta.png"))
img2 = ImageTk.PhotoImage(Image.open("lol.png"))
img3 = ImageTk.PhotoImage(Image.open("lol1.png"))
img4 = ImageTk.PhotoImage(Image.open("lol2.png"))
img5 = ImageTk.PhotoImage(Image.open("lol33.png"))


image_lst = [img1,img2,img3,img4,img5]
n = random.randint(0, 4)
my_label = Label(image = image_lst[n] )
my_label.grid(row = 0, column = 0, columnspan = 3)
def forward():
    global n
    if n < len(image_lst)-1:
        n +=1
        return NORMAL
    elif n == len(image_lst)-1:
        n = len(image_lst)-1
    my_label = Label(image = image_lst[n])
    my_label.grid(row=0, column=0, columnspan=3)
def backward():
    global n
    if n != 0:
        n -= 1
    elif n == 0:
        n = 4
    my_label = Label(image = image_lst[n])
    my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text = "<<", command = backward)
button_exit = Button(root, text = "Exit PROGRAM", command = root.quit)
button_forward = Button(root, text = ">>", command = forward)
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)
# root.tk.call('wm', 'iconphoto', root._w, img1)

root.title("gallery")



root.mainloop()


# img = PhotoImage(file = '/Users/xiaodonghuo/PycharmProjects/user_interface/ok.ico')
# root.tk.call('wm', 'iconphoto', root._w, img)
# root.iconbitmap('/Users/xiaodonghuo/PycharmProjects/user_interface/ok.ico')





