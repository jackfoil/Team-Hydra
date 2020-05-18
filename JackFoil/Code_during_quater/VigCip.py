#Name: Jack Foil
#Date: 3/25/ 2020
#Topic: Vigenere Cipher

from sys import stdin, argv
import re

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ".#'


#encrpts the letters by moving them fowards
def encrypt(textshift, text_ex, text_ex_in, text_cap, keyshift):
    cipherkey = ""
    i = 0
    j= 0

    #shifts the text when using the key
    while i < len(textshift):
        if(j == len(keyshift)):
            j = 0
        textshift[i] += keyshift[j]
        
        j +=1
        i +=1


    #Finding the letters
    k = 0
    cipherkey_arr = []
    while k < len(textshift):
        if(textshift[k] > 25):
            textshift[k] -= 26
        cipherkey_arr.append(alpha[textshift[k]])
        k += 1



    # insert the extras like (' ', ! $%^&*()_) into the array
    a = 0
    while a < len(text_ex):
        cipherkey_arr.insert(text_ex_in[a], text_ex[a])
        a += 1
        
    
    #orginal character back to lower case
    b = 0
    while b < len(text_cap):
        if(text_cap[b] == 1):
            cipherkey_arr[b] = cipherkey_arr[b].lower()
        b +=1

    # turn it into a string
    cipherkey = ''.join(str(c) for c in cipherkey_arr)
    
    return cipherkey


#decryps the code by shifting the letters backwards
def decrypt(textshift, text_ex, text_ex_in, text_cap, keyshift):
    plaintext = ""
    i = 0
    j= 0

    #shifts the text when using the key
    while i < len(textshift):
        if(j == len(keyshift)):
            j = 0
        textshift[i] -= keyshift[j]
        
        j +=1
        i +=1


    #Finding the letters
    k = 0
    plain_arr = []
    while k < len(textshift):
        if(textshift[k] < -25):
            textshift[k] += 26
        plain_arr.append(alpha[textshift[k]])
        k += 1



    # insert the extras like (' ', ! $%^&*()_) into the array
    a = 0
    while a < len(text_ex):
        plain_arr.insert(text_ex_in[a], text_ex[a])
        a += 1
        
    
    #orginal character back to lower case
    b = 0
    while b < len(text_cap):
        if(text_cap[b] == 1):
            plain_arr[b] = plain_arr[b].lower()
        b +=1

    # turn it into a string
    plaintext = ''.join(str(c) for c in plain_arr)


    return plaintext


def getshifts(thekey):
    #checks lower characters with 1s and 0s 1= lower 0 = upper
    #stores them into an array
    capital =[]
    i = 0
    while i < len(thekey):
        if(thekey[i].islower()):
            capital.append(1)
        else:
            capital.append(0)
        i+=1


    #captilize eveything
    thekey = thekey.upper()

    #marks the non characters and index this is gonna be used towards the end of the
    #process
    a = 0
    b = 0
    index_extra = []
    extra = []
    while a < len(thekey):
        while b < len(alpha):

            #if it equals to each other then breaks loop
            if(thekey[a] == alpha[b]):
                b = 100

            #if it is at the end and does not equal
            #then add to extra arrays
            elif(b == 25 and thekey[a] != alpha[b]):
                extra.append(thekey[a])
                index_extra.append(a)
                b+=1

            # moves the checking the array along
            elif(thekey[a] != alpha[b]):
                b+=1     
        b = 0
        a += 1    


    #gets rid of everything but characters in the strings
    thekey = "".join(re.split("[^a-zA-Z]*", thekey))

    #Translates the text into numbers
    nums = []
    j = 0
    k = 0
    while j < len(thekey):
        while k < len(alpha):
            if(thekey[j] == alpha[k]):
               nums.append(k)               
            k+=1
        j+=1
        k =0

    return (nums, extra, index_extra, capital)
        

    




# gets the mode, key, user input
mode = argv[1]
key = argv[2]
text = raw_input().rstrip("\n")

# this will get the key and text (sent by the user) thier numbers, special characters and indexes, which
# letters are lower case
shift = getshifts(key)
text_nums = getshifts(text)




if(mode == "-e"):    
    # give text to function
    ciphertext = encrypt(text_nums[0], text_nums[1], text_nums[2], text_nums[3], shift[0])
    #print final result
    print ciphertext




if(mode == "-d"):
    # give text to function
    encrypt = decrypt(text_nums[0], text_nums[1], text_nums[2], text_nums[3], shift[0])
    
    #print final result
    print encrypt
    
