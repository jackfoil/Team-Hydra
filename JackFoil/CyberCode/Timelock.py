### Name: Jack Foil
### Date: 4/29/2020
###Program: Timelock / Use Python 2.7
########################################################
from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5

#Debug mode
DEBUG = True

#set to true if on the challenge server
ON_SERVER = False

#time interval
INTERVAL = 60

#manual date time 
MANUAL_DATETIME ="2017 04 26 15 14 30"

# takes the epoch time and gets rid of quotes in the epoch (will cause erros if not)
epoch = raw_input()
if (epoch[0] == '"'):
    epoch = epoch[1:len(epoch)-2]


#gets the UTC time
def getdatetime(a):       
    x = a.split()
    local_TZ = pytz.timezone("America/Chicago")
    dt = datetime(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]))
    dt = local_TZ.localize(dt, is_dst=None)
    dt = dt.astimezone(pytz.utc)    
    return dt


#adjust the seconds depending on the interval
def findinterval(interval, var):
    split = var.split() 
    sec = int(split[5])
    half = (interval / 2)
    diff = 0
    while(sec != interval and sec != 0):
        # how to determine to go up or down
        if(half < sec):
            sec += 1
            diff += 1
        else:
            sec -= 1
            diff += 1
    return diff

# find the code in the md5 
def findcode(hidden):
    reverse = hidden[::-1]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    let = ""
    nums = ""
    code = ""
    
    # find first two letters left to right
    a = 0
    b = 0
    while a < len(hidden):
        while b < len(alpha):
            if(alpha[b] == hidden[a]):
                let += str(hidden[a])
            b +=1

        if(len(let) == 2):
            break
        
        a +=1
        b = 0
                
    # find single digits right to left
    c = 0
    d = 0
    while c < len(reverse):
        while d < len(num):
            if(num[d] == reverse[c]):
                nums += str(reverse[c])
            d +=1
            
        if(len(nums) == 2):
            break
        
        c +=1
        d = 0
        
    code += let
    code += nums
    return code
    

        
        

###Main part of the code
##finds the UTC time
dt = getdatetime(MANUAL_DATETIME)
et = getdatetime(epoch)

#Finds the seconds and difference in those seconds depedning on interval
deltim = dt - et
dt_diff = findinterval(INTERVAL, MANUAL_DATETIME)
et_diff = findinterval(INTERVAL, epoch)
difference = ((int(deltim.total_seconds())) - (dt_diff + et_diff))

#md5 twice 
md_one = md5(str(difference).encode())
md_two = md5(str(md_one.hexdigest()))

#the code
code = findcode(md_two.hexdigest())


# Debug mode (prints out everything)
if(DEBUG):
    print "Current (UTC): " + str(dt)
    print "Epoch (UTC): " +str(et)
    print "Seconds: " + str(int(deltim.total_seconds()))
    print "Seconds: " + str(difference) # based on interval
    print "MD5 #1: " + str(md_one.hexdigest())
    print "MD5 #2: " + str(md_two.hexdigest())

#prints the code
print "Code: " + str(code)

