from Modules import Views
import os 
from colorama import Fore, Style
from art import *

def logo():
    pic = text2art("solo.to")
    print(Fore.RED + pic + Fore.RESET)
    print("""\n
    [HELP]
    Use \"set target [username] \" to define the username of the account you want to view bot.
    [1] View botter
    [2] Clear terminal and reprint banner
    """)
def clean():
    if os.name == "nt":
        l = os.system('cls')
    
    else:
        l = os.system("clear")

    logo()

clean()
def handler():
    
    target = 'Null'
    username = os.getlogin()
    while True:
        try:
            command = input(f'{Fore.RED} {Style.BRIGHT}${Fore.RESET} {username}(target={target}) > ')
            if "set target" in command.lower():
                target = command.split('target')[1].replace(' ', '')
                if target == '':
                    print("You didnt actaully enter a target sperg")
                    target = 'Null'

            if command.lower() == "1":
                clean()
                print("View botter has been chosen! Use Ctrl + C to exit the program and stop view botting. Or wait for views to finish botting and then press enter.")
                Views.run(target)

            elif command.lower() == "3":
                clean()    
        
        except KeyboardInterrupt as err:
            print(Fore.RED + "\nKeyboard interrupt called exiting program..." + Fore.RESET)
            break