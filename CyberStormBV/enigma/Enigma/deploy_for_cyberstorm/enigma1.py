# -*- coding: utf-8 -*-
"""
Template for enigma machine challange
See https://py-enigma.readthedocs.io/en/latest/guide.html#building-your-enigma-machine
for more information
"""


from enigma.machine import EnigmaMachine
from sys import stdin, stderr

#All Wehrmacht models
LIST_OF_ROTORS = ['I','II','III','IV', 'V']
#Kriegsmarine M3 & M4
#LIST_OF_ROTORS = ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII']

#X is not in use, to make your life easier
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

#there are more reflectors, but this will be bad enough for you to deal with.
LIST_OF_REFLECTORS = ['B', 'C']

#This is one way to create an enigma machine, there are others ;)
machine = EnigmaMachine.from_key_sheet(
       rotors='III II I',
       reflector='B',
       ring_settings='A A A',
       plugboard_settings='AB CD EF GH IJ KL MN OP QR ST')

message = stdin.read().rstrip("\n")
    
decrypted_message = machine.process_text(message)
decrypted_message = decrypted_message.split("X")
decrypted_message = " ".join(decrypted_message)
print(decrypted_message)