import socket
from binascii import hexlify


print ('Enter the IP address that you want to convert')
x = input()

packedIP = socket.inet_aton(x)
unpackedIP = socket.inet_ntoa(packedIP)

print(f'The packed IP is {hexlify(packedIP)} and unpacked ip is {unpackedIP}')
