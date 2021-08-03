import threading
import requests
from colorama import *
import os 


def Botter(target, views):
    global i
    url = f"http://solo.to/{target}"
    i = 0
    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; Win64, x64)'}
    while i < views:
        try:
            response = requests.get(url, headers=header)
            if response.status_code == 200:
                print(Fore.GREEN + "Botted successfully\n")
                i = i + 1
                os.system(f"title Active threads: {threading.active_count()} Current views: {i}")
                continue
            else:
                print(Fore.RED + f"Server has denied request or the username has not been found\n")
                continue
        except requests.ConnectionError:
            print(Fore.RED + "Failed to communicate with server!\n")
            print(Fore.GREEN + "Retrying")
            continue
        except requests.exceptions.HTTPError as err:
            print(Fore.RED + f"Error:{err}\n")
            continue




def main(target):
    threads = int(input("Threads: "))
    amountofViews = int(input("Views: "))
    for _ in range(threads):
        t = threading.Thread(target = Botter, args = (target, amountofViews))
        t.daemon = True
        t.start()

def run(target):
    main(target)