from tkinter import *
from subprocess import call
import win32api
from win32com.client import Dispatch
def speak(string):
    speech=Dispatch(('SAPI.SpVoice'))
    speech.speak(string)
def exit():
    speak('Thank you for visiting Square calculator')
    root.destroy()
root= Tk()
Label(root, text='Number').grid(row=0) 
e1 = Entry(root)
e1.grid(row=0, column=1)
def getSquare():
    
    x1 = e1.get()
    string = str(float(x1)**2)
    label3 = Label(root, text= 'The Square of ' + x1 + ' is:',font=('helvetica', 10)).grid(row=3,column=0)
    
    label4 = Label(root, text= string,font=('helvetica', 10, 'bold')).grid(row=4,column=0)
    c= float(x1)**2
    b=('The Square of ' + x1 + ' is:')
    d=(c)
    speak(b)
    speak(d)
button1 = Button(text='Get the Square', command=getSquare, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button1.grid()
button2 = Button(text='EXIT', command=exit, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button2.grid()
speak('Welcome to Square calculator')
root.mainloop()

