'''
Name: David Milam
Assignment #6: XOR Crypto
Date: May 6, 2020
Language: Python 3
Description: Take in a plaintext and perform xor operation on it with the provided key (assuming key is in same folder labeled 'key')
			  and send output to stdout buffer. If a ciphertext is provided, the output will be decrypted back to plaintext.
Usage: 1) cat ciphertext1 | python3 06.py
	   2) python3 06.py < ciphertext
'''


from sys import stdin
import sys
from math import ceil, log



SENTINEL_LIST = [0, 255, 0, 0, 255, 0]
SENTINEL_BYTEARRAY = bytearray(SENTINEL_LIST)



def plot_bytearray_img(bytearray):
	from PIL import Image
	import io
	import matplotlib.pylab as plt

	img = Image.open(io.BytesIO(bytearray))
	plt.imshow(img)
	plt.show()

# take in wrapper (type: bytes)
def extract_byte_method(wrapper, offset, interval):
	hidden = [] # store hidden bytes into list
	wrapper = wrapper[int(offset):]
	for i in range(0, len(wrapper), interval):
		byte = wrapper[i]
		hidden.append(byte)
		if len(hidden) > len(SENTINEL_LIST):
			subset = hidden[-len(SENTINEL_LIST):]
			if subset == SENTINEL_LIST:
				return bytes(hidden[:-len(SENTINEL_LIST)])

	print('Sentinel message not found with given offset and interval:', offset, interval)
	return -1

def extract_bit_method(wrapper, offset, interval):
	hidden = [] # store hidden bytes into list

	wrapper = bytes(wrapper[int(offset):])

	i = 0
	while i < len(wrapper):
		b = 0
		try:
			for j in range(8):
				b |= ( wrapper[i] & 0b00000001)
				if j < 7:
					b = (b << 1) & (2 ** 8 - 1)
				i += interval

			hidden.append(b)

			if len(hidden) > len(SENTINEL_LIST):
				subset = hidden[-len(SENTINEL_LIST):]
				if subset == SENTINEL_LIST:
					return bytes(hidden[:-len(SENTINEL_LIST)])
		except:
			return -1
	print('Sentinel message not found with given offset and interval:', offset, interval)
	return -1

with open('life_brac_bit_method(Encr.sg1)', mode='rb') as f:
	wrapper = f.read()
# with open('life_brac_steg.jpeg', mode='rb') as f:
# 	wrapper = f.read()
# print(wrapper)
# print(len(wrapper), type(wrapper))
# exit(1)

# for i in [1, 2, 4, 8, 16, 32]:
# 	for j in [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]:
i = 1636
j = 32
print('offset and interval:', j, i)
# hidden = extract_bit_method(wrapper, offset=j, interval=i) #bytes(hidden)
hidden = extract_byte_method(wrapper, offset=j, interval=i)  # bytes(hidden)
# plot_bytearray_img((hidden))
# if hidden != -1: break
# if hidden != -1: break
# hidden = extract_bit_method(wrapper, 1024, 1) #bytes(hidden)
# hidden = extract_byte_method(wrapper, 1024, 8) #bytes(hidden)
# print('hidden:', len(hidden), type(hidden))

if hidden == -1:
	print("oof :(")
	exit(1)

# with open('marb.bmp', mode='rb') as f:
# 	wrapper = (f.read())
# with open('hidden_byte', mode='rb') as f:
# 	msg_to_hide = f.read()
#with open('byte_method_on_constitution', mode='wb') as f:
#	f.write(hidden)
#
# hidden = store_message_byte(bytes(wrapper), bytes(msg_to_hide), 4096, 4)
# # hidden = extract_byte_method(wrapper, 1024, 8) #bytes(hidden)
# print('hidden:', len(hidden), type(hidden))

#plot_bytearray_img(( hidden)) # hidden  wrapper
