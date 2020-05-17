# -*- coding: utf-8 -*-
"""
Template for enigma machine challange
See https://py-enigma.readthedocs.io/en/latest/guide.html#building-your-enigma-machine
for more information
"""


from enigma.machine import EnigmaMachine
from sys import stdin, stderr

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
    decrypted_message = decrypted_message.lower().split("x")

    for word in decrypted_message:
        if(word in ddict):
            #print(word)
            count += 1

    #for word in ddict:
    #    if(word.lower() in decrypted_message):
    #        count+=1
    #print(count)
    if(count > int(len(decrypted_message)*.35)):
        for word in decrypted_message:
            if(word in ddict):
                print(word)
        #print(count)
        #print("{} {} {}".format(reflector, rotor, ring_settings))
        decrypted_message = " ".join(decrypted_message)
        #print(decrypted_message.upper())
    #print("{} {} {}".format(reflector, rotor, ring_settings))
    
    #
    #print(i)