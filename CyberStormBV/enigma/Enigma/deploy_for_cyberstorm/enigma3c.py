# -*- coding: utf-8 -*-
"""
Template for enigma machine challange
See https://py-enigma.readthedocs.io/en/latest/guide.html#building-your-enigma-machine
for more information
"""


from enigma.machine import EnigmaMachine
from sys import stdin, stderr
from itertools import permutations, combinations

#All Wehrmacht models
LIST_OF_ROTORS = ['III I II']
#Kriegsmarine M3 & M4
#LIST_OF_ROTORS = ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII']

RING_SETTINGS = ["B D J"]

USED_PLUGBOARD = ["LO", "KI", "JU", "HY", "GT", "FR", "DE", "SW", "QA"]

#X is not in use, to make your life easier
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

#PLUBBOARD_COMBINATIONS = []

#there are more reflectors, but this will be bad enough for you to deal with.
LIST_OF_REFLECTORS = ['B']

message = stdin.read().rstrip("\n")

for i in list(permutations(LIST_OF_REFLECTORS)):
    reflector = i[0]
    for j in list(permutations(LIST_OF_ROTORS)):
        rotor = " ".join(j)
        for k in list(permutations(RING_SETTINGS)):
            ring_settings = " ".join(k)
            for combo in combinations(ALPHABET, 2):  # 2 for pairs, 3 for triplets, etc
                for l in list(permutations(combo)):
                    #print combo
                    try:
                        #This is one way to create an enigma machine, there are others ;)
                        machine = EnigmaMachine.from_key_sheet(
                            rotors="III I II",
                            reflector="B",
                            ring_settings="B D J",
                            plugboard_settings='LO KI JU HY GT FR DE SW QA {}'.format("".join(l)))
                            
                        decrypted_message = machine.process_text(message)
                        decrypted_message = decrypted_message.split("X")
                        decrypted_message = " ".join(decrypted_message)
                        print("{} {} {} LO KI JU HY GT FR DE SW QA {}".format(reflector, rotor, ring_settings, "".join(l)))
                        #print("{} {} {}".format(reflector, rotor, ring_settings))
                        print(decrypted_message)
                    except:pass