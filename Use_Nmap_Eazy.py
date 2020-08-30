print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+                                                          +")
print("+           [!] powered by  Yazeed Bilal (zerox4) [!]      +")
print("+                                                          +")
print("+           My Email: Bilalyazeed4@gmail.com               +")
print("+                                                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

import os

ip = input("Enter Url or IP: ")
nmap = os.system("nmap -T4 -A -v {}".format(ip))
