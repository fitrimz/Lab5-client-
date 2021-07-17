import socket

udpS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "HELLO !! SERVER.. IM CLIENT"


#send message using sendto

udpS.sendto(message.encode(),('192.168.1.27',8080))
