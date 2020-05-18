# Made with Python 2.7.18
# Brandon Vessel
# CSC 442 / CYEN 301
# XOR
# May 8, 2020

from sys import stdout, stdin

# the file for the binary key
key_file = "key.txt"


def XOR(message, key):
    '''XOR a message with a key'''
    # get key length
    key_length = len(key)

    # bytearray for xor'd message
    result = bytearray(len(message))

    # xor message
    for i in range(len(message)):
        # message byte to the power of (key[i mod key_length])
        result[i] = (message[i] ^ key[i % key_length])

    # write the result to stdout
    stdout.write(result)


if __name__ == "__main__":
    # convert message to bytearray
    message = bytearray(stdin.read())

    # convert key to bytearray
    key = bytearray(open(key_file, mode="r").read())

    # xor the message with the key
    XOR(message, key)
