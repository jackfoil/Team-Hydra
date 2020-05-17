################################################################################
# Ayman Dokwal
# Timelock Program
# Using Python 2.7
################################################################################

# import statements
import time
import datetime
import sys
import md5

# debugging
DEBUG = False

# deciding to use either the current system time or a custom system time for testing
customTime = False
val_customTime = "2017 04 26 15 14 30"

# making the code valid for 60 seconds
interval = 60




# converting a time string into UTC
def to_UTC(timeString):
        # converting string into time struct, then convert the struct to UTC time since epoch to return
        timeStruct = time.strptime(timeString, "%Y %m %d %H %M %S")
        return int(time.mktime(timeStruct))


# retrieving hex value
def get_Hex():

	# retrieving time from stdin and converting it to UTC
	epochTime = to_UTC(sys.stdin.read().strip('\n'))

	# determining whether to use custom time or real system time
	if (customTime):
		systemTime = to_UTC(val_customTime)

	else:
		# else, getting the real system time
		dateTime = datetime.datetime.now()
		systemTime = to_UTC("{} {} {} {} {} {}".format(dateTime.year, dateTime.month, \
                                dateTime.day, dateTime.hour, dateTime.minute, dateTime.second))

    # computing unadjusted time elapsed
	elapsed_time = systemTime - epochTime
	# adjusting time elapsed based on how long the code is valid for
	elapsed_timeAdjustment = elapsed_time % interval

	# getting the true time elapsed converted to hex with md5
	true_elapsed_time = str(elapsed_time - elapsed_timeAdjustment)
	return (md5.new(md5.new(true_elapsed_time).hexdigest()).hexdigest())


# using a hex string to retrieve the secret code
def get_Code(hex_string):
        # showing full hex_string
        if(DEBUG):
                print(hex_string)

        # setting up strings for holding the letters and numbers found in the hex
        alpha = ""
        nums = ""

        # retrieving the first 4 letters from left to right
        for i in hex_string:

                # appending the letter found to the end of the alpha string
                if (i.isalpha()):
                        alpha += i

                        # once the four letters are found, no longer need this anymore
                        if(len(alpha) >= 4):
                                break

        # retrieving the first 4 numbers from right to left
        for i in range(len(hex_string)-1, -1, -1):

                # appending the number found to the end of the nums string
                if (not hex_string[i].isalpha()):
                        nums += hex_string[i]

                        # once four numbers are found, no longer need this anymore
                        if(len(nums) >= 4):
                                break

        # retrieving the four digit code, handling special cases
        if(len(alpha) >= 2 and len(nums) >= 2):
                # no special case is needed
                code = alpha[:2] + nums[:2]

        elif(len(alpha) < 2):
                # combining all of the letters and numbers in the string, removing an extra number from the end if there is one (index 5 if len(alpha) == 1)
                code = alpha + nums
                code[:4]

        else:
                # not enough numbers, so either use three letters if there is one number, or all letter if no numbers
                if(len(nums) == 1):
                        code = alpha[:3] + nums
                else:
                        code = alpha

        # sending resulting 4-digit code to stdout
        print code


get_Code(get_Hex())
