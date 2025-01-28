from tkinter import *
import my_fun as fun

win = fun.create_window('My Grid id.XXX')

btn = Button(text='Python')
btn.grid(row=0, column=0,padx=20, pady=20)

Button(text='Programming').grid(row=0, column=2,padx=5)
Button(text='Google').grid(row=0, column=1, padx=10)

Button(text='Coffee').grid(row=1,column=0)
Button(text='Americano').grid(row=1,column=1, columnspan=2)
win.mainloop()