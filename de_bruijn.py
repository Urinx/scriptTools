#! usr/bin/env python
# coding:utf-8
import sys

def de_bruijn(k,n):
	'''
	De Bruijn sequence for alphabet size k
	and subsequences of length n.
	'''
	a=[0]*k*n
	sequence=[]
	def db(t,p):
		if t>n:
			if n%p==0:
				for j in range(1,p+1):
					sequence.append(a[j])
		else:
			a[t]=a[t-p]
			db(t+1,p)
			for j in range(a[t-p]+1,k):
				a[t]=j
				db(t+1,t)
	db(1,1)
	return sequence

# |B(2,n)|=2^(2^(n-1)-n)
def num_of_de_bruijn(n):
	return 2**(2**(n-1)-n)

def usage():
	print 'Usage: %s [number]' % sys.argv[0]

if __name__=='__main__':
	if len(sys.argv)<2:
		usage()
	else:
		n=int(sys.argv[1])
		print 'Total number of De Bruijn sequence is:',num_of_de_bruijn(n)
		print 'One of all the sequences is:',de_bruijn(2,n)