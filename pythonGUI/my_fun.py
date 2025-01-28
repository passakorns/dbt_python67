from tkinter import *

def create_window(name_title):
    window = Tk()
    window.geometry('400x300+600+200')
    window.title(name_title)
    window.config(bg='#E6E6FA')
    return window

