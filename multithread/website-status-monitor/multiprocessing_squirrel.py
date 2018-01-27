#!/usr/bin/env python3
"""
Part of Website status monitor - multiprocessing approach
It's very similar to `concurrent.futures`, but for processes not threads
"""


import time
import multiprocessing

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

start_time = time.time()

with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
    results = pool.map_async(check_website, WEBSITE_LIST)
    results.wait()

end_time = time.time()

print('Time for Multiprocessing Squirrel: {}secs'.format(end_time - start_time))

# Output at 1/26/2018
# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# Time for Multiprocessing Squirrel: 2.562021017074585secs
