from tkinter import *
import my_fun as fun

root = fun.create_window(name_title='GUI_Ex4: ')

lbl_name = Label(text='Name: ', width=10)
lbl_age = Label(text='Age: ',width=10)

ent_name = Entry()
ent_age =Entry()

btn1 = Button(text='Ok',width=10)
btn2 = Button(text='Clear', width=10)
btn3 = Button(text='Cancel', width=10)

#จัดวางวิดเจ็ต
lbl_name.place(x=65, y=50)
ent_name.place(x=165, y=50)
lbl_age.place(x=65, y=100)
ent_age.place(x=165, y=100)
btn1.place(x=65, y=180)
btn2.place(x=165, y=180)
btn3.place(x=265, y=180)

root.mainloop()