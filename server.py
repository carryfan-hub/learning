#praise the lord,jesus,christ
#lord jesus christplease help me
import socket
v = socket.socket()
v.bind(("localhost",9990))
v.listen(2)
while True:
    c,addr=v.accept()
    print(c,addr)
    m = c.recv(1024).decode()
    y = c.recv(1).decode()
    k = c.recv(1).decode()
    if m == "subtraction":
        j = int(y) - int(k)
        print(j)
    else:
        c.send(bytes("no","utf-8"))
        
    c.close()
