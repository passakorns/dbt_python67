from tkinter import *

win = Tk()

win.geometry('400x300+600+200')

btn1 = Button(text='First')
btn2 = Button(text='Second')
btn3 = Button(text='Third')
btn4 = Button(text='Forth')
btn5 = Button(text='Five')

btn1.pack(side=TOP, pady=15, fill=X)
btn2.pack(side=LEFT, padx=20, fill=Y)
btn3.pack(side=RIGHT, padx=20, fill=Y)
btn4.pack(side=BOTTOM, pady=25, fill= X)
btn5.pack(side=BOTTOM, pady=25, fill=X)

win.mainloop()