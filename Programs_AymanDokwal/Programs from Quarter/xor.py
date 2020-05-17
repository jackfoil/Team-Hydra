#########################################
# Ayman Dokwal
# Program 6
# CSC 442
#########################################

import os
import sys

# reading in plaintext or ciphertext file
m = sys.stdin.read()

# retrieving binary data from the "key" binary file
k = open('key.txt', 'rb').read()

result = ""

# looping through each byte in the message text m and xor with the corresponding index from the key k
for i in range(len(m)):
    # because the key can be shorter than the length of the message, mod by the length of the key to loop around
    result += chr(ord(m[i]) ^ ord(k[i%len(k)]))

# printing resulting text to stdout
print(result)
