#!/usr/bin/python
#Please note: this script is unstable in Windows, feel free to do some changes:P
'''                _    
                  | |   
  _ __   ___  _ __| | __
 | '_ \ / _ \| '__| |/ /
 | | | | (_) | |  |   < 
 |_| |_|\___/|_|  |_|\_\

'''                    
import urllib2
import os

def main():
	asciiDraw()
	menu()
	pass

class color:
	BLUEBLOOD = '\033[1;34m'
	BOLD = '\033[1m'
	END = '\033[0m'
	GREEN = '\033[92m'
	RED = '\033[91m'
	YELLOW = '\033[93m'
	WHITE = '\033[1;37m'
	pass

def menu():
  color()
  ans=True
  
  while ans:  
	welcome = """
Welcome to Athena by Athena API, what would you like to do?

1. Google That - An simple API that let you google something!
2. UP or DOWN - Checks if an website is UP/DOWN using HTTP Headers!
3. Password Generator - Generates a random password whit the selected length
4. Minecraft Checker - Enter username and known if the accounts is premium
5. Email Validator - Checks for a valid email format
"""

	print color.BOLD + welcome + color.END
	choice=raw_input('\nChoose your option: ')
	
	if choice=="1":
	 clearConsole()
	 googleThat()
	 
	elif choice=="2":
	 clearConsole()
	 uporDown()
	 
	elif choice=="3":
	 clearConsole()
	 passwordGenerator()
	 
	elif choice=="4":
	 clearConsole()
	 minecraftChecker()
	 
	elif choice=="5":
	 clearConsole()
	 emailValidator()
	 
	elif choice=="6":
	 clearConsole()
	 emailValidator()
	 
	elif choice !="":
	 print("\n Not valid choice, please try again!") 
	pass

def asciiDraw():
	color()
	athena = """        
        _   _                     
       | | | |                     
   __ _| |_| |__   ___ _ __   __ _ 
  / _` | __| '_ \ / _ \ '_ \ / _` |
 | (_| | |_| | | |  __/ | | | (_| |
  \__,_|\__|_| |_|\___|_| |_|\__,_| 
                                """
	print color.BOLD + color.BLUEBLOOD + athena + color.END 
	pass
	
def googleThat():
	color()
	print('Type the url')
	print color.BOLD + color.BLUEBLOOD + 'G' + color.RED + 'O' + color.YELLOW + 'O' + color.GREEN + 'L' + color.RED + 'E' + color.WHITE + ' THAT' + color.END
	googleThat = raw_input('> ')
	url = 'http://api.predator.wtf/google/?arguments=site:' + googleThat
	loading()
	webFile = urllib2.urlopen(url).read()
	print color.BOLD + color.GREEN + '\n' + webFile + color.END	
	return main()
	
def uporDown():
	color()
	print color.BOLD + 'Site URL' + color.END
	upDownSite = raw_input('> ')
	url = 'http://api.predator.wtf/upordown/?arguments=' + upDownSite
	loading()
	webFile = urllib2.urlopen(url).read()
	print color.BOLD + color.GREEN + '\n' + webFile + color.END	
	return main()
	pass

def passwordGenerator():
	color()
	print color.BOLD + 'Choose pass lenght: (min: 13)' + color.END
	password = raw_input('> ')
	url = 'http://api.predator.wtf/passgen/?arguments=' + password
	loading()
	webFile = urllib2.urlopen(url).read()
	print color.BOLD + color.GREEN + '\n' + webFile + color.END	
	pass
	
def minecraftChecker():
	color()
	print color.BOLD + 'Type the account username:' + color.END
	username = raw_input('> ')
	url = 'http://api.predator.wtf/minecraft/?arguments=' + username
	loading()
	webFile = urllib2.urlopen(url).read()
	print color.BOLD + color.GREEN + '\n' + webFile + color.END	
	return main()
	pass

def emailValidator():
	print color.BOLD + 'Type the email:' + color.END
	email = raw_input('> ')
	url = 'http://api.predator.wtf/emailv/?arguments=' + email
	loading()
	webFile = urllib2.urlopen(url).read()
	print color.BOLD + color.GREEN + '\n' + webFile + color.END	
	return main()
	pass

def clearConsole():
	#if you are using Windows just change 'clear' to 'cls'
	clear = lambda: os.system('clear')
	clear()
	pass
	
def loading():
	color()
	loadingStatus = "Loading, please wait..."
	print color.BOLD + loadingStatus + color.END
	pass
if __name__ == '__main__':
	main()


