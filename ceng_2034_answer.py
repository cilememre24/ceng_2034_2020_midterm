#!/usr/bin/python3

import os,sys,requests,threading
from sys import platform as _platform

print("PID: ",os.getpid())


if _platform == "linux":
	print(os.getloadavg())

load1, load5, load15 = os.getloadavg()

print("Load average over the last 5 minute:", load5)

nproc = os.cpu_count() 
 
print("Number of CPUs in the system:", nproc) 


if (nproc - load5 < 1):
	sys.exit()

urls=['https://api.github.com​', 'http://bilgisayar.mu.edu.tr/​', 'https://www.python.org/​ ', 'http://akrepnalan.com/ceng2034​', 'https://github.com/caesarsalad/wow​']

def check_url(url):
	x=requests.get(url)
	print(x.status_code)
	if(x.status_code>=200 and x.status_code <=300):
		print("The url:",url,"is valid.")
	elif(x.status_code>=404):
		print("The url:",url," is not valid.")


threads = [threading.Thread(target=check_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

