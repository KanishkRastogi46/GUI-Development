from tkinter import *

root= Tk()

#creating a input box
e= Entry(root, width=65, bg="black", fg='white')
e.pack()
e.insert(0, "Enter your name: ")
e.get()         #returns a value that has been entered in the input box


def myClick():
    myLabel= Label(root, text='Hello, how are u?'+e.get())
    myLabel.pack()

#creating a button
#padx and pady add padding in x and y direction
myButton= Button(root, text="CLICK", command=myClick, padx=20, pady=5, fg='red', bg='yellow')
myButton.pack()

root.mainloop()