
from ctypes import *
from ctypes.wintypes import *
import struct
import re
import sys

def getpid(process_name):
    import os
    return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]

OpenProcess = windll.kernel32.OpenProcess
ReadProcessMemory = windll.kernel32.ReadProcessMemory
CloseHandle = windll.kernel32.CloseHandle

PROCESS_ALL_ACCESS = 0x1F0FFF
pid = int(getpid("winmine.exe")[0])
address =0x1005360
address0 =0x1005330
buffer = c_char_p(b" "*10000)
val = c_int()
bufferSize = len(buffer.value)
bytesRead = c_ulong(0)
i=10
a=""
s=""
processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
if ReadProcessMemory(processHandle, address0, buffer, bufferSize, byref(bytesRead)):	


	s=str(buffer)
	while (i<11):
		a=a+hex(ord(s[i]))
		i=i+1
		if(a=="0x63"):
			lengh=2058
			n=0
		if(a=="0x28"):
			lengh=1874
			n=14
		if(a=="0x5c"):
			lengh=1078
			n=10
i=10
a=""
if ReadProcessMemory(processHandle, address, buffer, bufferSize, byref(bytesRead)):	
	s=str(buffer)
	while (i<lengh):
		a=a+hex(ord(s[i]))
		i=i+1
	
	a=re.sub("0x40","O",a)
	a=re.sub("0x42","O",a)
	a=re.sub("0x41","O",a)
	if (lengh==2058):
		a=re.sub("0x5c0x780x310x30","0",a)
	if(lengh==1078 or lengh==1874):
		a=re.sub("0x5c0x780x310x30","0",a)
		a=re.sub("0x5c0x780x300x66"*n,"\n",a)

	a=re.sub("0x5c0x780x300x66","O",a)
	a=re.sub("0x5c0x780x630x63","X",a)
	a=re.sub("0x5c0x780x380x61","X",a)
	a=re.sub("0x5c0x780x380x66","X",a)
	a=re.sub("00","*\n*",a)
	a=re.sub("\nO","",a)
	a=re.sub("0","*",a)
	print a
CloseHandle(processHandle)


# http://stackoverflow.com/questions/19684697/python-converting-byte-address-from-readprocessmemory-to-string

