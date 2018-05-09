#coding: utf-8
#!/usr/bin/python3

from colorama import init, Fore, Back, Style
import os
import sys
import time
import platform
import win32file
import pywintypes

init(convert=True)

print(Fore.YELLOW + 'Enter the file path to get the original time stamps.' + Style.RESET_ALL)
file1 = input('Enter: ')
print()
stinfo = os.stat(file1)
print(Fore.GREEN + 'Access time of ' + Style.RESET_ALL + file1 + Fore.GREEN + ': %s ' %stinfo.st_atime + Style.RESET_ALL)
print(Fore.GREEN + 'Modified time of ' + Style.RESET_ALL + file1 + Fore.GREEN + ': %s ' %stinfo.st_mtime + Style.RESET_ALL)
print(Fore.GREEN + 'Creation time of ' + Style.RESET_ALL + file1 + Fore.GREEN + ': %s ' %stinfo.st_ctime + Style.RESET_ALL)
print (time.asctime(time.localtime(stinfo.st_atime)))

print()
print('Enter the the new file time with date time. e.g. 2011.01.08 18:00:50')
file1w1 = input('Enter the new access time in: ')
file1w2 = input('Enter the new modified time: ')
file1w3 = input('Enter the new creation time: ')
print()
nfile1 = int(time.mktime(time.strptime(file1w1, '%Y.%m.%d %H:%M:%S')))
nfile2 = int(time.mktime(time.strptime(file1w2, '%Y.%m.%d %H:%M:%S')))
nfile3 = int(time.mktime(time.strptime(file1w3, '%Y.%m.%d %H:%M:%S')))

# main logic function
def changeFileCreateTime(file1, ctime):
	handle = win32file.CreateFile(
		file1,
		win32file.GENERIC_WRITE,
		0,
		None,
		win32file.OPEN_EXISTING,
		0,
		0
	)
	PyTime = pywintypes.Time(nfile3)
	win32file.SetFileTime(
		handle,
		PyTime
	)
changeFileCreateTime(file1, 1234567789)

print(nfile1)
print(nfile2)
print(nfile3)

os.utime(file1, (nfile1, nfile2))

print(Fore.GREEN + 'Done.' + Style.RESET_ALL)