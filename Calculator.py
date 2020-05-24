from tkinter import *
global lst
lst =[]

button_x = 20
button_y = 17
root = Tk()
root.title("calculator")
e = Entry(root, width = 20,  borderwidth = 5)
e.grid( row = 0, column = 1 , columnspan = 3, padx = 10, pady = 10)
# e.insert(0,"Enter an integer")
def handle_button(number):
    current = e.get() #fetch the current entry text
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    lst.append(number)
def handle_button_9(event):
    e.insert(15,9)
    lst.append(9)
# def handle_button_plus(event):
#     e.insert(15,"+")
#     lst.append("+")
def handle_button_minus(event):
    e.insert(15,"-")
    lst.append("-")
def plus_operation():
    global method
    method = "+"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0,END)
    # result_label = Label(root, text= sum, padx=button_x, pady=button_y)  # state = DISABLED,
    # result_label.grid(row=5, column=3)
def min_operation():
    global method
    method = "-"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
def mul_operation():
    global method
    method = "*"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
def div_operation():
    global method
    method = "/"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_enter():
    global f_num
    global method
    second_number = e.get()
    e.delete(0,END)
    if method == "+":
        result = f_num + int(second_number)
    elif method == "-":
        result = f_num - int(second_number)
    elif method == "*":
        result = f_num * int(second_number)
    elif method == "/":
        result = format(float(f_num) / float(second_number), ".2f")
    e.insert(0, result)
    result_label = Label(root, text= result, padx=button_x, pady=button_y)  # state = DISABLED,
    result_label.grid(row=5, column=3)

def clear():
    global lst
    lst = []
    print(lst)
    e.delete(0, 'end')
    result_label = Label(root, text= '', padx=button_x, pady=button_y)  # state = DISABLED,
    result_label.grid(row=5, column=3)

button_0 = Button(root, text = "0", padx = button_x, pady = button_y, command = lambda: handle_button(0))
button_1 = Button(root, text = "1", padx = button_x, pady = button_y, command = lambda: handle_button(1))
button_2 = Button(root, text = "2", padx = button_x, pady = button_y, command = lambda: handle_button(2))
button_3 = Button(root, text = "3", padx = button_x, pady = button_y, command = lambda: handle_button(3))
button_4 = Button(root, text = "4", padx = button_x, pady = button_y, command = lambda: handle_button(4))
button_5 = Button(root, text = "5", padx = button_x, pady = button_y, command = lambda: handle_button(5))
button_6 = Button(root, text = "6", padx = button_x, pady = button_y, command = lambda: handle_button(6))
button_7 = Button(root, text = "7", padx = button_x, pady = button_y, command = lambda: handle_button(7))
button_8 = Button(root, text = "8", padx = button_x, pady = button_y, command = lambda: handle_button(8))
button_9 = Button(root, text = "9", padx = button_x, pady = button_y)
button_plus = Button(root, text = "+", padx = button_x, pady = button_y, command = plus_operation)
button_minus = Button(root, text = "-", padx = button_x, pady = button_y,command = min_operation )
button_multiply = Button(root, text = "X", padx = button_x, pady = button_y, command = mul_operation)
button_divide = Button(root, text = "/", padx = button_x, pady = button_y, command = div_operation)

button_clear = Button(root, text = "clear", padx = button_x, pady = button_y, command = clear)
Label_equal = Label(root, text = "=", padx = button_x, pady = button_y)
button_enter = Button(root, text = "Enter", padx = button_x, pady = button_y,command = button_enter)

# text_result = StringVar(root,text= "testing text")
button_9.bind("<Button-1> ", handle_button_9)
# button_plus.bind("<Button-1> ", handle_button_plus)

# button_enter.bind("<Button-1> ", plus_operation)

button_0.grid(row = 4, column = 1)
button_1.grid(row = 3, column = 1)
button_2.grid(row = 3, column = 2)
button_3.grid(row = 3, column = 3)
button_4.grid(row = 2, column = 1)
button_5.grid(row = 2, column = 2)
button_6.grid(row = 2, column = 3)
button_7.grid(row = 1, column = 1)
button_8.grid(row = 1, column = 2)
button_9.grid(row = 1, column = 3)
button_clear.grid(row = 4, column = 2)
button_plus.grid(row = 5, column =1)
button_minus.grid(row = 6, column =1)
button_multiply.grid(row = 6, column =2)
button_divide.grid(row = 6, column =3)
Label_equal.grid(row = 5, column = 2)
button_enter.grid(row = 4, column = 3)
button_enter.grid(row = 4, column = 3)
# text_result.grid(row= 4, column = 4)

def myClick():
    myLabel1 = Label(root, text=e.get() + " me", background = "#000fff000")
    myLabel1.pack()

myLabel2 = Label(root, text = "My name is what the fuck \n LOLO ")


root.mainloop()


# def squ():
#
#     miles = int(el_value.get()) * 1.6
#     t1.insert(END,miles)
#
#
# b1=Button(window, text = "Execute", command = squ)
# b1.grid(row = 0, column = 0, rowspan = 1)
#
# t2 = Text(window,height = 1, width = 20, text = "fa" )
# t2.grid(row = 1, column = 2)
#
# el_value = StringVar()
    # e1 = Entry(window,textvariable = el_value )
# e1.grid(row=0, column = 1)
#
# t1 = Text(window,height = 1, width = 20, )
# t1.grid(row = 0, column = 2)
#
# window.mainloop()  # exit button
# def plus_operation():
#     global lst
#     print(lst)
#     lsta = []
#     a = ''
#     lstb = []
#     b = ''
#     for item in lst:
#         if type(item) != str:
#             lsta.append(item)
#             lst = lst[1:]
#         if type(item) == str:
#             lst = lst[1:]
#             break
#     lstb = lst
#     for item in lsta:
#         a += str(item)
#     # print(a)
#     for item in lstb:
#         b += str(item)
#     # print(b)
#     sum = int(a)+int(b)
#     print(sum)
#     result_label = Label(root, text= sum, padx=button_x, pady=button_y)  # state = DISABLED,
#     result_label.grid(row=5, column=3)
#     return sum