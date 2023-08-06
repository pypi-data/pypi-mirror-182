from sys import stderr, stdout
from colorama import Fore
from datetime import datetime

def log(msg):
    print(f'{Fore.GREEN}[LOG] {datetime.now()}{Fore.WHITE} {msg}', file=stdout)

def err(msg):
    print(f'{Fore.RED}[ERR] {datetime.now()}{Fore.WHITE} {msg}', file=stderr)
