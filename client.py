#praise the lord,jesus,christ
#lord jesus christplease help me
from tkinter import *
window = Tk()
d = Entry(window,width=200)
d.pack()
def connect():
    import socket
    v=socket.socket()
    v.connect(("localhost",9999))
    l=v.recv(425365).decode()
    d.delete(0,END)
    d.insert(0,str(l))
    
g = Button(window,text="connect",command=connect)
g.pack()
window.mainloop()
#ok
