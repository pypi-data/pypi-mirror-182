import sys
import typer
from colorama import Fore, Style
from tor_refresh.tor import Tor
from tor_refresh.utils import get_secure_password
from tor_refresh.exceptions import TorStartFailedException
from tor_refresh.logger import log, err

def main(port: int = typer.Argument(9150), control_port: int = typer.Argument(9151)):
    '''
    Main Function
    Starts the TOR instance and waits for user input.
    '''

    log(f'Welcome to {Fore.MAGENTA}TOR Refresh{Fore.WHITE}!')

    tor = Tor(port, control_port, get_secure_password(16))

    log(f'Starting TOR on port: {Fore.YELLOW}{port}{Fore.WHITE}, control_port: {Fore.YELLOW}{control_port}{Fore.WHITE}')

    try:
        tor.start()
        log('TOR was successfully bootstrapped')
    except TorStartFailedException:
        err('An error occurred while starting TOR, is something else using the same address?')
        sys.exit(-1)

    # Input cycle
    while True:
        print(f'\nCurrent address\t:\t{Fore.YELLOW}{tor.get_external_address()}{Fore.WHITE}\n')
        print(f'Hit {Fore.GREEN}\'r\'{Fore.WHITE} to refresh the TOR circuit')
        print(f'Hit {Fore.GREEN}\'e\'{Fore.WHITE} to exit')

        user_input = sys.stdin.read(1)

        if user_input == 'r':
            tor.renew_circuit()

        if user_input == 'e':
            break

        sys.stdin.flush()

    tor.stop()

if __name__ == '__main__':
    typer.run(main)
