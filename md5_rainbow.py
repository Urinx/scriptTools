#! usr/bin/env python
# coding:utf-8
# Author:Eular
import sys,hashlib

def md5_rainbow_table_generate(infile,outfile='md5_rainbow_table.txt'):
	f1=open(infile,'r')
	f2=open(outfile,'a')
	while 1:
		line=f1.readline().replace('\n','')
		if line:
			md5=hashlib.md5(line).hexdigest()
			f2.write(md5+' '+line+'\n')
		else:
			break
	f1.close()
	f2.close()
	print 'save in md5_rainbow_table.txt'

def md5_decode(psw,table='md5_rainbow_table.txt'):
	f=open(table,'r')
	while 1:
		line=f.readline().replace('\n','').split(' ')
		if line[0]:
			if psw==line[0]:
				print 'find the password:',line[1]
				break
		else:
			print 'not find'
			break
	f.close()

def usage():
	print '='*80
	print 'Usage:'
	print '*generate a md5 rainbow table'
	print '     %s -g [input] [output]' % sys.argv[0]
	print '*use a md5 rainbow table to decode password'
	print '     %s -d [password] [md5_rainbow_table]' % sys.argv[0]
	print '='*80

if __name__=='__main__':
	if len(sys.argv)<3 or sys.argv[1]=='-h':
		usage()
	else:
		if sys.argv[1]=='-g':
			md5_rainbow_table_generate(*sys.argv[2:])
		elif sys.argv[1]=='-d':
			md5_decode(*sys.argv[2:])