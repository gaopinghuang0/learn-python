#!/usr/bin/env python3
"""
Part of Website status monitor - threading approach
"""


import time
from queue import Queue
from threading import Thread

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4
task_queue = Queue()

def worker():
    # Constantly check the queue for addresses
    while True:
        address = task_queue.get()
        check_website(address)

        # Mark the processed task as done
        task_queue.task_done()

start_time = time.time()

# Create the worker threads
threads = [Thread(target=worker) for _ in range(NUM_WORKERS)]

# Add the websites to the task queue
[task_queue.put(item) for item in WEBSITE_LIST]

# Start all the workers
[thread.start() for thread in threads]

# wait for all the tasks in the queue to be processed
task_queue.join()

end_time = time.time()

print('Time for Thread Squirrel: {}secs'.format(end_time - start_time))

# Output at 1/26/2018
# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# Time for Thread Squirrel: 2.8117380142211914secs
