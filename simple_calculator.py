from tkinter import *
from tkinter import ttk

root= Tk()
root.title("Calculator")

#creating a frame widget in which we will place all the other widgets
mainframe= ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
#print(mainframe.configure())

#creating a input box
e= ttk.Entry(mainframe, width=60)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

#function for calculations
def button_click(number):
    e.delete(0, END)
    e.insert(0, number)

#creating buttons
button1= ttk.Button(mainframe, text="1", padding="5", command=lambda:button_click(1))
button2= ttk.Button(mainframe, text="2", padding="5", command=lambda:button_click(2))
button3= ttk.Button(mainframe, text="3", padding="5", command=lambda:button_click(3))
button4= ttk.Button(mainframe, text="4", padding="5", command=lambda:button_click(4))
button5= ttk.Button(mainframe, text="5", padding="5", command=lambda:button_click(5))
button6= ttk.Button(mainframe, text="6", padding="5", command=lambda:button_click(6))
button7= ttk.Button(mainframe, text="7", padding="5", command=lambda:button_click(7))
button8= ttk.Button(mainframe, text="8", padding="5", command=lambda:button_click(8))
button9= ttk.Button(mainframe, text="9", padding="5", command=lambda:button_click(9))
button0= ttk.Button(mainframe, text="0", padding="5", command=lambda:button_click(0))
buttonAdd= ttk.Button(mainframe, text="+", padding="5", command=button_click)
buttonEqualsTo= ttk.Button(mainframe, text="=", padding="5", command=button_click)
buttonClear= ttk.Button(mainframe, text="clr", padding="5", command=button_click)
#print(button0.configure())

#packing buttons onto the screen
button1.grid(row= 3, column=0 )
button2.grid(row= 3, column= 1)
button3.grid(row= 3, column= 2)

button4.grid(row= 2, column=0 )
button5.grid(row=2, column= 1)
button6.grid(row= 2, column= 2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0 )
buttonAdd.grid(row=4, column=1)
buttonEqualsTo.grid(row=5, column=0 )
buttonClear.grid(row=5, column=1 )

#event loop
root.mainloop()