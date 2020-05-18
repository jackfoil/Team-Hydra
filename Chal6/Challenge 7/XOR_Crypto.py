###################################################
# By: Cole Edwards
# Date: 5.6.2020
# Python 2.7.17
###################################################
from sys import stdin, stdout

#get key from a file in the directory
with open('', 'r') as file:
    temp = file.read()
#create the bytearray
key = bytearray(temp)

#get the text that will be XOR'd with the key
temp = stdin.read().rstrip("\n")
#create the bytearray
text = bytearray(temp)

#XOR the key and text
i = 0
msg = bytearray()
while(i < len(key)):
    msg.append(key[i] ^ text[i])
    i += 1

#output the msg
stdout.write(msg)
