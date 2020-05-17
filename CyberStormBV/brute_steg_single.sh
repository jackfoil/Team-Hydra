#!/bin/bash
# Coded by Brandon for team Hydra
# DO NOT LEAK
# usage
if [ -z $1 ]
then
	echo "usage: ./brute_steg_single.sh filename"
    exit 1
fi

# target file
filename=$1

# colors
GREEN='\033[1;32m'
NC='\033[0m'

# delete OUTPUT
rm -rf "OUTPUT"

# make directories for bruter
mkdir "OUTPUT"
mkdir "OUTPUT/brute-1byte"
mkdir "OUTPUT/brute-1bit"
mkdir "OUTPUT/brute-2byte"
mkdir "OUTPUT/brute-2bit"

echo -e "\n${GREEN}Starting Brute 1${NC}\n"

# change the number ranges to suite your challenge
# brute 1
for interval in 17 16 15 14 13 12 11 10 9
do
    interval=$((2**$interval))

    for offset in 4 5 6
    do
        offset=$((2**$offset))

        # echo for debug
        echo "O:$offset I:$interval"

        # execute python script with calculated arguments
        python steg.py -r -B -o$offset -i$interval -w$filename > "OUTPUT/brute-1byte/$offset-$interval"
        python steg.py -r -b -o$offset -i$interval -w$filename > "OUTPUT/brute-1bit/$offset-$interval"
    done
done

echo -e "\n${GREEN}Brute 1 Finished\nStarting Brute 2${NC}\n"
sleep 2

# delete empty folders
find "OUTPUT/brute-1byte" -empty -type d,f -delete
find "OUTPUT/brute-1bit" -empty -type d,f -delete

# brute 2
for interval in 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
do
    interval=$((2**$interval))

    for offset in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    do
        offset=$((2**$offset))

        # echo for debug
        echo "O:$offset I:$interval"

        # execute python script with calculated arguments
        python steg.py -r -B -o$offset -i$interval -w$filename > "OUTPUT/brute-2byte/$offset-$interval"
        python steg.py -r -b -o$offset -i$interval -w$filename > "OUTPUT/brute-2bit/$offset-$interval"
    done
done

echo -e "\n${GREEN}Brute 2 Finished${NC}\n"

# delete empty folders
find "OUTPUT/brute-2byte" -empty -type d,f -delete
find "OUTPUT/brute-2bit" -empty -type d,f -delete
