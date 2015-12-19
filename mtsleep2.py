#!/usr/bin/python

# avoid using thread module, use threading instead
# in that thread support in the threading module is much improved and 
# threading allows the important child threads to finish first before exiting
# here for learning purposes only

import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
	print 'start loop', nloop, 'at:', ctime()
	sleep(nsec)
	print 'loop', nloop, 'done at:', ctime()
	lock.release()

def main():
	print 'starting at:', ctime()
	locks = []
	nloops = range(len(loops))

	# there are several reasons why we didn't start the threads in this lock
	# acquisition loop but in the next loop: 
	# 1) we wanted to synchronize the threads, so that "all the horses started
	# out the gate"
	# 2) locks take a little bit of time to be acquired. If thread excutes 
	# "too fast", it is possible to complete before lock is acquired
	for i in nloops:
		lock = thread.allocate_lock()
		lock.acquire()
		locks.append(lock)

	for i in nloops:
		thread.start_new_thread(loop, (i, loops[i], locks[i]))

	for i in nloops:
		while locks[i].locked():
			pass

	print 'all DONE at:', ctime()

if __name__ == '__main__':
	main()