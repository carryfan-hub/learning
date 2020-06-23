#praise the lord,jesus,christ
#lord jesus christplease help me
from tkinter import * 
window = Tk()
x=Entry(window,width=200000)
x.pack()
def connect():
    import socket
    f = socket.socket()
    f.bind(("localhost",9999))
    f.listen(2)
    while True:
        c,addr = f.accept()
        x.insert(0,"praise the lord")
        m=c.recv(2438467587).decode()
        x.insert(0,str(m))
        c.close()
        
    
d=Button(window,text="startchat",command=connect)
d.pack()
window.mainloop()

