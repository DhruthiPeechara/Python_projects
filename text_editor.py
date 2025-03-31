from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk ()
window.title("Codingal's Text Editor ")
window.geometry("600x500")
window.rowconfigure(0, minisize=800, weight=1)
window.columnfigure(1,  minisize = 800, weight = 1)

def open_file():
    """ Open a file for editing"""
    filepath = askopenfilename (
        filetypes = [("Text files ", "*.txt"), ("All files", "*.*")]

    )
    if not filepath: 
        