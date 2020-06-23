#praise the lord,jesus,christ
#lord jesus christ please help me
from tkinter import *
window = Tk()
j=Entry(window,width=200)
j.pack()
def chat():
    import socket
    mk = socket.socket()
    mk.connect(("localhost",9990))
    l =j.get()
    mk.send(bytes(l,"utf-8"))
    
ki = Button(window,text="go",command = chat)
ki.pack()
window.mainloop()
    