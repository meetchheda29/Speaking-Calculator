from tkinter import *
from subprocess import call
import win32api
from win32com.client import Dispatch
def speak(string):
    speech=Dispatch(('SAPI.SpVoice'))
    speech.speak(string)
def exit():
    speak('Thank u for visiting Addition calculator')
    root.destroy()
root= Tk()
Label(root, text='Number1').grid(row=0,column=0) 
e1 = Entry(root)
e1.grid(row=0, column=1)
Label(root, text='Number2').grid(row=0,column=3) 
e2 = Entry(root)
e2.grid(row=0, column=4)
def Sum():
    
    x1 = e1.get()
    x2 = e2.get()
    label3 = Label(root, text= 'The Sum of ' + x1 + ' and ' + x2 + ' is:',font=('helvetica', 10)).grid(row=3,column=2)
    
    label4 = Label(root, text= float(x1)+float(x2),font=('helvetica', 10, 'bold')).grid(row=4,column=2)
    c= float(x1)+float(x2)
    b=('The Sum of ' + x1 + ' and ' + x2 + ' is:')
    d=(c)
    speak(b)
    speak(d)
button1 = Button(text='Get the Sum', command=Sum, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button1.grid(row=1, column=2)
button2 = Button(text='EXIT', command=exit, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button2.grid(row=2, column=2)
speak('Welcome to Addition calculator')
root.mainloop()
