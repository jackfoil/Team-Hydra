####################################
# Ayman Dokwal
# Intro to Cybersecurity
# Steg Program
####################################


import sys

DEBUG = False

# general usage messages
GENERAL_USAGE = "General Usage: ./steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
STORAGE_USAGE = "Store Data Usage: ./steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> -h<val>"

# sentinel value
SENTINEL = [0,255,0,0,255,0]

# if sentinel is changed, any pieces of code using the length of the sentinel can be automatically adjusted
SEN_LENGTH = len(SENTINEL)


# process the storage of data into a wrapper file
def storeData(wrapper, offset, interval):

	# retrieving file to hide inside of wrapper
	hidden = getHidden()

	# turning wrapper into list to allow for changing of chars at indexes
	wrapper = list(wrapper)

	# using byte or bit method based on args, otherwise specify usage
	if(sys.argv[2] == "-B"):

		# byte method:
        # storing the bytes of the hidden file first into the wrapper
		for i in range(len(hidden)):
			wrapper[offset] = hidden[i]
			offset += interval

		# storing the sentinel into the wrapper
		for i in range(SEN_LENGTH):
                        wrapper[offset] = chr(SENTINEL[i])
			offset += interval


	elif(sys.argv[2] == "-b"):

				# bit method:
                # storing a byte one bit at a time by replacing the LSBs of 8 bytes in the wrapper with the 8 bits of a byte from the hidden file
                for i in range(SEN_LENGTH):
                        hidden += chr(SENTINEL[i])

                hidden = list(hidden)
                for i in range(len(hidden)):
                        # getting int version of the hidden byte
                        curHidden = ord(hidden[i])
                        for j in range(8):
                                # storing current wrapper byte as int
                                curWrapper = ord(wrapper[offset])
                                curWrapper &= 11111110
                                curWrapper |= ((curHidden & 10000000) >> 7)
                                curHidden <<= 1
                                # setting value of wrapper at offset to the new character
                                wrapper[offset] = chr(curWrapper)
                                offset += interval


	# informing user of proper way to use command line arguments
	else:
		print(STORAGE_USAGE)
		exit()


        # displaying results of either method
	print("".join(wrapper))
	if(DEBUG):

                # for debugging, printing out the integer representation and char value of each byte, 1 per line
                hiddenOrd = ""
                for i in range(len(hiddenData)):
                        hiddenOrd += str(ord(hiddenData[i])) + " " + hiddenData[i] + "\n"
                print hiddenOrd


