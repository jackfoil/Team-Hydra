# Ayman Dokwal
# April 1, 2020
# Program 3: FTP Covert Channel
###############################################################################


import ftplib

# global variable to select number of bits to use
numbits = 7

# global variable to select mode (0 (7-bit) or 1 (10-bit))
method = 0

# global variable for the string of the FTP server
# for this program, it is jeangourd.com
ser = 'www.jeangourd.com'

# global variable for directory within server
direct = ''

# adjusts the directory based on the method variable above
if (method == 0):
	direct = '7'
else:
	direct = '10'

# data recieved variable
data = []

# converting into string
def convert_ASCII(binaryInput, binaryLength):
	finalString = ""
	
	# looping through indexes such that i = the 0th bit in every sequence of numbits
	# from the binary decoding program
	for i in range(0, binaryLength-(numbits-1), numbits):

		# getting the ASCII number for the bits
		num = int(binaryInput[i:i+numbits], 2)

		# checking if the num will produce a backspace, which is ASCII value 8
		if(num == 8):

			# removing the trailing character from the string
			finalString = finalString[:-1]
		   
		else:
			# converting into an integer that is base 2 and then using chr to convert the integer into the equivalent ASCII character
			finalString += chr(num)
		
	print(finalString)
	return


# appending all permission data in the DIR directory in the server to the data array
def retrieve_Data():
	
	server.dir(direct, data.append)

	# looping through each line of data retrieved (1 line/index of the data array)
	for i in range(len(data)):

		# removing all but the first 10 characters of each line, so that we only get the permissions info
		data[i] = data[i][0:10]
		i=i+1


# generating a binary string based on the permissions
def generate_String():
	
	string = ''

	# based on method specified, it processes data accordingly
	if (method == 0):

		# 7-bit method
		for line in data:

			# only processes lines of data that have all '-' for the first 3 characters
			if line [:3] == ('---'):

				# for the remaining 7-bits, append a 0 to the string for any '-', else 1
				for letter in line[3:]:
					if (letter ==  ('-')):
						string += "0"
					else:
						string += "1"

	else:

		# 10-bit method
		for line in data:

			# appending 0 to string for any '-', else 1
			for letter in line:
				if (letter ==  ('-')):
					string += "0"
				else:
					string += "1"

	# output the 7-bit ASCII version
	convert_ASCII(string, len(string))

	
# setting up connection to server
server = ftplib.FTP()
server.connect(ser)
server.login('anonymous')

# retrieving the permissions data from server
retrieve_Data()

# generating the binary string and print the 7-bit ASCII version
generate_String()






