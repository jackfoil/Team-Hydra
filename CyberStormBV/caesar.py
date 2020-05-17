# Made with Python 2.7.16
# Brandon Vessel
# CSC 442 / CYEN 301
# caesar cipher
# May 5, 2020

# Purpose: to encode or decode a message using a Vigenere cipher

from sys import stdin, argv

# setup whitelist rings
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers   = "0123456789"
custom    = ""

table = [uppercase, lowercase, numbers, custom]

inclusions = [True, True, True, False]

# create character whitelist from rings
whitelist = []
for i in range(len(table)):
    if(inclusions[i]):
        for character in table[i]:
            whitelist.append(character)

whitelist = "".join(whitelist)


# shift characters in a string
def shift(text, key):
    text = list(text)

    # iterate key
    for i in range(len(text)):
        # check whitelist
        if(text[i] in whitelist):
            # iterate tables
            for j in range(len(table)-1):
                # if character in table
                if(text[i] in table[j]):
                    # change character by key. mod to length of the table used
                    text[i] = table[j][(char_to_int(text[i]) + key) % (len(table[j]))]
                    break

    return "".join(text)


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
    # get piped input
    text = stdin.read()
    
    # remove newlines
    text = text.replace("\n", "")

    # read arguments
    if(len(argv) == 1):
        # bruteforce mode
        for i in range(0, 26):
            print("shift {} or {}: {}".format(i, abs(26-i), shift(text, i)))
    else:
        if(len(argv) == 2):
            key = argv[1]
            print(shift(text, key))

        else:
            print("usage: python {} [key]".format(argv[0]))
