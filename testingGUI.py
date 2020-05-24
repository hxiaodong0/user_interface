#
# import tkinter as tk
# win = tk.Tk()
#
# var = tk.IntVar()
# var_entry = tk.Entry(win,text='var',textvariable=var)
# var_entry.grid()
#
# def handle_button(event):
#     button_arg = event.widget['text']
#     var_entry.insert(15,1)    #insert(self, index, string)
#
# button1 = tk.Button(win, text = "kkk")
# button1.bind("<Button-1> ", handle_button)
# button1.grid()
# # similarly I defined all the buttons.
#
#
# win.mainloop()








# x = StringVar() # Holds a string; default value ""
# x = IntVar() # Holds an integer; default value 0
# x = DoubleVar() # Holds a float; default value 0.0
# x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True

# from tkinter import *
#
# def motion(event):
#   print("Mouse position: (%s %s)" % (event.x, event.y))
#   return
#
# master = Tk()
# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = Message(master, text = whatever_you_do)
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# msg.bind('<Motion>',motion)   # widget.bind(event, handler) 如果有一个指定事件发生，则进行某种行为；；
# msg.pack()
# mainloop()



lst = [1,2,3,4,5,6, "+",6,5,3,2]


def plus_operation(lst):
    lsta = []
    a = ''
    lstb = []
    b = ''
    for item in lst:
        if type(item) != str:
            lsta.append(item)
            lst = lst[1:]
        if type(item) == str:
            lst = lst[1:]
            break
    lstb = lst
    for item in lsta:
        a += str(item)
    # print(a)
    for item in lstb:
        b += str(item)
    # print(b)
    # result_label = Label(root, text= str(int(a)+int(b)), padx=button_x, pady=button_y)  # state = DISABLED,
    # result_label.grid(row=5, column=3)
    return int(a)+int(b)

print (plus_operation(lst))