###################################################
# By: Cole Edwards
# Date: 4.21.2020
# Python 2.7.17
###################################################
import socket
from sys import stdout
from time import time
from binascii import unhexlify

DEBUG = False

ip = "138.47.99.163" #challenge
port = 12321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

ZERO = 0.15 #0.1
ONE = 0.2 #0.2
#Had to lower ONE due to the lag between windows and the server (Not on campus)

covert_bin = ""
covert = ""
i = 0


data = s.recv(4096)
while(data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()
    t0 = time()
    data = s.recv(4096)
    t1 = time()

    delta = round(t1 - t0, 3)
    if(delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"

    if(DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

s.close()

while(i < len(covert_bin)):
    b = covert_bin[i:i+8]
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i += 8
stdout.write(covert)
stdout.write("\n")
stdout.flush()
