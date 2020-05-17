# Made with Python 2.7.16
# Brandon Vessel
# CSC 442 / CYEN 301
# FTP (FTP.py)
# April 3, 2020

#import os
from ftplib import FTP
import datetime

# bit length. 7 or 10
METHOD=7

# filepath
FOLDER="/.secretstorage/.folder2/.howaboutonemore"

# host information
HOST="jeangourd.com"
PORT=8008

# login information
USERNAME="valkyrie"
PASSWORD="chooseroftheslain"

# create the timestamp
def create_timestamp():
    info = datetime.datetime.timetuple(datetime.datetime.today())[:]
    weekdays = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
    months = ("Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    year = info[0]
    month = months[info[1]]
    weekday = weekdays[info[6]]
    day = info[2]
    hour = info[3]
    minute = info[4]
    second = info[5]

    #return "Fri Jan 10 09:01:01 2020 time={:.1}ms TTL=1"
    return "{} {} {} {:2d}:{:2d}:{:2d} {}".format(weekday,month,day,hour,minute,second,year)


# fetch permissions from the current directory
def fetch_permissions(connection):
    # list of files
    files = []

    # append file list to files
    connection.dir(files.append)

    # return file list
    return files


# convert from seven bit permissions booleans to text
def seven_bit(ftp):
    # traverse to 7 bit directory
    ftp.cwd(FOLDER)

    # grab file permissions
    permissions = fetch_permissions(ftp)

    # close connection
    ftp.quit()

    #print(permissions)

    bit_permissions = []
    # iterate through permissions
    for i in range(len(permissions)):
        # get file data from list
        file_data = permissions[i]

        # seperate the permissions from everything else
        file_data = file_data.split(" ")[0]

        # check first 3 bits
        first_three = "".join(list(file_data)[0:3])
        
        # only proceed if the first three bits are 0
        if(first_three == "---"):
            # chop off the bits we don't need
            file_data = "".join(list(file_data)[3:10])
            #print(file_data)

            # set the permissions value as the new string
            bit_permissions.append(file_data)
            #print(file_data)

    # return modified permission
    return bit_permissions


# convert from ten bit permissions booleans to text
def ten_bit(ftp):
    # traverse to 10 bit directory
    ftp.cwd(FOLDER)

    # grab file permissions
    permissions = fetch_permissions(ftp)

    # close connection
    ftp.quit()

    # iterate through permissions
    for i in range(len(permissions)):
        # get file data from list
        file_data = permissions[i]

        # seperate the permissions from everything else
        file_data = file_data.split(" ")[0]

        # set the permissions value as the new string
        permissions[i] = file_data

    # return modified permissions
    return permissions


# the main decoding function
def decode():
    # initiate connection
    # create FTP object
    ftp = FTP()

    # connect to server
    ftp.connect(HOST, PORT)

    # login
    ftp.login(USERNAME, PASSWORD)


    # call specific bit function
    if(METHOD == 7):
        permissions = seven_bit(ftp)
    elif(METHOD == 10):
        permissions = ten_bit(ftp)

    # final binary string
    binary = []

    # convert from characters to binary
    for file_data in permissions:
        #print(file_data)
        file_data = str(file_data).replace("-","0").replace("w","1").replace("r","1").replace("x","1").replace("d", "1")
        #print(file_data)
        binary.append(file_data)
    
    # make binary into it's final form
    binary = "".join(binary)
    #print(binary)

    if(METHOD == 7):
        # only print 7 bit length
        print(binary_to_text(binary, 7))

    else:
        # since length is unknown, print 7 and 8 bit length ascii
        print("7 Bit:")
        print(binary_to_text(binary, 7))
        print("8 Bit:")
        print(binary_to_text(binary, 8))
    

# converts binary to text give a string and bit length
# from Binary.py
def binary_to_text(data, step):

    fstring = []

    data = list(data)

    while(len(data) != 0):
        character = []
        # try catch in case of improper step
        try:
            for i in range(step):
                # pop off only the characters we need
                character.append(data.pop(0))
        except:pass
        
        # make it a string
        character = "".join(character)

        # convert to ascii number base 10
        character = int(character, 2)
        #print("{} {}".format(character, chr(character)))

        # check for backspace
        if(int(character) == 8):
            # delete character before backspace
            NULL = fstring.pop()

        # check for tab
        elif(int(character) == 9):
            # tab
            fstring.append("\t")
        # check for carraige return
        elif((int(character) == 10) or (int(character) == 13)):
            # new line
            fstring.append("\n")
        else:
            # add character to string list as an ascii character instead of its number
            fstring.append(chr(character))
        
    # return binary string
    return "".join(fstring)


# MAIN
if(__name__ == "__main__"):
    import time
    try:
        print(create_timestamp())
        decode()
    except Exception as e:
        print(e)