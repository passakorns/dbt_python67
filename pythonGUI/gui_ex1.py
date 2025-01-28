from tkinter import *

#สร้างคอนเทนเนอร์หลัก
root_window = Tk()

root_window.title('Tk Interface my GUI')
#การกำหนดขนาดของวินโดว์+ตำแหน่งการวางวินโดว์
# กว้างxสูง+ตำแหน่งแกนX + ตำแหน่งแกนY
root_window.geometry('500x400+600+200')

#กำหนดการเปลี่ยนขนาดของวินโดว์
root_window.resizable(True, False) #width, height :0=False,1=True

root_window.minsize(200,80)
root_window.option_add('*font','Courier 16 bold')
root_window.config(bg='pink')

#สร้างวิดเจ็ดชนิดป้ายชื่อ
my_label = Label(text='สวัสดีเช้าวันอังคาร', bg='pink')
my_label2 = Label(text='ท้องฟ้าสดใส', bg='pink')

#วางป้ายชื่อในวินโดว์
my_label.pack()
my_label2.pack()

root_window.mainloop()