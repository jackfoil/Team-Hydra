# Made with Python 2.7.16
# Brandon Vessel
# CSC 442 / CYEN 301
# Chat Covert Channel
# April 24, 2020

import socket
from sys import stdout
from time import time

## CONFIG ##

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.102.67"
port = 33333

# delay config
delay_0 = 0.1
delay_1 = 0.2

## FUNCTIONS ##

# returns the closest value in a list to the given value
def closest(lst, value): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-value))]


# converts binary to text give a string and bit length
# from Binary.py. modified for this program
def binary_to_text(data, step):

    fstring = []

    data = list(data)

    while(len(data) != 0):
        character = []
        # try catch in case of improper step
        try:
            for i in range(step):
                # pop off only the characters we need
                character.append(str(data.pop(0)))
        except:pass
        
        # make it a string
        character = "".join(character)

        # convert to ascii number base 10
        character = int(character, 2)

        # check for backspace
        if(int(character) == 8):
            # delete character before backspace
            NULL = fstring.pop()

        # check for tab
        elif(int(character) == 9):
            # tab
            fstring.append("\t")
        # check for carraige return
        elif((int(character) == 10) or (int(character) == 13)):
            # new line
            fstring.append("\n")
        # check to see if the character is even valid
        elif(int(character) > 127):
            fstring.append("?")
        else:
            # add character to string list as an ascii character instead of its number
            fstring.append(chr(character))
        
    # return binary string
    return "".join(fstring)


## MAIN CODE ##

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# covert message list
# pre-populate the covert_message list to prevent time delays from python reallocating the list
covert_message = []
for i in range(0,10000):
    covert_message.append(0.11)

# length of the message. gets longer as the message is recieved
message_length = 0

# receive data until EOF
data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)

    # add delta to the covert message list
    covert_message[message_length] = delta
    message_length+=1

    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

# close the connection to the server
s.close()

# chop the bits we don't need
covert_message = covert_message[0:message_length]

# delays to binary
for i in range(len(covert_message)):
    value = closest([delay_0, delay_1], covert_message[i])
    if(value == delay_0):
        covert_message[i] = 0
    else:
        covert_message[i] = 1

if(DEBUG):
    print(covert_message)

# translate to message
message = binary_to_text(covert_message, 8)
print("\nCovert message:{}".format(message.split("EOF")[0]))
if(DEBUG):
    print("Raw message: {}".format(message))