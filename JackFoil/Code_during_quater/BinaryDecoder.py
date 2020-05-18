#######################################################################
#Name: Jack Foil
#Date: 3/20/2020
# Description: Binary Decoder
#######################################################################
from sys import stdin


#function deocodes the binary
def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte, 2)

        #if the byte is a backpace it will produce a backpace
        if(byte == 8):
            arrOfStr = text.split()
            temp =""
            for a in arrOfStr:
                temp += a[0:len(a)-1]
            text = temp
        #if not it will add the character into the text string 
        else:
            text += chr(byte)
        i+=n
    #return the decoded message
    return text




##reads the standard input
binary = stdin.read().rstrip("\n")


###finds the length of the input and sees if it is divisible by 8 or 7 to disginish
##if it is ASCII 7 or 8
if(len (binary) % 7 ==0):
    ###sends that string of binary to the decode function
    text = decode(binary, 7)
    #prints the final result
    print "7-bit:"
    print text

    
if(len(binary) % 8 == 0):
    ###sends that string of binary to the decode function
    text = decode(binary, 8)
    #prints the final result
    print "8-bit:"
    print text





