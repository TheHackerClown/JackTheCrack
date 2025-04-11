#!/bin/python3
#Author: TheHackerClown
#LICENSE: WTFPL - wtfpl.net

from termcolor.termcolor import colored
from pyfiglet import figlet_format as writef
from os import system
from platform import system as whatos

__VERSION__ = "1.0.0"


def printf(data:str,font:str="banner3-D",color:str="red",width:int=200,justify:str="left")->None:
  print(colored(writef(data, font,justify=justify,width=width),color),end="")
def printc(data:str)->None:
   print(data.center(200))

def clear():
    if whatos() == "Windows":
       system("cls")
    else:
       system("clear")
       
def mainmenu():
    printc("Fullscreen has the best view")
    printc("Note: Submenu Feature Coming Soon...\n")
    printc("---Select Options---")
    printc("1. Create Program")
    printc("0. Exit")
    printc("--------------------\n")
    print("Enter Number 1 or 0 : ".rjust(105),end="")
    
def intro():
    clear()
    printf("Jack The Crack",justify="center")
    print("\n")
    printc(f"----Version-{__VERSION__}--Author: TheHackerClown------")
    print("\n")

def writefile(NAME_STRING:str,FONT_TYPE:str,FONT_COLOR:str,FONT_ALIGN:str, OPTN_NO:int, OPTN_LIST:list[str],AUTHOR:str,VERSION:str)->list[str]:
    payload = [
      "#!/bin/python3", 
      f"#Author: {AUTHOR}",
      "", 
      "#Imports for Clearing Terminal",
      "from os import system as sys",
      "from platform import system as whatos",
      "",
      "#Version String [Modify This]",
      f"__VERSION__ = '{VERSION}' ",
      f"__AUTHOR__ = '{AUTHOR}'"
      "", 
      "def clear():",
      '   if whatos() == "Windows":',
      '      sys("cls")',
      '   else:',
      '      sys("clear")',
      "",
    ]

    if FONT_ALIGN == "center":
      payload.extend([
        'def printc(data:str)->None:',
        '   print(data.center(200))',        
      ])
    else:
      payload.extend([
        'def printc(data:str)->None:',
        '   print(data)',
      ])
    if FONT_ALIGN == "center":
       payload.extend([
       f'LOGO_STRING = """{colored(writef(NAME_STRING,font=FONT_TYPE,width=200,justify="center"),color=FONT_COLOR)}"""',
        ])
    else :
       payload.extend([
       f'LOGO_STRING = """{colored(writef(NAME_STRING,font=FONT_TYPE,width=200,justify="left"),color=FONT_COLOR)}"""',
        ])

    payload.extend([
        "",
        "def intro():",
        "   clear()",
        '   print(LOGO_STRING)',
        '   print("\\n")',
        '   printc(f"----Version-{__VERSION__}--Author: {__AUTHOR__}------")',
        '   print("\\n")',
        "",
        'def mainmenu():',
        '   printc("---Select Options---")'])
    
    for i in range(1, OPTN_NO+1):
        payload.append(f'   printc("{i}. {OPTN_LIST[i-1]}")')
    
    payload.extend(['   printc("0. Exit")','   printc("--------------------\\n")'])

    if FONT_ALIGN == "center":
       payload.append(f'   print("Enter Number [{"/".join([str(x) for x in range(1, OPTN_NO+1)])}/0] : ".rjust(105),end="")')
    else:
       payload.append(f'   print("Enter Number [{"/".join([str(x) for x in range(1, OPTN_NO+1)])}/0] : ",end="")')

    for i in range(1, OPTN_NO+1):
        payload.extend([
            "",
            "#HEY, EDIT THIS FUNCTION",
            f"def {OPTN_LIST[i-1].replace(" ","_")}():",
            f"   #this function belongs to option {i}",
            "   print()"
            ])
    
    payload.extend([
       "",
       'while True:',
       '   intro()',
       '   mainmenu()',
       '   choice = int(input())',
       '   match choice:',
    ])
    for i in range(1, OPTN_NO+1):
        payload.extend([
          f'      case {i}:',
          f'         #HEY EDIT THIS FUNCTION',
          f'         {OPTN_LIST[i-1].replace(" ","_")}()'
        ])

    payload.extend([
        '      case 0:',
        '         clear()',
        '         #You can edit this message of exiting',
        '         printc("Bite my ass nigga")',
        '         break'
    ])

    return payload

while True:
    intro()
    mainmenu()
    choice = int(input())
    match choice:
       case 1:
          intro()
          print("Enter Name of Your Program : ".rjust(105),end="")
          prog_name = str(input())
          print("Enter Name of the Author : ".rjust(105),end="")
          author_name = str(input())
          print("Enter Version of Your Program : ".rjust(105),end="")
          prog_version = str(input())
          print("Enter what aligment of text you want [center/left] : ".rjust(105),end="")
          font_align = str(input())
          print("Enter type of font you want [check font_codenames.md file, then enter codename] : ".rjust(105),end="")
          font_type = str(input())
          print("Enter color of logo [any color] : ".rjust(105),end="")
          font_color = str(input())
          print("Enter Number of Options you want : ".rjust(105),end="")
          optn_nom = int(input())
          optn_list = []
          for i in range(1, optn_nom+1):
            print(f"Enter Name of Option {i} [dont worry about spaces] : ".rjust(105),end="")
            data = str(input())
            optn_list.append(data)
          with open(f"./output/{prog_name}.py","w") as fd:
                data = writefile(prog_name,font_type,font_color,font_align,optn_nom,optn_list,author_name,prog_version)
                for i in data:
                   fd.write(i + "\n")
          clear()
          intro()
          printc(f"Your File is successfully created, and saved in output folder, with name {prog_name}.py...")
          print("\n Wanna Restart ??? [y/n]: ".rjust(105),end="")
          rest = str(input())
          if rest.lower() == "n":
             break
       case 0:
          clear()
          printf("yohoho nigga", font="doh" ,width=400)
          break
    