from tkinter import * 

from datetime import date 

root = Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')

lbl = Label(text"Hey There", fg = "White" , bg = 'Pink', height= 1, width= 300)

name_lbl = Label(text = "Full name", bg = "Blue")

name_entry = Entry()


def display ():

    name = name_entry.get()

    global message 
    message = "Welcome to the Application! \nToday's date is "
    greet = "Hello"+ name+"\n"


    text_box.insert(END, greet )
    text_box.insert(END, message)
    text_box.insert(END, date.today())

    text_box = Text(height = 3)