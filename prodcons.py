#!/usr/bin/python

from random import randint
from Queue import Queue
from myThread import MyThread
from time import sleep

def writeQ(queue):
	print 'producing object for Q...',
	queue.put('xxx', 1)
	print 'size now', queue.qsize()

def readQ(queue):
	val = queue.get(1)
	print 'consumed object from Q... size now', queue.qsize()

def writer(queue, loops):
	for i in range(loops):
		writeQ(queue)
		sleep(randint(1, 3))

def readr(queue, loops):
	for i in range(loops):
		readQ(queue)
		sleep(randint(2, 5))

funcs = [writer, readr]
nfuncs = range(len(funcs))


def main():
	nloops = randint(2, 5)
	q = Queue(32)

	threads = []
	for i in nfuncs:
		t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:  # start threads
		threads[i].start()

	for i in nfuncs:  # wait for all threads to finish
		threads[i].join()

	print 'all DONE'

if __name__ == '__main__':
	main()