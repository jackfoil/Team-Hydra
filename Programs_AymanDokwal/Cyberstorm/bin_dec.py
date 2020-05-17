# Ayman Dokwal
# Intro to Cyber Security
# Program 1

# the import statement for the standard input
from sys import stdin

# the decoding function that takes two parameters
def decode(binary, n):

	# initializing variables
	text = ""
	i = 0

	# converting the binary to ASCII
	while (i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte, 2)

		# removing the letter that was backspaced
		if byte == 8:
			text = text[:-1]
		else:
			text += chr(byte)	
		i += n
	return text

# reading the file into a variable binary
binary = stdin.read().rstrip("\n")

# deciding whether to use 7 or 8 bit
if (len(binary) % 7 == 0):
	text = decode(binary, 7)
	print "7-bit"
	print text
if (len(binary) % 8 == 0):
	text = decode(binary, 8)
	print "8-bit"
	print text

