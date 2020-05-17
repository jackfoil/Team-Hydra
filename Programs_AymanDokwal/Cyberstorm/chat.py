####################################################
# Ayman Dokwal
# April 22, 2020
# Chat Covert Channel Program
####################################################

from time import time
import socket
import sys

DEBUG = False

# server information
PORT = 12321
IP = "138.47.99.163"

# server information for localhost for testing
#PORT = 1337
#IP = "localhost"

# timings that output a 1 or 0 for the covert message
zero = .1
one = .151

#use average time to account for variation
avg = (one + zero)/2


# function for coverting to ASCII taken from the binary decoder program
def convertASCII(binaryInput, binaryLength, numBits):
	
	finalString = ""
	
	# looping through indexes such that i = the 0th bit in every sequence of numbits
	for i in range(0, binaryLength-(numBits-1), numBits):

                # getting the ASCII number for the bits
		num = int(binaryInput[i:i+numBits], 2)

                # checking if the num will produce a backspace, which is ASCII value 8
		if(num == 8):
                        # removing the trailing character from the string
			finalString = finalString[:-1]
		   
		else:
			# converting into an integer that is base 2 and then using chr to convert the integer into the equivalent ASCII character
			finalString += chr(num)
		
	print("Covert message: {}".format(finalString))


# retrieving the message with timings to get bits for the covert message
def getCov(s):

        # hold the binary for the covert message
        covBin = ""

        # retrieving the first char outside the loop
        data = s.recv(4096)

        # loop until an EOF is received
        while (data.rstrip("\n") != "EOF"):

                # displays the held character
                sys.stdout.write(data)
                sys.stdout.flush()

                # times the retrieval of the next character
                start = time()
                data = s.recv(4096)
                end = time()

                # determining what range the time falls into to add a 1 or 0 to the covert string
                delta = round(end-start, 3)
                if (DEBUG):
                        print("")
                        print (delta)

                # using the average time to account for variations
                if(delta >= avg):
                        covBin += "1"
                else:
                        covBin += "0"


        print("...\n[disconnect from the chat server]")

        # closing out of the server and display the converted output
        s.close()

        if(DEBUG):
                print(covBin)
                
        convertASCII(covBin, len(covBin), 8)



# main
# displays the overt message and generate the bits of the covert message based on the timing of retrieving the characters
# setup connection to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
print ("[connect to the chat server]\n...")

# gets the covert message
getCov(s)
