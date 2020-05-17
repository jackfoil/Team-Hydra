# Ayman Dokwal
# Intro to Cybersecurity
# Program 2: Vigenere Cypher
# Using Python 2.7
################################################################


from sys import stdin, argv
from array import *
import string


# the string of all lowercase and uppercase letters in that order
alphabet = string.ascii_letters

# setting the arguments as variables
mode = argv[1]
key = argv[2]

# this function takes an array of numbers and non-alphabet symbols to convert to the new text which is either plaintext or ciphertext
def new_text(code):
        final = ""
        for i in code:
        
                if(isinstance(i, int)):
                        # the ints in the code array match to indexes of corresponding letters in alphabet, so that letter is appended to the text
                        final += alphabet[i]
                        
                else:
                        # all the other indexes in code array will be in another array that holds a non-alphabetic symbol from the inputed text that is preserved to be put into the new text
                        final += i[0]              
        return final


# takes in key with the plaintext to encrypt
def encrypt(string, key):

        # the int shows how many non-alphabetic symbols have been processed 
        # the symbols are not modified in the cipher, the key should not advance
        # an index after processing one, so this int compensates for the offset between key index and string index
        nonAlphabet = 0
        ciphertext = []
        key = space(key)

        # encrypting indexes of the inputted string
        for i in range(len(string)):
                
                # checking if a non-alphabetic symbol is present
                if(not (string[i] in alphabet)):
                
                        # appending the non-alphabetic symbol and incrementing the counter
                        ciphertext.append([string[i]])
                        nonAlphabet += 1
                        
                else:

                        # using an encryption equation: [ciphertext at index i =(plaintext at i + key at i)%26]
                        # the mod is taken to loop back around just in case the key is too short
                        index = ((alphabet.index(string[i]) + alphabet.index(key[((i-nonAlphabet) % len(key))])) % 26)

                        # for uppercase letters, add 26 to go from lowercase to uppercase
                        if(string[i].isupper()):
                                index += 26
                                
                        ciphertext.append(index)

        # sending the ciphertext to stdout
        print (new_text(ciphertext))


# takes in key with the plaintext to decrypt
def decrypt(string, key):

        nonAlphabet = 0
        plaintext = []
        key = space(key)
        
        # decrypting indexes of the inputted string
        for i in range(len(string)):
                
                # checking if a non-alphabetic symbol is present
                if(not (string[i] in alphabet)):
                        plaintext.append([string[i]])
                        nonAlphabet += 1
                        
                else:
                        # using a decryption equation:[plaintext at index i =(ciphertext at i + key at i)%26]
                        # the mod is taken to loop back around just in case the key is too short
                        index = ((26 + alphabet.index(string[i]) - alphabet.index(key[((i-nonAlphabet) % len(key))])) % 26)

                        # for uppercase letters, add 26 to go from lowercase to uppercase
                        if(string[i].isupper()):
                                index += 26
                                
                        plaintext.append(index)

        # sending resulting plaintext to stdout
        print (new_text(plaintext))


# this function is here to take the spaces out of the key
def space(key):
        key = key.split()
        key = "".join(key)
        return key

        
# making sure that the usage is correct depending on the length of the arguments given and displaying the proper way to run
if(len(argv) < 3):
	print("Usage: ./vigener-cipher.py -[d or e] KEY")
	exit()


# determining the modes, whether to encrypt or decrypt
if(mode == "-d"):

	# processes all inputs from stdin as ciphertext
        text = stdin.readline()
        while(text):
        
                # this is to split off the newline
                text = text.split('\n')
                decrypt(text[0], key)
                text = stdin.readline()

elif(mode == "-e"):

	# processes all inputs from stdin as plaintext
	text = stdin.readline()
        while(text):
        
                # this is to split off the newline
                text = text.split('\n')
                encrypt(text[0], key)
                text = stdin.readline()

# making sure the usage is correct and displaying the proper way to run
else:
	print("Usage: ./vigener-cipher.py -[d or e] KEY")