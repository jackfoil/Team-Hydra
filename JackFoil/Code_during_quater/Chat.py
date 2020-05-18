#Name: Jack Foil
# Date: 4/20/2020
# Topic: Chat program
#####I am using Python 2.7
##########################################################
import socket
from sys import stdout
from time import time
import binascii


# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = 12321
port = "138.47.99.163"

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))


#variables / constants
covert_bin = ""
ZERO = 0.025
ONE = .15



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
        if(delta >= ONE):
            covert_bin += "1"
        else:
            covert_bin += "0"

	# Will print out the timming if DEBUG is true 
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()



#converts the binary into something readable
covert = ""
i = 0
while (i < len(covert_bin)):
    b = covert_bin[i:i+8]
    n = int("0b{}".format(b), 2)
    try:
        covert += binascii.unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i +=8


#prints the covert message and closes the connection
print "Covert message: " + str(covert)
s.close()













