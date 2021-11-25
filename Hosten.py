import os
import datetime
black = ("\033[1;30m")
Green = ("\033[1;32m")
red = ("\033[1;31m")
white = ("\033[1;37m")
os.system("clear")
print("""
\033[1;37m
     .o oOOOOOOOo                                       OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                  .adOOOOOOO
    OboO00000000000.OOo. .oOOOOOo.    OOOo.oOOOOOo..OO0000000
    OOP.oOOOOOOOOOOO POOOOOOOOOOOo.   `OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOoOOOOOOOOOOO` .adOOOOOOOOOoOOO'    OOOOo
    .OOOO'            `OOOOOOOO00000OOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OO.HOSTEN.OOOO.OOOOOOOOOOOOOO
 "OOOO"       YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOO.HOSTEN.OOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                              .

	H""HHHHH""HH                     dP
	H  HHHHH  HH                     88
	H         `H .d8888b. .d8888b. d8888P .d8888b. 88d888b.
	H  HHHHH  HH 88'  `88 Y8ooooo.   88   88ooood8 88'  `88
	H  HHHHH  HH 88.  .88       88   88   88.  ... 88    88
	H  HHHHH  HH `88888P' `88888P'   dP   `88888P' dP    dP
	HHHHHHHHHHHH Telegram : https://t.me/HostenEgypt0

""")
time1 = datetime.datetime.now()
time = int(time1.strftime("%Y%m%d"))
if time > 20211110:
    print("أنتهت الفترة التجريبية تأكد من وجود تحديثات جديدة  في قناة التلجرام")
    exit()
try:
    Enter_file = input("Enter Name File: ")
    files = Enter_file.endswith(".txt")
    if files == True:
        list_file = open(f"{Enter_file}","r").read().splitlines()
    elif files == False:
        list_file = open(f"{Enter_file}.txt","r").read().splitlines()
except FileNotFoundError:
    print(f"{red}Error: Not Found File ({Enter_file}). !!{white}")
    exit()
space = " "
xc = 0
xnc = 0
lista, lista2= [], []
for i in list_file:
    comm = os.popen(f"ping -c 2 {i}").read()
    _i_ = int(len(i))
    cl = 40 - _i_
    if "icmp_seq=2" in comm:
        lista.append(i)
        xnc += 1
        xc += 1
        print(f"{Green}>>> [{i}]{space*cl}OPEN(✓){black}")
    else:
        xnc += 1
        print(f"{red}>>> [{i}]{space*cl}Lock(×){black}")
print(f"\033[1;33mmasseg: The number of open hosts ({xc}) from ({xnc})!")
#Save file and chack host in file
saved = input(f"{white}do you save hosts open? Y/N: ")
while saved not in ["Y","y","yes","N","n","no"]:
    print(f"{red}Error: please trai agine!!")
    saved = input(f"{white}do you save hosts open? Y/N: ")
try:
	file_check = open("Host_open.txt","+r").read().splitlines()
except:
	os.system("touch Host_open.txt")
	file_check = open("Host_open.txt","+r").read().splitlines()
for append in file_check:
	lista2.append(append)
	
if saved in ["yes","y","Y"]:
	for i in lista:
		if i in lista2:
			pass
		elif i not in lista2:
			file_saved = open("Host_open.txt","a").write(f"{i}\n")
	print(f"\033[1;33mmasseg: Saved successfully!")
	print(f"\033[1;33mmasseg: Thank you for using the tool Hosten")
elif saved in ["no","n","N"]:
	print(f"\033[1;33mmasseg: Thank you for using the tool Hosten")
	exit()

		
		
		
		
