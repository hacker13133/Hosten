import os
import datetime
import subprocess
os.system("clear")

# Colors ----------->>
Black = ("\033[1;30m")
Green = ("\033[1;32m")
Red = ("\033[1;31m")
White = ("\033[1;37m")
Yellow = ("\033[1;33m")
Blue = ("\033[1;36m")

# Ping connected hosts -------->>
def ping(host):
	error_host = host.startswith("ww.")
	if host[0] == "*" or error_host == True:
		host = False
	else:
		ping_command = subprocess.getstatusoutput(f"ping -c 2 {host}")
		chack_connected = ping_command[1].find("icmp_seq=2")
		if int(chack_connected) > 0:
			host = True
		elif "Name or service not known" in ping_command[1]:
			host = False
		else:
			host = False
	return host

# Minue and Logo -------------->>
def minu():
    print(f"""{Blue}
      1- Chack hosts list
      2- Check one host only
    {White}
    """)
def Logo():
	print(f"""{White}

     .o oOOOOOOOo                                       OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                  .adOOOOOOO
    OboO00000000000.OOo. .oOOOOOo.    OOOo.oOOOOOo..OO0000000
    OOP.oOOOOOOOOOOO POOOOOOOOOOOo.   `OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOoOOOOOOOOOOO` .adOOOOOOOOOoOOO'    OOOOo
    .OOOO'            `OOOOOOOO00000OOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOO.HOSTEN.OOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                              .

      {Blue}H""HHHHH""HH{White}                     dP
      {Blue}H  HHHHH  HH{White}                     88
      {Blue}H         `H{White} .d8888b. .d8888b. d8888P .d8888b. 88d888b.
      {Blue}H  HHHHH  HH{White} 88'  `88 Y8ooooo.   88   88ooood8 88'  `88
      {Blue}H  HHHHH  HH{White} 88.  .88       88   88   88.  ... 88    88
      {Blue}H  HHHHH  HH{White} `88888P' `88888P'   dP   `88888P' dP    dP {Blue}1.6v{White}
      {Blue}HHHHHHHHHHHH{White}{Blue} Telegram : https://t.me/HostenEgypt0{White}
		""")

# Stoped Time --------->>
time1 = datetime.datetime.now()
time = int(time1.strftime("%Y%m%d"))
#if time > 20211130:
#    print("masseg: Please Update The Tools!!")
#    exit()

# number 1 in Minue (Chack host list file) ------------>>
def Chack_host_list():
	# Enter file and chack list file and found file (*.txt) -------->>
	while True:
		try:
			name_file = input("Enter Name File: ")
			files = name_file.endswith(".txt")
			if files == True:
				list_file = open(f"{name_file}","r").read().splitlines()
			elif files == False:
				list_file = open(f"{name_file}.txt","r").read().splitlines()
			break
		except FileNotFoundError:
			print(f"{Red}Error: Not Found File ({name_file}). !!{White}")
			print(f"{Yellow}-----------------------------")
			os.system("ls *.txt")
			print(f"-----------------------------{White}")
		except KeyboardInterrupt:
			exit()
	# chack connected host open or no --------->>

	space = " "
	number_hosts_file = len(list_file)
	all_open_host = 0
	all_number_host = 0
	lista, lista2= [], []

	for i in list_file:
		hosts_ping = ping(host=i)
		number_len_host = int(len(i))
		space_host = 40 - number_len_host

		if hosts_ping == True:
			lista.append(i)
			all_number_host += 1
			all_open_host += 1
			print(f"{Green}>>> [{i}]{space*space_host}OPEN(✓) [{all_number_host}/{number_hosts_file}]{Black}")
		elif hosts_ping == False:
			all_number_host += 1
			print(f"{Red}>>> [{i}]{space*space_host}Lock(×) [{all_number_host}/{number_hosts_file}]{Black}")

	print(f"{Yellow}masseg: The number of open hosts ({all_open_host}) from ({all_number_host})!")
	#Save file and chack host in file ---------->>

	while True:
		saved = input(f"{White}do you save hosts open? Y/N: ")
		if saved not in ["Y","y","yes","N","n","no"]:
			print(f"{Red}Error: please trai agine!!")
		else:
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
					print(f"{Yellow}masseg: Saved successfully!")
					print(f"{Yellow}masseg: Thank you for using the tool Hosten")
					exit()
			elif saved in ["no","n","N"]:
				print(f"{Yellow}masseg: Thank you for using the tool Hosten")
				exit()

Logo()
minu()
try:
	Enter = input(">>>>> ")
except KeyboardInterrupt:
	exit()
while Enter not in["1","2"]:
	print(f"{red}Please enter a valid number!!{white}")
	try:
		Enter = input(">>>>> ")
	except KeyboardInterrupt:
		exit()
if Enter == "1":
	Chack_host_list()
elif Enter == "2":
	one_host()
