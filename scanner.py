#Import Socket Module
import socket
#AF_INET is stands from Address Family on Internet also called IP address
#AF_INET it use for the version 4 IP addresses
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.settimeout(2)

host = '192.168.43.208'
port = 4430

def portscanner(port):
    if socket.connect_ex((host,port)):
        print('port %d is close'%(port))
    else :
        print("port %d is open"%(port))


portscanner(port)

