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
#machine = EnigmaMachine.from_key_sheet(
#       rotors='III II I',
#       reflector='B',
#       ring_settings='A B C',
#       plugboard_settings='AC LS BQ WN MY UV FJ PZ TR OK')
#
#message = stdin.read().rstrip("\n")
#    
#decrypted_message = machine.process_text(message)
#print(decrypted_message)

file = open("codebook_for_ciphertext_final", "r")
lines = []
for line in file:
	lines.append(line.rstrip())

file.close()

file = open("dictionary.txt", "r")
ddict = []
for line in file:
	ddict.append(line.rstrip())

file.close()

# sanitize
for i in range(len(lines)):
    lines[i] = lines[i].split("{} ".format(i+1))[1]
    #print(lines[i].split(" "))

message = stdin.read().rstrip("\n")

for i in range(len(lines)):
    line = lines[i].split(" ")
    #print(line)
    #print(len(line))

    rotor = "{} {} {}".format(line[0], line[1], line[2])
    reflector = "{}".format(line[len(line)-1])
    ring_settings = "{} {} {}".format(line[3], line[4], line[5])
    plugboard_settings = "{} {} {} {} {} {} {} {} {} {}".format(line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15])
    
    machine = EnigmaMachine.from_key_sheet(
        rotors=rotor,
        reflector=reflector,
        ring_settings=ring_settings,
        plugboard_settings=plugboard_settings
    )

    count = 0
    decrypted_message = (machine.process_text(message))
    decrypted_message = machine.process_text(message)
    decrypted_message = decrypted_message.split("X")
    decrypted_message = " ".join(decrypted_message)

    for word in ddict:
        if(word.lower() in decrypted_message.lower()):
            count+=1

    if(count > 1000):
        print(count)
        print("{} {} {}".format(reflector, rotor, ring_settings))
        print(decrypted_message)
    #print("{} {} {}".format(reflector, rotor, ring_settings))
    
    #
    #print(i)