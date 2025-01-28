from tkinter import *

win = Tk()
#กำหนดคุณลักษณะของคอนเทนเนอร์
win.geometry('400x300+600+200')
win.title('My GUI')
win.config(bg='#E6E6FA')

#สร้างวิดเจ็ด
btn1 = Button(text='One', width=15, height=5)
btn2 = Button(text='Two', font='time 14 bold')
btn3 = Button(text='Three', fg='#8A2BE2', font='time 14 bold', width=15)
lbl = Label(text='บอกชื่อของคุณ:', font='AngsanaUPC 14 bold')
ent = Entry(width=20)
#วางวิดเจ็ดลงในคอนเทนเนอร์
btn1.pack()
btn2.pack()
lbl.pack()
ent.pack()
btn3.pack()

#สั่งวนลูป แสดงผลหน้าต่าง
win.mainloop()