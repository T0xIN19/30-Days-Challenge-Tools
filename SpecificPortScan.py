import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Host = input("[*] Enter the host or Ip address to scan ")

Port = int(input("[*] Enter the Port address to scan "))

def portscan(Port):
    if sock.connect_ex((Host,Port)):
        print("port %d is closed" % (Port))
    else:
        print("Port %d is Opened" % (Port))

portscan(Port)
