#!/usr/bin/env python3
"""
Part of Website status monitor - Gevent approach

Note:
* Code performed concurrently by greenlets is deterministic.
It guarantees that for any two identical runs, you'll always get the same results in the same order.
* You need to monkey patch standard functions so that they cooperate with gevent. See more explanation from
https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612
"""

import time
from gevent.pool import Pool
from gevent import monkey

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

# monkey-patch socket module for HTTP requests
monkey.patch_socket()

start_time = time.time()

pool = Pool(NUM_WORKERS)
for address in WEBSITE_LIST:
    pool.spawn(check_website, address)

# wait for stuff to finish
pool.join()

end_time = time.time()

print('Time for Gevent Squirrel: {}secs'.format(end_time - start_time))

# Output at 1/26/2018
# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# Time for Gevent Squirrel: 3.903378963470459secs

# Note that the order will remain the same if we run it again
