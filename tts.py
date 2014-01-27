#! usr/bin/env python
import sys,subprocess,urllib,platform

def getSpeech(phrase):
	googleAPIurl='http://translate.google.com/translate_tts?tl=en&'
	param={'q':phrase}
	data=urllib.urlencode(param)
	googleAPIurl+=data
	return googleAPIurl

def mplayerTalk(text):
	subprocess.call(['mplayer',getSpeech(text)],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def MacSay(text,param='',out=''):
	subprocess.call(['say',text,param,out],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def usage():
	print '='*80
	print 'Usage:'
	print '     %s [-f input | words] [-o output]' % sys.argv[0]
	print 'eg:'
	print '     %s hello,world' % sys.argv[0]
	print '     %s -f words.txt' % sys.argv[0]
	print '     %s hello,world -o yuyin.aiff' % sys.argv[0]
	print '='*80

if __name__=='__main__':
	if len(sys.argv)<2:
		usage()
	else:
		if platform.system()=='Darwin':
			if sys.argv[1]=='-f':
				f=open(sys.argv[2],'r')
				MacSay(f.read())
			else:
				MacSay(*sys.argv[1:])
		elif platform.system()=='Linux':
			mplayerTalk(sys.argv[1])
		elif platform.system()=='Windows':
			print 'Sorry,it\'s not supported for Windows'