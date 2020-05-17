# Made with Python 2.7.16
# Brandon Vessel
# CSC 442 / CYEN 301
# Binary Decoder
# March 30, 2020

# Purpose: to decode a binary string into it's ascii representation and output it

from sys import stdin

def decipher(data, step):

    fstring = []

    while(len(data) != 0):
        character = []
        # try catch in case of improper step
        try:
            for i in range(step):
                # pop off only the characters we need
                character.append(data.pop(0))
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
        else:
            # add character to string list as an ascii character instead of its number
            fstring.append(chr(character))
        
    # combine and print final string    
    print("".join(fstring))


### parse stdin
text = stdin.read().rstrip()

## make it a string if it isn't already. sanitize
data = str(text).rstrip("\n")

## break up the string into characters
data = list(data)

## determine if it is 8 or 7 bit ascii
if(len(data) % 8 == 0):
    step = 8
elif(len(data) % 7 == 0):
    step = 7
else:
    print("[ERROR] Invalid bit length\nattempting print of both")
    decipher(data, 7)
    decipher(data, 8)
    exit()

## check for double validation
if((len(data) % 7 == 0) and (len(data) % 8 == 0)):
    # data is valid for 7 and 8, print them both
    print("Data is valid for 7 and 8 bit,\nprinting both")
    decipher(data, 7)
    decipher(data, 8)
else:
    # data is normal
    decipher(data, step)
