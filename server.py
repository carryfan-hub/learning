#praise the lord,jesus,christ
#lord jesus christplease help me
import socket
s = socket.socket()
print("praise the lord")
s.bind(("localhost",9999))
s.listen(1)

while True:
    c,addr = s.accept()
    print(c,addr)
    for i in range(0,5):
        c.send(bytes(str(i),"utf-8"))
    c.close()

