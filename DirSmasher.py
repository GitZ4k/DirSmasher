import concurrent.futures as con
import colorama
import os
import platform
from colorama import Fore, Style
import requests
import time
import datetime
colorama.init(autoreset=True)

if platform.system() == 'Windows':
    command = 'cls'
else:
    command = 'clear'
def anaconda():
    from rich import print
    banner = '\n\n' + fr'''[#01F9C6]                               /^\/^\
                             _|__|  O|
                    \/     /~     \_/ \
                     \____|__________/  \
                            \_______      \
                                    `\     \                 \
                                      |     |                  \
                                     /      /                    \
                                    /     /                       \\
                                  /      /                         \ \
                                 /     /                            \  \
                               /     /             _----_            \   \
                              /     /           _-~      ~-_         |   |
                             (      (        _-~    _--_    ~-_     _/   |
                              \      ~-____-~    _-~    ~-_    ~-_-~    /
                                ~-_           _-~          ~-_       _-~
                                   ~--______-~                ~-___-~
    ''' + '\n\n'
    delay = 0.04
    lines = banner.split('\n')
    for line in lines:
        print(f'[#01F9C6]{line}')
        time.sleep(delay)

os.system(command)

anaconda()
def current_time():
    return f"{datetime.datetime.now().strftime('%H:%M:%S')}"
def basic_url_checker(url):
    if not (url.startswith('https://') or url.startswith('http://')):
        url = 'https://' + url
        if not url.endswith('/'):
            url += '/'
    return url


RED=Fore.RED
GREEN=Fore.GREEN
YELLOW=Fore.YELLOW
BLUE=Fore.BLUE
MAGENTA=Fore.MAGENTA
CYAN=Fore.CYAN
WHITE=Fore.WHITE
GREY=Fore.LIGHTBLACK_EX 


current_time()

status_codes_input = input(f'{Style.BRIGHT}{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}>{MAGENTA}] | Status codes ->{WHITE} ')
status_codes = [int(code.strip()) for code in status_codes_input.replace(',','').split()]

current_time()
wordlist_input = input(f'{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}>{MAGENTA}] | Wordlist ->{WHITE} ')
current_time()
url_input = input(f'{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}>{MAGENTA}] | Website ->{WHITE} ')
url = basic_url_checker(url_input)
print(f'{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}~{MAGENTA}] | Scanning..')
time.sleep(2)

def brute_forcer(url, wordlist):
    total_found = 0
    start_time = time.perf_counter()
    total = len(open(wordlist, 'r').read().splitlines())
    def sender(url, directory):
        nonlocal total_found
        full_url = f'{url}{directory}'
        try:
            response = requests.get(full_url)
            if response.status_code in range(300, 400):
                main_color = YELLOW
            else:
                main_color = GREEN if response.status_code in range(200,300) else RED
            if response.status_code in status_codes:
                current_time()
                total_found += 1
                return f'{main_color}[{WHITE}{current_time()}{main_color}] [{WHITE}{Style.BRIGHT}{response.status_code}{main_color}] | {directory} --> {full_url}'
            return None
        except requests.exceptions.RequestException as error:
            time.sleep(3)
            return f'{RED}[{WHITE}{current_time()}{RED}] [{WHITE}!!!{RED}] | ERROR ->{RED} {error}'
    with con.ThreadPoolExecutor(max_workers=25) as exe:
        try:
            with open(wordlist, 'r', errors='ignore') as f:
                words = f.read().splitlines()
                tasks = []
                for word in words:
                    task = exe.submit(sender, url, word)
                    tasks.append(task)
                for task in con.as_completed(tasks):
                    result = task.result()
                    if result:
                        print(f'{result}')
        except FileNotFoundError:
            print(f'{RED}File: {wordlist} not found!')
        except Exception as e:
            print(f'{RED}{e}')
    print(f'{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}@{MAGENTA}] | {round(time.perf_counter()-start_time, 1)} seconds --> {total_found} / {total}')

brute_forcer(url, wordlist_input)