# processing the retrieval of data from
def retrieveData(wrapper, offset, interval):

        # general setup for either method:
        # setup string to hold retrieved hidden bytes from the wrapper
        hiddenData = ""

        # keeping track whether sentinel was found
        found = False

	# using byte or bit method based on args, otherwise specify usage
	if(sys.argv[2] == "-B"):

		# byte method:
		# continue to loop until the sentienl is found, or once the entire wrapper has been traversed
		while (not found and len(wrapper) > offset):

            # adding the byte from the wrapper at the offset to the hidden data, increasing offset by interval after
			hiddenData += ((wrapper[offset]))
			offset += interval

			# check for sentinel once enough data has been retrieved for it to possibly be there
                        if(len(hiddenData) >= SEN_LENGTH):

                                # check to see if the seninel was found
                                for i in range(SEN_LENGTH):

                                        # stop checking once a digit of hidden data doesn't match sentinel
                                        if(ord(hiddenData[i-SEN_LENGTH]) != SENTINEL[i]):
                                                break

                                        # once all pieces of the sentienl were found, remove them from the hidden data string and set found to true
                                        elif(i == SEN_LENGTH-1):
                                                hiddenData = hiddenData[:-SEN_LENGTH]
                                                found = True


	elif(sys.argv[2] == "-b"):

		# bit method:
		# continue to loop until the sentienl is found, or once the entire wrapper has been traversed
		while (not found and len(wrapper) > offset + 7):

                        # holding the resulting byte retrieved from the 8 ending bits
                        hiddenByte = 0
                        for i in range(8):

                                # the wrapper byte with 1 to only get the value of the least significant bit
                                bit = ord(wrapper[offset]) & 1

                                # or the wrapper byte with the current status of the hidden byte to change the LSB of the hiddenByte to the proper bit without changing the remaining bits
                                hiddenByte |= bit

                                # expect for the 8th bit, shift the hidden byte 1 to the left to make room for the remaining bits
                                if(i < 7):
                                        hiddenByte <<= 1

                                # incrementing the offset by the interval to look at the next appropriate wrapper byte
                                offset += interval


                        # adding the newly formed hidden byte to the hidden data string
			hiddenData += chr(hiddenByte)

			# check for sentinel once enough data has been retrieved for it to possibly be there
                        if(len(hiddenData) >= SEN_LENGTH):

                                # check to see if the seninel was found
                                for i in range(SEN_LENGTH):
                                        if(ord(hiddenData[i-SEN_LENGTH]) != SENTINEL[i]):
                                                break

                                        # once all 6 pieces of the sentienl were found, remove them from the hidden data string and set found to true
                                        elif(i == SEN_LENGTH-1):
                                                hiddenData = hiddenData[:-SEN_LENGTH]
                                                found = True


	# informing user of proper way to use command line arguments
	else:
		print(GENERAL_USAGE)
		exit()


    # finishing steps for either method:
	# sending hidden data to standard output
        print(hiddenData)
        if(DEBUG):

                #for debugging, print out the integer representation and char value of each byte, 1 per line
                hiddenOrd = ""
                for i in range(len(hiddenData)):
                        hiddenOrd += str(ord(hiddenData[i])) + " " + hiddenData[i] + "\n"
                print hiddenOrd


# retrieving file to hide inside of wrapper from current directory based on command line arg
def getHidden():
	if(sys.argv[-1][:2] == "-h"):
        # removing trailing newline inserted from opening
		return open(sys.argv[-1][2:], 'rb').read()[:-1]

	# informing user that hidden file is required for storage mode
	else:
		print(STORAGE_USAGE)
		exit()


# ensure a wrapper file was provided in command line arg from current directory and open it
def getWrapper():
	if(sys.argv[-1][:2] == "-w"):
                # removing trailing newline inserted from opening
		return open(sys.argv[-1][2:], 'rb').read()[:-1]

	elif(sys.argv[-2][:2] == "-w"):
                # removing trailing newline inserted from opening
		return open(sys.argv[-2][2:], 'rb').read()[:-1]

	# informing user of proper usage and exit
	else:
		print(GENERAL_USAGE)
		exit()


# ensuring interval was specified and return its value if so
def getInterval():

	# returning the interval if found
	if(sys.argv[4][:2] == "-i"):
		return int(sys.argv[4][2:])

	# using a default interval of 1 otherwise
	else:
                return 1


# ensuring an offset was specified and return its value if so
def getOffset():

	# returning the offset if found
	if(sys.argv[3][:2] == "-o"):
		return int(sys.argv[3][2:])

	# informing user of proper usage and exit
	else:
		print(GENERAL_USAGE)
		exit()



# read in arguments from the command line, specifying proper usage if necessary
if(len(sys.argv) < 5):
	print(GENERAL_USAGE)
	exit()

# ensuring wrapper file provided (needed regardless of method used)
wrapper = getWrapper()

# ensuring offset specified
offset = getOffset()

# getting interval from args (or use 1 if none provided, common for bit method)
interval = getInterval()

# go to the appropriate function to store (hide) data or retrieve it
if(sys.argv[1] == "-s"):
	storeData(wrapper, offset, interval)
elif(sys.argv[1] == "-r"):
	retrieveData(wrapper, offset, interval)

# invalid mode specified
else:
	print(GENERAL_USAGE)
