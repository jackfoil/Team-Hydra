from ftplib import FTP

IP = "localhost"
PORT = 21
FOLDER = "7"

contents = []

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login()
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

for row in contents:
    print(row)
