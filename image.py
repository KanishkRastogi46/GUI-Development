from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root= Tk()
root.title("Images")
root.iconbitmap("download.jpeg")

mainframe= ttk.Frame(root, padding='10')
mainframe.grid(row=0, column=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

my_image= ImageTk(mainframe, Image.open("download.jpeg"))
my_label= ttk.Label(image=my_image)

root.mainloop()