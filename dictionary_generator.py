#! usr/bin/env python
# coding:utf-8
# Author:Eular
# Version:1.5
import sys,itertools,time,os,string

def gen_dict(keys,k,fname='dictionary.txt'):
	f=open(fname,'a')
	dic=itertools.product(keys,repeat=int(k))
	for w in dic:
		f.write(''.join(w)+'\n')
	f.close()

def gen_dict_by_rule(rule,keys,fname):
	s=set(list(rule))
	k=len(s)
	f=open(fname,'a')
	for i in itertools.permutations(keys,k):
		table=string.maketrans(''.join(s),''.join(i))
		f.write(rule.translate(table)+'\n')
	f.close()

def gen_dict_by_rules(rules,keys,fname):
	for rule in rules:
		gen_dict_by_rule(rule,keys,fname)

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
	print '         -r set the rules as \'aabbccdd\''
	print '         -c common password made by given string'
	print 'eg:'
	print '     %s -bds 8 a.txt' % sys.argv[0]
	print '     %s -c \'0123456789\' a.txt' % sys.argv[0]
	print '     %s -l \'abcd\' 4 a.txt' % sys.argv[0]
	print '     %s -t yyyymmdd a.txt' % sys.argv[0]
	print '     %s -r \'aabbccdd\' \'0123456789\' a.txt' % sys.argv[0]
	print '     %s [\'1994\',\'uri\',\'12\',\'31\'] 4 a.txt' % sys.argv[0]
	print '='*80

if __name__=='__main__':
	if len(sys.argv)<4 or sys.argv[1]=='-h':
		usage()
	else:
		tStart=time.time()

		param=sys.argv[1]
		fname=sys.argv[-1]
		key={'b':'0123456789','d':'abcdefghijklmnopqrstvwxyz','D':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','s':'[!@#$%^&*()-_=+\|;:<>/?~{}]'}
		if sys.argv[1]=='-l':
			gen_dict(*sys.argv[2:])
		elif param=='-a':
			keys=''.join(key.values)
			gen_dict(keys,*sys.argv[2:])
		elif param=='-t':
			ymd=list(sys.argv[2])
			keys=[['19'*(ymd.count('y')/2-1)+str(i) for i in xrange(80,100)],[(ymd.count('m')-1)*(2-len(str(i)))*'0'+str(i) for i in xrange(1,13)],[(ymd.count('d')-1)*(2-len(str(i)))*'0'+str(i) for i in xrange(1,32)]]
			gen_dict(keys,'1',sys.argv[3])
		elif param=='-r':
			gen_dict_by_rule(*sys.argv[2:])
		elif param=='-c':
			rules=['a'*8,'a'*6,'aaaabbbb','aabb'*2,'ab'*4,'aabbbbaa','abcd'*2,'abcddcba','aabbccdd','abcdaaaa','aabbbbbb']
			gen_dict_by_rules(rules,*sys.argv[2:])
		elif param[0]=='-':
			keys=''
			for i in list(param[1:]):
				keys+=key[i]
			gen_dict(keys,*sys.argv[2:])

		print 'File Name:',fname
		print 'Size:',os.path.getsize(fname)/1024./1024,'M'
		print 'Finished in',time.time()-tStart,'s'
