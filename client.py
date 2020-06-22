import socket
d=socket.socket()
d.connect(("localhost",9999))
for t in range(0,2):
    f = d.recv(24253654).decode()
    print(f)


