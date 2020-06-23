#praise the lord,jesus,christ
#lord jesus christ please help me
import socket
d = socket.socket()
d.connect(("localhost",9999))
while True:
    d.send(bytes("hello","utf-8"))