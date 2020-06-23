#praise the lord,jesus,christ
#lord jesus christplease help me
import socket
t = socket.socket()
t.bind(("localhost",9999))
t.listen(2)
while True:
    c,addr = t.accept()
    c.send(bytes("praise the lord","utf-8"))
    c.close()





