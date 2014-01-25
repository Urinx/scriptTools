#! usr/bin/env python
# coding:utf-8
# Author:Eular
import sys

def dictionary(keys,k,fname='dictionary.txt'):
	####################
	def generate(key,n):
		if n==1:
			return key
		else:
			arr=[]
			for i in generate(key,n-1):
				for j in key:
					arr.append(i+j) 
			return arr
	####################
	def generate2(key,n):
		if n==1:
			return key[n-1]
		else:
			arr=[]
			for i in generate2(key,n-1):
				for j in key[n-1]:
					arr.append(i+j) 
			return arr
	####################
	if type(keys)==list:
		arr=generate2(keys,k)
	else:
		arr=generate(keys,k)
	f=open(fname,'w')
	f.write('\n'.join(arr))
	f.close()
	print 'successfully done.'
	

def usage():
	print '='*80
	print 'Usage:'
	print '     %s [options | keys] [length] [filename]' % sys.argv[0]
	print '         -a all the param:[0-9a-zA-Z!@#$%^&*()-_=+\|;:<>/?~{}]'
	print '         -b only numbers:[0-9]'
	print '         -d only low-case letters:[a-z]'
	print '         -D only upper-case letters:[A-Z]'
	print '         -s special characters:[!@#$%^&*()-_=+\|;:<>/?~{}]'
	print '         -l list of given string'
	print '         -t dates from 1980.01.01-1999.12.31: yyyymmdd | yymmdd | yyyymd | yymd'
	print 'eg:'
	print '     %s -bds 8 a.txt' % sys.argv[0]
	print '     %s -l \'abcd\' 4 a.txt' % sys.argv[0]
	print '     %s -t yyyymmdd a.txt' % sys.argv[0]
	print '     %s [\'1994\',\'uri\',\'12\',\'31\'] 4 a.txt' % sys.argv[0]
	print '='*80
	

if __name__=='__main__':
	if len(sys.argv)<4 or sys.argv[1]=='-h':
		usage()
	elif len(sys.argv)==5 and sys.argv[1]=='-l':
		dictionary(list(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
	else:
		param=sys.argv[1]
		fname=sys.argv[3]
		key={'b':'0123456789','d':'abcdefghijklmnopqrstvwxyz','D':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','s':'[!@#$%^&*()-_=+\|;:<>/?~{}]'}
		if param=='-a':
			a=[]
			for i in key:
				a.extend(list(key[i]))
			k=int(sys.argv[2])
			dictionary(a,k,fname)
		elif param=='-t':
			ymd=list(sys.argv[2])
			a=[['19'*(ymd.count('y')/2-1)+str(i) for i in xrange(80,100)],[(ymd.count('m')-1)*(2-len(str(i)))*'0'+str(i) for i in xrange(1,13)],[(ymd.count('d')-1)*(2-len(str(i)))*'0'+str(i) for i in xrange(1,32)]]
			dictionary(a,3,fname)
		else:
			a=[]
			for i in list(param.replace('-','')):
				a.extend(list(key[i]))
			k=int(sys.argv[2])
			dictionary(a,k,fname)