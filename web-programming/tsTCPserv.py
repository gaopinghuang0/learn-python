#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def main():
	tcpSerSock = socket(AF_INET, SOCK_STREAM)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(5)

	while True:
		print 'waiting for connection...'
		tcpCliSock, addr = tcpSerSock.accept()
		print '...connected from:', addr

		while True:
			data = tcpCliSock.recv(BUFSIZ)
			if not data:
				break
			print 'receved: ', data
			tcpCliSock.send('[%s] %s' % (ctime(), data))

		tcpCliSock.close()

	tcpSerSock.close()

if __name__=='__main__':
	main()
