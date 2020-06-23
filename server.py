#praise the lord,jesus,christ
#lord jesus christplease help me
import socket
v = socket.socket()
v.bind(("localhost",9999))
v.listen(2)
while True:
    c,addr = v.accept()
    m=c.recv(1024).decode()
    print(m)
    
    

