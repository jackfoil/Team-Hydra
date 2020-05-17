# Made with Python 3.7.3
# Brandon Vessel
# CSC 442 / CYEN 301
# TimeLock
# 2020 05 08

import pytz
from datetime import datetime
from hashlib import md5

## CONFIG ##
# debug mode
DEBUG = False

# challenge server flag
ON_SERVER = False

# valid time interval
INTERVAL = 60

# manual current datetime (UTC-5)
MANUAL_DATETIME = "2017 04 26 15 14 30"
############

# get epoch time from input
EPOCH_TIME = input().rstrip("\n")


def dprint(text):
    '''Prints debug messages'''
    if(DEBUG):
        print("[DEBUG] {}".format(text))


def UTC5_0(timetext):
    '''Converts Dr. Gourd-formatted timestamps to UTC Unix time'''
    ## time zone conversion
    # create datetime object from input time
    d = datetime.strptime(timetext, "%Y %m %d %H %M %S")

    # Set the time zone to 'America/Chicago'
    d = pytz.timezone('America/Chicago').localize(d)

    # Transform the time to UTC
    d = d.astimezone(pytz.utc)

    # debug print
    dprint("Date: {}\n\tTime: {}".format(d.strftime("%y-%m-%d %H:%M:%S"), int(d.timestamp())))

    return int(d.timestamp())


# LIVE CHALLENGE CODE
def getCurrentTime():
    '''Gets the current time as a Dr. Gourd timestamp for live testing'''
    info = datetime.timetuple(datetime.today())[:]
    year = info[0]
    month = info[1]
    day = info[2]
    hour = info[3]
    minute = info[4]
    second = info[5]
    return "{} {} {} {} {} {}".format(year, month, day, hour, minute, second)


def generateMD5Hash():
    global ON_SERVER
    global MANUAL_DATETIME
    global EPOCH_TIME
    global INTERVAL

    ## LIVE CODE CHECK
    # check to see if live
    if(ON_SERVER):
        # generate current time
        MANUAL_DATETIME = getCurrentTime()


    ## timezone convertion
    time1=UTC5_0(MANUAL_DATETIME)
    time2=UTC5_0(EPOCH_TIME)


    ## time difference
    difference = time1-time2
    clamped_difference = difference - (difference % INTERVAL)

    # print differences
    dprint("Difference: {}".format(difference))
    dprint("Difference: {}".format(clamped_difference))

    # hash
    str_hash = md5(md5(str(clamped_difference).encode("UTF-8")).hexdigest().encode("UTF-8")).hexdigest()

    # print hash
    dprint("MD5 Hash: {}".format(str_hash))


    ## build code
    # make hash a list
    str_hash = list(str_hash)

    # code list
    code=[]


    # letter 1
    i=0
    while(i<len(str_hash)):
        try:
            # try to make it an int
            temp=int(str_hash[i])
        except:
            # if not a number, it's a letter. append it
            code.append(str_hash[i])
            i+=1
            break
        i+=1
    else:
        # NO LETTERS (NOT IMPLEMENTED)
        dprint("[ERROR] No letters in hash")


    # letter 2
    while(i<len(str_hash)):
        try:
            # try to make it an int
            temp=int(str_hash[i])
        except:
            # if not a number, it's a letter. append it
            code.append(str_hash[i])
            i+=1
            break
        i+=1
    else:
        # NO LETTERS (NOT IMPLEMENTED)
        dprint("[ERROR] No letters in hash")


    # number 1
    i=len(str_hash)
    while(i>0):
        try:
            # try to make it an int and append it
            code.append(str(int(str_hash[i])))
            i-=1
            break
        except:
            # if not a number, it's a letter. ignore it
            pass
        i-=1
    else:
        # NO LETTERS (NOT IMPLEMENTED)
        dprint("[ERROR] No numbers in hash")


    # number 2
    while(i>0):
        try:
            # try to make it an int and append it
            code.append(str(int(str_hash[i])))
            i-=1
            break
        except:
            # if not a number, it's a letter. ignore it
            pass
        i-=1
    else:
        # NO LETTERS (NOT IMPLEMENTED)
        dprint("[ERROR] No numbers in hash")


    ## print final code
    return "".join(code)

# main
if(__name__ == "__main__"):
    print(generateMD5Hash())

    # live loop
    if(ON_SERVER):
        # print hashes forever
        while(1):
            print(generateMD5Hash())