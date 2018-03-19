#!/usr/bin/env python3
"""
Part of Website status monitor - concurrent.futures approach
"""


import time
import concurrent.futures 

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    tasks = {executor.submit(check_website, address) for address in WEBSITE_LIST}
    concurrent.futures.wait(tasks)

end_time = time.time()

print('Time for Future Squirrel: {}secs'.format(end_time - start_time))

# Output at 1/26/2018
# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# Time for Future Squirrel: 2.0710461139678955secs
