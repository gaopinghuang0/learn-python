#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def main():
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)

	while True:
		data = raw_input('> ')
		if not data:
			break
		tcpCliSock.send(data)
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		print data

	tcpCliSock.close()

if __name__=='__main__':
	main()
