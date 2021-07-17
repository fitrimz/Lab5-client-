import socket

s= socket.socket()

port=8888

s.connect(('192.168.1.27',port))

data=s.recv(1024)

s.send(b'HI,SAYA CLIENT.Terima Kasih!!');

print (data)

s.close()
