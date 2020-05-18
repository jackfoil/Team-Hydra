###################################################
# By: Cole Edwards
# Date: 3.27.2020
# Python 2.7
###################################################

from sys import stdin

def decode(binary, n):
    text = ""
    i = 0
    while(i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte, 2)
        #check for a backspace
        if(byte == 8):
            #if found, truncate the last letter added
            text = text[:-1]
        else:
            #if not, add the next letter
            text += chr(byte)
        #increment
        i+=n

    return text

binary = stdin.read().rstrip("\n")
print "binary", len(binary)

#decide if the binary number given is ASCII 7 or 8 bit
if(len(binary) % 7 == 0):
    text = decode(binary, 7)
    print "7-bit:"
    print text
if(len(binary) % 8 == 0):
    text = decode(binary, 8)
    print "8-bit:"
    print text
