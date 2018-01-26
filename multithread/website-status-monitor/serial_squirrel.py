#!/usr/bin/env python3
"""
Part of Website status monitor - serial way
"""

import time

from utils import check_website
from websites import WEBSITE_LIST

def do_serial():
    start_time = time.time()
    for address in WEBSITE_LIST:
        check_website(address)
    end_time = time.time()

    print('Time for serial squirrel: {}secs'.format(end_time - start_time))

# output at 1/26/2018
# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# Time for serial squirrel: 7.528430700302124secs


if __name__ == '__main__':
    do_serial()