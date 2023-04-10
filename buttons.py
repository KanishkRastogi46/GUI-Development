from tkinter import *

root= Tk()

def myClick():
    myLabel= Label(root, text='Hello, how are u?')
    myLabel.pack()

#creating a button
#padx and pady add padding in x and y direction
myButton= Button(root, text="CLICK", command=myClick, padx=20, pady=5, fg='red', bg='yellow')
myButton.pack()

root.mainloop()