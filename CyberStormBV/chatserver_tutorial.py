import socket
from time import sleep
from binascii import hexlify

# set the port for client connections
port = 31337

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

delay_0 = 0.02
delay_1 = 1

# listen for clients
# this is a blocking call
s.listen(0)

# a client has connected!
c, addr = s.accept()

# set the message
msg = "Bud bud is a happy dog :)"
covert_message="password:budbud :)" + "EOF"

# turn covert message into bit message
covert_bin=[]

for i in covert_message:
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

msg = list(msg)

# send the message, one letter at a time
# while there is still bit_message to send
n=0
print(len(covert_bin))
done=False
while(not done):
    for i in msg:
        # Get bit to send
        bit =  covert_bin[n]

        c.send(i)
        if(int(bit)==0):
            delay=delay_0
        else:
            delay=delay_1
        sleep(delay)
        n = (n+1) % len(covert_bin)
        if(n==0):
            done=True
        

# send EOF and close the connection to the client
c.send("EOF")
c.close()
