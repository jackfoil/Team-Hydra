#!/bin/bash
# Coded by Brandon for team Hydra
# DO NOT LEAK

## CONFIG ##
# parameter maximum
MAXoffset=4096
MAXinterval=512

# modes
enabled_modes=( "b" "B" )

# output folder
output_folder="OUTPUT"
## /CONFIG ##


if [ -z $1 ]
then
	echo "usage: ./brute_steg_folder.sh directory/ [<interval start>] [<offset start>]"
	exit 1
fi

if [ -z $2 ]
then
	num=1
else
	num=$2
fi

if [ -z $3 ]
then
	tnum=1
else
	tnum=$3
fi

mkdir -p $output_folder

for k in $1*
do
	for mode_string in "${enabled_modes[@]}"
	do
		for (( interval=$tnum; interval<=MAXinterval; interval*=2 ));
		do
			for (( offset=$num; offset<=MAXoffset; offset*=2 ));
			do
                IFS='/' read -ra filename <<< "$k"
                filename=${filename[1]}
				mkdir -p "$output_folder"/"$filename"
				echo "File:$k $mode_string Offset:$offset Interval:$interval"
				python steg.py -$mode_string -r -o$offset -i$interval -w$k > ./$output_folder/"$filename"/"$mode_string"-"$offset"-"$interval" 2>/dev/null
			done
		done
	done
    find "$output_folder"/"$filename" -empty -type d,f -delete
done

