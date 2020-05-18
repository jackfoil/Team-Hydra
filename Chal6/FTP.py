from ftplib import FTP

IP = "138.47.102.67"
PORT = 21
FOLDER = ""

contents = []

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login('garlicpowder', 'redwopcilrag')
print "in"
#ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

for row in contents:
    print(row)
