## Name: Jack Foil
## Date: 5/4/2020
##Topic: XOR, USE python 2.7!!
#############################################

from sys import stdin
from sys import stdout
import sys


message = stdin.read()
byte_mes = bytearray(message)

######OXRs the key with other
def XOR(mes, key):
    sub_key = key
    sub_mes = mes
    keybin = ""
    mesbin = ""
    text = ""

    # makes sure that the key is same length
    while(len(sub_mes) > len(sub_key)):
        sub_key += str(key)

    while(len(sub_mes) < len(sub_key)):
        sub_key = sub_key[:-1]

    while(len(sub_mes) < len(sub_key)):
        sub_mes += str(mes)

    while(len(sub_mes) > len(sub_key)):
        sub_mes = sub_mes[:-1]

    # XORS the message
    xor_mes = bytearray(len(sub_mes))
    test = ""
    for j in range(len(xor_mes)):
        keybin = str(bin(sub_key[j]))[2:].zfill(8)
        mesbin = str(bin(sub_mes[j]))[2:].zfill(8)        
        test += bin(int(keybin, 2) ^ int(mesbin, 2))[2:].zfill(8)

    # turns those bites into characters      
    i = 0
    while(i < len(test)):
        byte = test[i:i+8]
        print byte
        byte = int(byte, 2)
        text += chr(byte)
        print chr(byte)
        i +=8
        
    
    return text


# Read the key from a file as binary data (consider bytearray)
file = open("key.txt", "r")
a = ""
for line in file:
    a +=(line)
KEY = bytearray(a)


#stdout the cipher text
cipher_text = XOR(byte_mes, KEY)
sys.stdout.write(cipher_text)
