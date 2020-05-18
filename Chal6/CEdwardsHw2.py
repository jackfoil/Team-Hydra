####################################
# By: Cole Edwards
# Date: 3.27.2020
# Python: 2.7
####################################

from sys import stdin, argv

mode = argv[1]
key = argv[2].replace(" ","").lower()
text = stdin.read().rstrip("\n")

def encrypt(plaintext, key):
    upper = False
    disregard = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    exceptions = [".",","," ","?","!","'",'"',"(",")","0","1","2","3","4","5","6","7","8","9",]
    i = 0
    n = 0
    
    while(i < len(plaintext)):
        #check to see if the key needs to be wrapped
        if(n > len(key)-1):
            n = 0

        if(plaintext[i] in exceptions):
            disregard = True
            Pi = plaintext[i]    
        #check to see if the letter we are about to add is uppercase
        elif(plaintext[i].isupper()):
            #if it is, set upper to true
            upper = True
            #then make the letter lowercase to find the numbers
            Pi = alphabet.index(plaintext[i].lower())
        else:
            #if it's not uppercase, find normally
            Pi = alphabet.index(plaintext[i])
            
        if(disregard == False):    
            #find the letter in the key in the alphabet
            Ki = alphabet.index(key[n])
            
            #main equation
            Ci = (Pi + Ki) % 26

            #if the letter was originally capitalized,
            # make that letter uppercase
            if(upper):
                ciphertext += alphabet[Ci].upper()
                #make it false so every letter will not become uppercase
                upper = False
            else:
                #else, the letter was already lowercase
                ciphertext += alphabet[Ci]

            #Increment variable
            n+=1
            
        else:
            ciphertext += Pi
            disregard = False
            
        #Increment variable  
        i+=1
    
    return ciphertext

def decrypt(ciphertext, key):
    upper = False
    disregard = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    exceptions = [".",","," ","?","!","'",'"',"(",")","0","1","2","3","4","5","6","7","8","9",]
    plaintext = ""
    i = 0
    n = 0

    while(i < len(ciphertext)):
        #check to see if the key needs to be wrapped
        if(n > len(key)-1):
            n = 0

        if(ciphertext[i] in exceptions):
            disregard = True
            Ci = ciphertext[i]    
        #check to see if the letter we are about to add is uppercase
        elif(ciphertext[i].isupper()):
            #if it is, set upper to true
            upper = True
            #then make the letter lowercase to find the numbers
            Ci = alphabet.index(ciphertext[i].lower())
        else:
            #if it's not uppercase, find normally
            #print ciphertext[i]
            Ci = alphabet.index(ciphertext[i])
            
        if(disregard == False):    
            #find the letter in the key in the alphabet
            Ki = alphabet.index(key[n])
            
            #main equation
            Pi = (26 + Ci - Ki) % 26

            #if the letter was originally capitalized,
            # make that letter uppercase
            if(upper):
                plaintext += alphabet[Pi].upper()
                #make it false so every letter will not become uppercase
                upper = False
            else:
                #else, the letter was already lowercase
                plaintext += alphabet[Pi]

            #Increment variable
            n+=1
            
        else:
            plaintext += Ci
            disregard = False
            
        #Increment variable    
        i+=1

    return plaintext

#Encrypted
if(mode == "-e"):
    ciphertext = encrypt(text, key)
    print ciphertext
#Decreypted
elif(mode == "-d"):
    ciphertext = decrypt(text, key)
    print ciphertext
else:
    print "error: incorrect mode recieved!"
