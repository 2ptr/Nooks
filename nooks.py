#!/bin/python

import os

startscreen = """
=====================================================
	 _ _            _                  _    
	| \ | ___  ___ | |__ ___      _ _ / |
	|   |/ . \/ . \| / /<_-<     | | || |
	|_\_|\___/\___/|_\_\/__/     |__/ |_|

                written by twopoint
                             
=====================================================
"""


def detectServices ():

    services = {
    3306: "MySQL",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    110: "POP3",
    143: "IMAP"
    }
    liveServices = []

    stdout = str(os.popen('netstat -aln | grep -e 0.0.0.0 -e 127.0 | cut -d : -f2 | cut -d " " -f 1').read())
    stdout = stdout.split("\n")
    
    for line in stdout:
        for port in services.keys():
            if str(port) == line and services[port] not in liveServices:
                liveServices.append(services[port])
    
    for port in liveServices:
        print("\t\t [+] " + port + " possibly detected!")
            

def sysline(cmd, tabs):
    stdout = str(os.popen("("+cmd+")" + " 2>&1").read())
    stdout = stdout.split("\n")
    for line in stdout:
        print("\t"*tabs + line)

def sysInfo():
    print("[*] System Info [*]\n")
    
    print("\t==> CPU Information")
    sysline("lscpu | head -n 4",1)
    
    print("\t==> Kernel and OS")
    sysline("uname -o && uname -v", 1)
    
    print("\t==> Listening Ports")
    sysline("netstat -aln | grep -e 0.0.0.0 -e 127.0 -e Address | cut -f 2", 1)
    detectServices()
    

print(startscreen)
sysInfo()