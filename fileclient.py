import socket

s = socket.socket()

s.connect(('192.168.1.27', 8888))

# encryptor
file = open("outputFile.txt", "rb")
SendFile = file.read(1024)

while SendFile:
    data = s.recv(1024)
    print(data)
    
    s.send(SendFile)
    SendFile = file.read(1024)     
    
s.close()
