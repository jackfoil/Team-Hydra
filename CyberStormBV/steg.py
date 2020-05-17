# Made with Python 2.7.18
# Brandon Vessel
# CSC 442 / CYEN 301
# Steg
# May 8, 2020

from sys import argv, stdout

## CONFIG ##
#   MAIN   #
ENDIAN = False

# DEFAULTS #
OFFSET = 0
INTERVAL = 1
STORE = False
RETRIEVE = False
HIDDEN = True

# SENTINEL #
SENTINEL_BYTES = [0x0,0xFF,0x0,0x0,0xFF,0x0]
SENTINEL_STRING = '000000001111111100000000000000001111111100000000'
SENTINEL_BINARY = ["00000000", "11111111", "00000000", "00000000", "11111111", "00000000"]
############


# usage string
usage='''python {} -(s/r) -(b/B) -o<val> [-i<val>] -w<val> [-h<val>]
-s      store
-r      retrieve
-b      bit mode
-B      byte mode
-o<val> set offset to <val> (default is 0)
-i<val> set interval to <val> (default is 1)
-w<val> set wrapper file to <val>
-h<val> set hidden file to <val>'''.format(argv[0])


## argument parse
# -s
for i in range(len(argv)):
    if(argv[i][0:2] == "-s"):
        STORE = True
        break
else:
    # -r
    for i in range(len(argv)):
        if(argv[i][0:2] == "-r"):
            RETRIEVE = True
            break

# -b
for i in range(len(argv)):
    if(argv[i][0:2] == "-b"):
        BYTEMODE = False
        break
else:
    # -B
    for i in range(len(argv)):
        if(argv[i][0:2] == "-B"):
            BYTEMODE = True
            break
    else:
        print("You must specify the bit/byte mode with either -b or -B")
        print(usage)
        exit()

# -o
for i in range(len(argv)):
    if(argv[i][0:2] == "-o"):
        OFFSET = int(argv[i][2:])
        break
else:
    print("You must specify the the offset with -o")
    print(usage)
    exit()

# -i
for i in range(len(argv)):
    if(argv[i][0:2] == "-i"):
        INTERVAL = int(argv[i][2:])
        break

# -w
for i in range(len(argv)):
    if(argv[i][0:2] == "-w"):
        WRAPPER = argv[i][2:]
        break
else:
    print("You must specify the wrapper file with -w")
    print(usage)
    exit()

# only check for hidden file if storing
if(STORE):
    # -h
    for i in range(len(argv)):
        if(argv[i][0:2] == "-h"):
            HID = argv[i][2:]
            break
    else:
        print("You must specify the hidden file with -h")
        print(usage)
        exit()


## functions
def store():    
    '''Store a file in another file'''
    # open wrapper and hidden file and read
    try:
        wrapper = bytearray(open(WRAPPER, "r").read())
    except Exception as e:
        raise Exception("Could not open wrapper file")
    try:
        hid = bytearray(open(HID, 'r').read())
    except Exception as e:
        raise Exception("Could not open hidden file")
        
    # set the offset to a dynamic variable
    off = OFFSET

    try:
        if(BYTEMODE):
            # byte mode
            # overwrite wrapper with hidden file
            for i in range(len(hid)):
                wrapper[off] = hid[i]
                off += INTERVAL

            # overwrite sentinel after hidden file
            for i in range(len(SENTINEL_BYTES)):
                wrapper[off] = SENTINEL_BYTES[i]
                off += INTERVAL
        else:
            # bit mode
            # overwrite wrapper with hidden file
            for i in range(len(hid)):
                for j in range(8):
                    wrapper[off] &= 11111110
                    wrapper[off] |= ((hid[i] & 10000000) >> 7)
                    hid[i] = (hid[i] << 1) & (2 ** 8 - 1)
                    off += INTERVAL
            
            # overwrite sentinel after hidden file
            for i in range(len(SENTINEL_BYTES)):
                for j in range(8):
                    wrapper[off] &= 11111110
                    wrapper[off] |= ((int(SENTINEL_BYTES[i]) & 10000000) >> 7)
                    SENTINEL_BINARY[i] = (SENTINEL_BYTES[i] << 1) & (2 ** 8 - 1)
                    off += INTERVAL
                i += 1
    except:
        raise Exception("Wrapper file not big enough or interval too big")

    temp = open(WRAPPER, "w")
    temp.seek(0)
    temp.truncate()
    temp.write(wrapper)
    temp.close()
        

def retrieve():
    '''Retrieve data hidden in a file'''
    # read the wrapper file as a bytearray
    try:
        wrapper = bytearray(open(WRAPPER, "r").read())
    except Exception as e:
        raise Exception("Could not open wrapper file")

    # create a new bytearray for the hidden data
    hid = bytearray()

    # set the offset to a dynamic variable
    off = OFFSET

    # check is the number of sentinel values we have seen in a row
    check = 0
    if (BYTEMODE):
        # byte mode
        while (off < len(wrapper)):
            b = wrapper[off]
            # check for sentinel byte
            if(b == SENTINEL_BYTES[check]):
                # increment sentinel counter
                check += 1
                hid.append(b)
            else:
                # reset sentinel counter
                hid.append(b)
                check = 0
            off += INTERVAL
            if(check == 6):
                break
        else:
            raise Exception("Sentinel not found in file")
        
        # chop off the sentinel values
        hid = hid[:-6]

    else:
        # bit mode
        while(off < len(wrapper)):
            b = 0
            for j in range(8):
                b |= (wrapper[off] & 00000001)
                if j < 7:
                    b = (b << 1) & (2 ** 8 - 1)
                    off += INTERVAL
            # check for sentinel byte
            if(b == SENTINEL_BYTES[check]):
                # increment sentinel counter
                check += 1
                hid.append(b)
            else:
                # reset sentinel counter
                hid.append(b)
                check = 0
            off += INTERVAL
            if(check == 6):
                break
        else:
            raise Exception("Sentinel not found in file")
        
        # chop off the sentinel values
        hid = hid[:-6]

    # print it out
    stdout.write(hid)
    stdout.flush()


## main
if(__name__ == "__main__"):
    try:
        if(STORE):
            store()
        elif(RETRIEVE):
            retrieve()
        else:
            print(usage)
    except Exception as e:
        if(not HIDDEN):
            stdout(e)