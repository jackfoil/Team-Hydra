# Made with Python 2.7.16
# Brandon Vessel
# CSC 442 / CYEN 301
# Vigenere Cipher
# March 30, 2020

# Purpose: to encode or decode a message using a Vigenere cipher

from sys import stdin, argv


# confirm arguments
if(len(argv) != 3):
    print("Invalid syntax\nUsage: python {} (-e/-d) <key>".format(argv[0]))
    exit()


# setup whitelist rings
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers   = "0123456789"
custom    = ""

table = [uppercase, lowercase, numbers, custom]

inclusions = [True, True, False, False]

# create character whitelist from rings
whitelist = []
for i in range(len(table)):
    if(inclusions[i]):
        for character in table[i]:
            whitelist.append(character)

whitelist = "".join(whitelist)

# encrypt a string given a key
def encrypt(text, key):
    text = list(text)

    key_index = 0

    # iterate key
    for i in range(len(text)):
        # check whitelist
        if(text[i] in whitelist):
            # iterate tables
            for j in range(len(table)-1):
                # if character in table
                if(text[i] in table[j]):
                    # change character by key. mod to length of the table used
                    text[i] = table[j][(char_to_int(text[i]) + key[key_index]) % (len(table[j]))]

                    # increment key
                    key_index += 1
                    
                    # prevent key overflow
                    if(key_index == len(key)):
                        key_index = 0


    return "".join(text)

# decrypt a string given a key
def decrypt(text, key):
    # vigenere is symmetrical, so why not abuse it by negating the key!
    for i in range(len(key)):
        key[i] = -key[i]
    return encrypt(text, key)


# convert a character to an position in the appropriate ring
def char_to_int(character):
    # iterate through rings
    for j in range(len(table)-1):
        # if character in ring
        if(character in table[j]):
            # return value as position in correct ring
            return table[j].index(character)


# MAIN
if(__name__ == "__main__"):

    # read arguments

    mode = argv[1]
    key = argv[2]

    # convert key characters into usable values
    num_key = []
    for i in range(len(key)):
        # space check and whitelist check
        if(key[i] != " " and key[i] in whitelist):
            num_key.append(char_to_int(key[i]))

    # get text input
    text = stdin.read().rstrip("\n")
    print("Message:{}".format(text))
    
    # encrypt or decrypt
    if (mode == "-e"):
        # encrypt
        ciphertext = encrypt(text, num_key)
        print("Cipher:{}".format(ciphertext))

    elif (mode == "-d"):
        # decrypt
        plaintext = decrypt(text, num_key)
        print("Plaintext:{}".format(plaintext))
    else:
        print("INVALID PARAMETERS\nUsage: python {} (-e/-d) <some key>".format(argv[0]))
        exit()