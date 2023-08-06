import atexit
import readchar
import sys
import typer
from colorama import Fore
from datetime import datetime
from rich.live import Live
from rich.table import Table
from tor_refresh.tor import Tor
from tor_refresh.utils import get_secure_password, get_ip_location
from tor_refresh.exceptions import TorStartFailedException
from tor_refresh.logger import log, err
from tor_refresh.clean import clean_at_exit

def main(port: int = typer.Argument(9150), control_port: int = typer.Argument(9151)):
    '''
    Main Function
    Starts the TOR instance and waits for user input.
    '''

    log(f'Welcome to {Fore.MAGENTA}TOR Refresh{Fore.WHITE}!')

    # Register exit handler
    atexit.register(clean_at_exit)

    tor = Tor(port, control_port, get_secure_password(16))

    log(f'Starting TOR on port: {Fore.YELLOW}{port}{Fore.WHITE}, control_port: {Fore.YELLOW}{control_port}{Fore.WHITE}')

    try:
        tor.start()
        log('TOR was successfully bootstrapped')
    except TorStartFailedException:
        err('An error occurred while starting TOR, is something else using the same address?')
        sys.exit(-1)

    # Output table
    table = Table(caption=f'Hit {Fore.GREEN}\'r\'{Fore.WHITE} to refresh the TOR circuit\nHit {Fore.GREEN}\'e\'{Fore.WHITE} to exit')

    table.add_column('Refresh date', style='Green')
    table.add_column('IP Address', style='Yellow')
    table.add_column('IP Location', style='Cyan')

    with Live(table, refresh_per_second=5):
        while True:
            address = tor.get_external_address()
            location = 'Unknown'

            try:
                location = get_ip_location(address)
            except:
                pass

            table.add_row(f'{datetime.now()}', f'{address}', f'{location}')
            table.caption = f'Hit {Fore.GREEN}\'r\'{Fore.WHITE} to refresh the TOR circuit\nHit {Fore.GREEN}\'e\'{Fore.WHITE} to exit'

            user_input = readchar.readchar()

            if user_input == 'r':
                table.caption = 'Refreshing...'
                tor.renew_circuit()

            if user_input == 'e':
                break

    tor.stop()

if __name__ == 'tor_refresh':
    typer.run(main)
