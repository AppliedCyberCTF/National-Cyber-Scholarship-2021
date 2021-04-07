# National Cyber Scholarship Competition - Spring 2021
# Script is written for the NM01 flag
# Authored for the Applied Cybersecurity Society by Mobmaker
# https://github.com/Mobmaker55

# Make sure to use Python 2! This script will not work properly on Python 3.

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "cfta-nm01.allyourbases.co"
port = 8017

sock.connect((host, port))
raw = str(sock.recv(4096))
print(raw)
thaw = raw.decode('unicode-escape') 
print(thaw)
sock.send(thaw)
sock.send('\n')
print(str(sock.recv(4096)))
time.sleep(0.5)
print(str(sock.recv(4096)))