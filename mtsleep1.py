#!/usr/bin/python

# avoid using thread module, use threading instead
# in that thread support in the threading module is much improved and 
# threading allows the important child threads to finish first before exiting
# here for learning purposes only

import thread
from time import sleep, ctime

def loop0():
	print 'start loop 0 at:', ctime()
	sleep(4)
	print 'loop 0 done at:', ctime()

def loop1():
	print 'start loop 1 at:', ctime()
	sleep(2)
	print 'loop 1 done at:', ctime()

def main():
	print 'starting at:', ctime()
	thread.start_new_thread(loop0, ())
	thread.start_new_thread(loop1, ())
	sleep(6)  # necessary, if not, main will exit and kill both threads
	print 'all DONE at:', ctime()

if __name__ == '__main__':
	main()