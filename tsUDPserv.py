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
	udpSerSock = socket(AF_INET, SOCK_DGRAM)
	udpSerSock.bind(ADDR)

	while True:
		print 'waiting for message...'
		data, addr = udpSerSock.recvfrom(BUFSIZ)
		udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
		print '...receved from and returned to: ', addr

	udpSerSock.close()

if __name__=='__main__':
	main()
