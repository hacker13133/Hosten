import os
import datetime
black = ("\033[1;30m")
Green = ("\033[1;32m")
red = ("\033[1;31m")
white = ("\033[1;37m")
yellow = ("\033[1;33m")
os.system("clear")

print(f"""
\033[1;37m
     .o oOOOOOOOo                                       OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                  .adOOOOOOO
    OboO00000000000.OOo. .oOOOOOo.    OOOo.oOOOOOo..OO0000000
    OOP.oOOOOOOOOOOO POOOOOOOOOOOo.   `OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOoOOOOOOOOOOO` .adOHOSTENOOoOOO'    OOOOo
    .OOOO'            `OOOOOOOO00000OOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOHOSTENOOOOOO.OOOOOOOOOOOOOO"`  '"OO.{Green}HOSTEN{white}.OOOO.OOOOOOOOOOOOOO
 {red}"OOOO"{white}       YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     {red}"OOO"{white}
   {red} Y{white}{white}           'OOO.{Green}HOSTEN{white}.OOO: .oOOo. :OOOOOOOOOOO?'         {red}:`{white}
   {red} :  {white}          .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         {red}.
   {red} .  {white}          oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"{red}OOo{white}
                 {red}'%o {white} OOOO"%OOOO%"%OOOOO"OOOOOO{red}"OOO':{white}
                     {red} `$"  `OO{white}OO' {red}`O"Y ' `{white}OO{red}OO'  {red}o             {red}.{white}
{red}    .                  .     OP"          : o     .
                            {red}  :{white}
                              {red}.{white}

	{Green}H""HHHHH""HH{white}                     dP
	{Green}H  HHHHH  HH{white}                     88
	{Green}H         `H{white} .d8888b. .d8888b. d8888P .d8888b. 88d888b.
	{Green}H  HHHHH  HH{white} 88'  `88 Y8ooooo.   88   88ooood8 88'  `88
	{Green}H  HHHHH  HH{white} 88.  .88       88   88   88.  ... 88    88
	{Green}H  HHHHH  HH{white} `88888P' `88888P'   dP   `88888P' dP    dP
	{Green}HHHHHHHHHHHH Telegram : https://t.me/HostenEgypt0{white}

{yellow}    1- Chack host open
    2- Unlock file Hosten
{white}
""")

time1 = datetime.datetime.now()
time = int(time1.strftime("%Y%m%d"))
if time > 20211130:
    print("masseg: Please Update The Tools!!")
    exit()

def Chack_Host():
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
    print(f"{yellow}masseg: The number of open hosts ({xc}) from ({xnc})!")
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
    	print(f"{yellow}masseg: Saved successfully!")
    	print(f"{yellow}masseg: Thank you for using the tool Hosten")
    elif saved in ["no","n","N"]:
    	print(f"{yellow}masseg: Thank you for using the tool Hosten")
    	exit()

def Unlock_file():

    def decode(text):
        key_trans = {

            '+Sa[B' : 'q',
            'J@%u~' : 'Q',
            'GwERG' : 'w',
            'Znt=#' : 'W',
            'n48,;' : 'e',
            'Q2)}]' : 'E',
            '?=kmr' : 'r',
            'Mf92/' : 'R',
            '$FAPb' : 't',
            'rxJ)^' : 'T',
            '.i.qO' : 'y',
            'T?H`8' : 'Y',
            'zh(UC' : 'u',
            '[rFO^' : 'U',
            '90N~k' : 'i',
            "$d&='" : 'I',
            '3i8)F' : 'o',
            '7>mNP' : 'O',
            'y=9)H' : 'p',
            '\\_LIe' : 'P',
            ':~E"V' : 'a',
            'cJjsN' : 'A',
            'kR\\~V' : 's',
            'i`Zk$' : 'S',
            'So16o' : 'd',
            'b4IWk' : 'D',
            ']=%{[' : 'f',
            '~X/9c' : 'F',
            'wjMDX' : 'g',
            '#;71L' : 'G',
            'P&$zO' : 'h',
            'b&D2J' : 'H',
            'Det6~' : 'j',
            '#!pgo' : 'J',
            '11C.E' : 'k',
            'j@|2m' : 'K',
            '>C*4)' : 'l',
            'U)wLl' : 'L',
            'e"sOd' : 'z',
            'g]6W(' : 'Z',
            'EpAc-' : 'x',
            '(la%k' : 'X',
            '88Bj>' : 'c',
            'a|Ms1' : 'C',
            '2,AK(' : 'v',
            '}Z|eJ' : 'V',
            '$VN?Q' : 'b',
            'E2Tmh' : 'B',
            'zy;XC' : 'n',
            '8Kw^1' : 'N',
            '{d2d)' : 'm',
            '26"/y' : 'M',
            'zYs5J' : '!',
            '+^0jI' : '@',
            '.RLI<' : '#',
            'Ih1,T' : '$',
            '|fa{-' : '%',
            'h/F@`' : '^',
            '9]:R,' : '&',
            '{#Wj"' : '*',
            'qg_K^' : '=',
            "X7'wR" : '~',
            'n(e8o' : '`',
            'f(p~z' : '<',
            'bFWxC' : '>',
            ':qI.m' : '(',
            '%F74v' : ')',
            'BNg7[' : '{',
            'G]}GC' : '}',
            'll&U`' : '[',
            'SH_V%' : ']',
            "x';Il" : ',',
            'Y*Ix7' : ';',
            '</l?l' : ':',
            'wbHA\\' : "'",
            '#8q{E' : '"',
            'r|#YG' : '\\',
            'gqP-b' : '|',
            'D{qo%' : '_',
            '0n#?p' : '-',
            '~|&[D' : '+',
            'U\\ZCP' : '.',
            '/D#R2' : '/',
            '3Nx`}' : '?',
            '0\\*a-' : '1',
            'sF=n,' : '2',
            '1F4|t' : '3',
            'UsDq*' : '4',
            'eHU$1' : '5',
            'B~B-8' : '6',
            'e{f$_' : '7',
            'Nk8pp' : '8',
            'E&#>%' : '9',
            '-pusN' : '0',
            "~3000" : " ",
            "~4500" : "    "
        }
        trans = ""
        z = 5
        x = 0
        for i in text:
            T = str(text[x:z])
            z += 5
            x += 5
            try:
                trans += (key_trans[T])
            except KeyError:
                pass
        return trans


    try:
        file_lock = input("Enter name file Hosten lock: ")
        file = open(file_lock,"r").read()
        Unlock = decode(file)
        file_open = open(f"{file_lock}","a").write(Unlock)
        print(f"{yellow}masseg: Saved successfully!")
        print(f"{yellow}masseg: Thank you for using the tool Hosten")
    except FileNotFoundError:
        print(f"{red}Error: Not Found File ({file_lock}). !!{white}")
        exit()


Enter = input(">>>>> ")
while Enter not in ["1","2"]:
    print(f"{red}Please enter a valid number!!{white}")
    Enter = input(">>>>> ")
if Enter == "1":
    Chack_Host()
elif Enter == "2":
    Unlock_file()



		
		
		
		
