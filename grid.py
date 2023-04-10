from tkinter import *

root= Tk()

#creating a label widget
myLabel1= Label(root, text='Hello World!')
myLabel2= Label(root, text='My name is Kanishk Rastogi')
myLabel3= Label(root, text='yo yo motherfucker how u doing').grid(row=3,column=4)

#shoving it onto the screen
myLabel1.grid(row=1, column=1)
myLabel2.grid(row=2, column=1)

root.mainloop()