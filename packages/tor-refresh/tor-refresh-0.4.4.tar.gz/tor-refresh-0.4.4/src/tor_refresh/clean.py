import shutil
from .logger import err, log

def clean_at_exit():
    try:
        shutil.rmtree('/tmp/tor_refresh')
        log('The storage directory was successfully removed')
    except OSError:
        err('Could not clean the storage directory, clean by hand using \'rm -r /tmp/tor_refresh\'')
