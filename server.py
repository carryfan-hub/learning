#praise the lord,jesus,christ
#lord jesus christplease help me
from tkinter import *
window = Tk()
x=Entry(window,width=200)
x.pack()
def start():
    import socket
    v=socket.socket()
    v.bind(("localhost",9990))
    v.listen(2)
    print("praise the lord")
    c,addr = v.accept()
    while True:
        c,addr=v.accept()
        m = c.recv(1024).decode()
        print("all ok")
        x.insert(0,m)
        c.close()
g = Button(window,text="press",command=start)
g.pack()
window.mainloop()