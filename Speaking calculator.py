from tkinter import *
from subprocess import call
import win32api
from win32com.client import Dispatch
master=Tk()
text = Label(master, text="Speaking Calculator",fg='brown',
font=('helvetica',55, 'bold'))
text.pack(pady=50)
def speak(string):
    speech=Dispatch(('SAPI.SpVoice'))
    speech.speak(string)

def ADD():
    call(["python", "ADD.py"])

b1 = Button(master,text='Add(Gives sum of two numbers)',command=ADD,bg='brown', fg='white', font=('helvetica', 20, 'bold'))
b1.pack(pady=25)

def SQR():
    call(["python", "Speaking square.py"])

b1 = Button(master,text='Square(calculates square of a number)',command=SQR,bg='brown', fg='white', font=('helvetica', 20, 'bold'))
b1.pack(pady=25)

def Diff():
    call(["python", "DIFF.py"])

b1 = Button(master,text='Difference(Gives difference of two digits)',command=Diff,bg='brown', fg='white', font=('helvetica', 20, 'bold'))
b1.pack(pady=25)

def SR():
    call(["python", "SQR ROOT.py"])

def exit():
    speak("Thank you for visiting Speaking Calculator")
    master.destroy()
b1 = Button(master,text='Square root(Gives square root of a number)',command=SR,bg='brown', fg='white', font=('helvetica', 20, 'bold'))
b2 = Button(master,text='Exit',command=exit,bg='brown', fg='white', font=('helvetica', 15, 'bold'))
b1.pack(pady=25)
b2.pack(pady=25)
speak('Welcome to speaking calculator') 
master.mainloop()
