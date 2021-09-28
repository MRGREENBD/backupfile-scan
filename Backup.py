#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 01:23:08 2021

@author: mehedi
"""
import os ,sys
from multiprocessing import Pool
from multiprocessing.dummy import Pool as Speed
from requests import get as GET

if os.name == "posix":
	os.system("clear")
	try:
		os.mkdir("./File")
	except:
		pass
else:
	os.system("cls")


print( """
    <<<     CODE BY MR.GREEN     >>>
  __  __ ___        ___ ___ ___ ___ _  _ 
 |  \/  | _ \      / __| _ \ __| __| \| |
 | |\/| |   /  _  | (_ |   / _|| _|| .` |
 |_|  |_|_|_\ (_)  \___|_|_\___|___|_|\_|
                                         
	AUTO BACKUP FILE FINDER
	EX : python3 script.py list-Domain
""")



HOW = []

SITENAME =[]
FINELURL = []
FULLURL = []

def URLMIX(URL):
	try:
		SITENAME.append(URL.split("//")[1].split("/")[0])
	except:
		pass
	try:
		SITENAME.append(URL.split("//")[1].split("/")[0].split(".")[0])
	except:
		pass
	try:
		SITENAME.append(URL.split("//")[1].split("/")[0].split(".")[1])
	except:
		pass
	try:
		SITENAME.append(URL.split("//")[1].split("/")[0].split(".")[2])
	except:
		pass
	try:
		SITENAME.append(URL.split("//")[1].split("/")[0].split(".")[1]+"."+URL.split("//")[1].split("/")[0].split(".")[2])
	except:
		pass
	try:
		SITENAME.append(URL.split("//")[1].split("/")[0].split(".")[1]+"."+URL.split("//")[1].split("/")[0].split(".")[2]+"."+URL.split("//")[1].split("/")[0].split(".")[3])
	except:
		pass

	ExT = [".zip",".7z",".rar",".tar.gz",".sql",".bak",".backup"]
	PatH = ["backup","bk","new","old","install","data","api","update","demo","download","archived","lastbackup"]

	for file in PatH:
		for fileName in ExT:
			FINELURL.append(file+fileName)
	for SiteFile in SITENAME:
		for fileName in ExT:
			FINELURL.append(SiteFile+fileName)
	for SiteFile in SITENAME:
		for fileName in ExT:
			for path in PatH:
				FINELURL.append(SiteFile+"/"+path+fileName)




def CHACK(URL):
	URL = URL.strip()
	Headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'}
	Go = GET(URL , headers=Headers,timeout=20,stream=True)
	Length =  int(Go.headers.get('Content-Length', 0))
	if Length > 1048576:
		print(URL +" : "+str(Go.status_code))
		open("./File/FoundBackup.txt","a").write(Go.url+"\n")
	print(URL +" ## "+str(Go.status_code))

def SAND(URL):
	URLMIX(URL)
	for Mix in FINELURL:
		FULLURL.append(URL+Mix)
		#print(URL+Mix)
	pool =Speed(30)
	pool.map(CHACK,FULLURL)
	pool.close()


try:
	Links = sys.argv[1]
	Links = open(Links,"r").readlines()
	for URL in Links:
		URL=URL.strip()
		if not URL.endswith('/'):
			URL = URL+"/"
		if not URL.startswith('http'):
			URL = "https://"+URL
		try:
			SAND(URL)
		except:
			pass
		FINELURL.clear()
		FULLURL.clear()
		SITENAME.clear()
except:
	print("File Not Found")
