#Name: Jack Foil
#Date: 5/5/2020
#Porgram: Steg / Python 2.7
########################################################
# Libraries 
from sys import stdin, argv
import sys
import re


#Reads the users input from the cmd 
a = 1
offset = 0 # sets the deflaut
interval = 1 # sets the default
bit_mode = False
byte_mode = False
store_mode = False
retrieve_mode = False
hidden = None


while(a < len(argv)):
    # store and retrieve mode
    if("-s" == argv[a][0:2]):
        store_mode = True
        
    elif("-r" == argv[a][0:2]):
        retrieve_mode = True

    #Byte and bit mode
    elif("-b" == argv[a][0:2]):
        bit_mode = True
        
    elif("-B" == argv[a][0:2]):
        byte_mode = True

    #offset and interval 
    elif("-o" == argv[a][0:2]):
        offset = int(argv[a][2:len(argv[a])])
        
    elif("-i" == argv[a][0:2]):
        interval = int(argv[a][2:len(argv[a])])

    #wrapper file  and hidden file   
    elif("-w" == argv[a][0:2]):
        filename = argv[a][2:len(argv[a])]
   
    elif("-h" == argv[a][0:2]):
        hidden = argv[a][2:len(argv[a])]

    else:
        print "Please put the following in cmd: "
        print "python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
    a +=1



#IMPORTANT VARIABLES
# Read the wrapper data from a file as binary data (filename and hidden)
wrapper = open(filename, 'rb')
wrapper_byte = bytearray(wrapper.read())

if (hidden != None):
    secret = open(hidden, 'rb')
    secret_byte = bytearray(secret.read())


# creates the sentinel
sentinel = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]


'''
FOUR FUNCTIONS:
1. BYTE STORE
2. BYTE EXTRACT
3. BIT  EXTRACT
4. BIT STORE
'''
##############################################IMPORTANT FUNCTIONS
#storage of the hidden data through bytes
def Byte_storage():
    global offset
    offsets = int(offset)
    

    i = 0
    # Take cares of hidding all hidden bytes into wrapper
    while i < len(secret_byte):
        wrapper_byte[offsets] = secret_byte[i]
        offsets += interval
        i +=1

    # adding the sentineal in the end of the wrapper
    i = 0
    while i < len(sentinel):
        wrapper_byte[offsets] = sentinel[i]
        offsets +=  interval
        i +=1
    text = ""
    i = 0
    while i < len(wrapper_byte):
        text += chr(wrapper_byte[i])
        i +=1
        
    return text


##extracts the secret meassage using the byte message
def Byte_Extract():
    global offset
    global wrapper_byte
    secret = ""

    while offset < len(wrapper_byte):
        b = wrapper_byte[offset]
        i = 0
        c = 0
        copy_pred = [b]
        
        # makes a copy of the next 7 bytes and makes a prediction
        while(i < 5):
            try:
                c+= interval       
                copy_pred.append(wrapper_byte[offset+c])
                i += 1
            except IndexError:
                i = 100
       
        # checks to see if sentinal is equal to the next 6 bytes
        # if it is it will return the secret message
        a =0
        while a < len(sentinel):
            if(copy_pred[a] == sentinel[a] and (a+1) == len(sentinel)):
                return secret
            elif(copy_pred[a] == sentinel[a]):
                a +=1
            else:
                a = 1000

        #adss the byte into the sectet 
        secret += chr(b)
        offset += interval


#Stores the hidden message using bit form
def Bit_storage():
    global offset
    global secret_byte
    i = 0
    offset = 0
    while i < len(secret_byte):
        for j in (0, 7):
            wrapper_byte[offset] &= 11111110
            wrapper_byte[offset] |= ((secret_byte[i] & 10000000) >> 7)

            # moves everything to the left by one
            secret_byte[i] = (secret_byte[i] << 1) & (2**8 -1)
            offset += interval
        i += 1
    
    i = 0
    while i < len(sentinel):
        for j in (0,7):
            wrapper_byte[offset] &= 11111110
            wrapper_byte[offset] |= ((sentinel[i] & 10000000) >> 7)

            # moves everything to the left by one
            sentinel[i] = (sentinel[i] << 1) &(2**8 -1)
            offset += interval
        i += 1

    
    text = ""
    i = 0
    while i < len(wrapper_byte):
        text += chr(wrapper_byte[i])
        i +=1
    
    return text


# uses the bit form to extract the hidden message 
def Bit_Extraction():
    global offset
    sec = bytearray()
    while offset < len(wrapper_byte):
        b = 0

        for j in range(7):
            b |= (wrapper_byte[offset] & 00000001)
            if(j < 7):
                b <<= 1
                offset += interval

        wrapper_byte += b
        offset += interval
    secret += chr(b)
    offset += interval
     


# Main Part Of the Code
#Example: python Steg.py -s -B -o1024 -i2 -wdogs.jpg -hnew.jpg > output
if(byte_mode == True and store_mode == True):
    print Byte_storage()

# Example: python Steg.py -r -B -o1025 -i2 -wsteg.bmp > output
if(byte_mode == True and retrieve_mode == True):
    print Byte_Extract()


# Example: python Steg.py -s -b -o01024 -wdogs.jpg -hnew.jpg > output 
if(bit_mode == True and store_mode == True):
    print Bit_storage()

# Example: python Steg.py -r -b -o1024 -wsteg.bmp > output
if(bit_mode == True and retrieve_mode == True):
    print Bit_Extract()


