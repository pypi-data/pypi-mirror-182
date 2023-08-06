import string_utils
import requests
from .exceptions import UnsecureLength

def get_secure_password(length: int=20) -> str:
    '''
    Returns a secure password of at least 12 characters
    Raises UnsecureLength
    '''

    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!#$%&?@'

    characters = ascii_lowercase + ascii_uppercase + digits + symbols

    if length < 12 or length > len(characters):
        raise UnsecureLength

    shuffled = string_utils.shuffle(characters)
    
    return shuffled[:length]

def get_ip_location(ip: str) -> str:
    '''
    Returns the location (State) of the passed IPv4 address
    '''

    res = requests.get(f'https://ipapi.co/{ip}/json')

    return res.json()['country_name']
