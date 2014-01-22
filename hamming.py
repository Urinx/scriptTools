#! usr/bin/env python
# coding:utf-8
import sys,math

def ascii(c):
	b=str(bin(ord(c))).replace('0b','')
	return (7-len(b))*'0'+b

def splitn(s,n):
	a=[]
	for i in xrange(0,len(s)/n+1):
		a.append(s[n*i:n*i+n])
	if not a[-1]:
		a.pop()
	return a

def chr2bin(chrs):
	strbin=''
	for i in chrs:
		strbin+=ascii(i)
	return strbin

def bin2chr(bins):
	s=''
	arr=splitn(bins,7)
	for i in arr:
		s+=chr(int(i,2))
	return s

def getk(m):
	# m+k+1<2^k
	k=int(math.log(m+math.log(m+1,2)+1,2))
	if 2**k<=m+k+1:
		k+=1
	return k

def enhamming(bins):
	k=getk(len(bins))
	hamin=list(bins)
	for i in xrange(0,k):
		hamin.insert(2**i-1,'')
	for i in xrange(0,len(hamin)):
		if hamin[i]=='1':
			a=list(str(bin(i+1)).replace('0b',''))
			a.reverse()
			for i in xrange(0,len(a)):
				if a[i]=='1':
					hamin[2**i-1]=str(1-int(hamin[2**i-1]))
		elif not hamin[i]:
			hamin[i]='0'
	return ''.join(hamin)

def dehamming(hamins):
	hamins=list(hamins)
	k=getk(len(hamins))
	hamcheck=[]
	for i in xrange(0,k):
		hamcheck.append(hamins[2**i-1])
		hamins[2**i-1]=''

	bins=''
	for i in xrange(0,len(hamins)):
		if hamins[i]:
			bins+=str(hamins[i])

	hamins2=list(enhamming(bins))
	sum=0
	for i in xrange(0,k):
		if hamcheck[i]!=hamins2[2**i-1]:
			sum+=2**i
	if sum!=0:
		print 'Error: at [%d] byte.\nAuto check for right number.' % sum
		hamins[sum-1]=str(1-int(hamins[sum-1]))
		bins=''
		for i in xrange(0,len(hamins)):
			if hamins[i]:
				bins+=str(hamins[i])

	return bin2chr(bins)
	
def usage():
	print "Usage:"
	print "      %s -e 'somewords'" % sys.argv[0]
	print "      %s -d '10110110011'" % sys.argv[0]

if __name__=='__main__':
	if len(sys.argv)<3:
		usage()
	elif sys.argv[1]=='-e':
		print 'hamming:',enhamming(chr2bin(sys.argv[2]))
	elif sys.argv[1]=='-d':
		print 'words:',dehamming(sys.argv[2])