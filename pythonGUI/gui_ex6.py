#คลิกปุ่ม แล้วให้เปลี่ยนข้อความ

from tkinter import *
import my_fun as fun

win = fun.create_window('My id.XXX')
def change():
    txt = mylbl['text']
    updateText=''
    if txt=='ธีรภัทร ทวีศรี':
        updateText= 'กรภัทร์ ปัญญาอรรถ'
    else:
        updateText= 'ธีรภัทร ทวีศรี'
    mylbl.config(text=updateText)

mylbl = Label(text='ธีรภัทร ทวีศรี',font=('AngsanaUPC', 20))
btnChange = Button(text='เปลี่ยนชื่อ',font=('AngsanaUPC', 16))
btnChange.config(command=change)

mylbl.pack()
btnChange.pack()
win.mainloop()