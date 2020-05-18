###################################################
# By: Cole Edwards
# Date: 5.5.2020
# Python 2.7.17
###################################################
from sys import stdin, stdout
from datetime import datetime, timedelta
import pytz
from hashlib import md5

DEBUG = False

ON_SERVER = False

INTERVAL = 60

#MANUAL_DATETIME = "2015 05 15 14 00 00"
MANUAL_DATETIME = datetime.now()

#get the epoch time
temp_epoch = stdin.read().rstrip("\n")

#set the time zones
EPOCH_T = pytz.timezone('US/Central')
Current_T = pytz.timezone('US/Central')

#set up the datetime
EPOCH = EPOCH_T.localize(datetime(int(temp_epoch[:4]),int(temp_epoch[5:7]),int(temp_epoch[8:10]),int(temp_epoch[11:13]),int(temp_epoch[14:16]),int(temp_epoch[17:19])))
Current_Time = Current_T.localize(datetime(int(MANUAL_DATETIME[:4]),int(MANUAL_DATETIME[5:7]),int(MANUAL_DATETIME[8:10]),int(MANUAL_DATETIME[11:13]),int(MANUAL_DATETIME[14:16]),int(MANUAL_DATETIME[17:19])))

#convert the time zone
EPOCH_UTC = EPOCH.astimezone(pytz.timezone('UTC'))
Current_UTC = Current_Time.astimezone(pytz.timezone('UTC'))

ET = EPOCH_UTC
CT = Current_UTC

if(DEBUG):
    print temp_epoch
    print "Current (UTC): " + str(CT)
    print "Epoch (UTC): " + str(ET)

#total elapsed time then convert it to seconds
dif = Current_UTC - EPOCH_UTC
Total_Seconds = int(dif.total_seconds())

if(DEBUG):
    print "Seconds: " + str(Total_Seconds)

CT_Sec = MANUAL_DATETIME[17:19]
ET_Sec = temp_epoch[17:19]

#find the interval
if(ET_Sec > CT_Sec):
    interval = abs((int(ET_Sec) - int(CT_Sec)) - 60)
else:
    interval = int(CT_Sec) - int(ET_Sec)

elapsed_time = (Total_Seconds - interval)

if(DEBUG):
    print "Seconds: " + str(elapsed_time)

#get the md5(md5(of the seconds elapsed))
#setup the first hash
m = md5()
m.update(str(elapsed_time))
first_hash = m.hexdigest()

#setup the second hash
n = md5()
n.update(first_hash)
second_hash = n.hexdigest()

if(DEBUG):
    print "MD5 #1: ", first_hash
    print "MD5 #2: ", second_hash


#get the letters and numbers
needed_letters = ["a","b","c","d","e","f"]
needed_num = ["1","2","3","4","5","6","7","8","9"]
i = 0
j = len(second_hash)

letters = ""
num = ""

#get the first 2 letters from left-to-right
while(i < len(second_hash)):
    if(second_hash[i:i+1] in needed_letters):
        letters += second_hash[i:i+1]
        if(len(letters) == 2):
            break
    i+=1

#get the first 2 numbers from right-to-left
while(j > 0):
    if(second_hash[j-1:j] in needed_num):
        num += second_hash[j-1:j]
        if(len(num) == 2):
            break
    j-=1

#output
stdout.write("Code: ")
stdout.write(letters)
stdout.write(num)
stdout.write("\n")
stdout.flush()
