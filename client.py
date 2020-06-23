#praise the lord,jesus,christ
#lord jesus christ please help me
from tkinter import *
window = Tk()
g=Entry(window,width=200)
g.focus()
g.pack()
def chat():
    import socket
    o=socket.socket()
    o.connect(("localhost",9999))
    l=g.get()
    o.send(bytes(str(l),"utf-8"))
    g.delete(0,END)
h=Button(window,text="connec to the server",command=chat)
h.pack()


window.mainloop()