#praise the lord,jesus,christ
#lord jesus christ please help me
import socket
f = socket.socket()
f.connect(("localhost",9990))
m=str(input())
y=input()
k=input()
f.send(bytes(str(m),"utf-8"))
f.send(bytes(y,"utf-8"))
f.send(bytes(k,"utf-8"))

    