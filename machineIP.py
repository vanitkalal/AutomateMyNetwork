#This code will give the machine's hostname and its IP address

import socket

hostname = socket.gethostname()

IP = socket.gethostbyname(hostname)

print(f'The hostname for this machine is {hostname} and ip is {IP} ')

