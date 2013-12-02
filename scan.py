#! /usr/bin/python
import sys,socket,string,os,thread,threading,re

class ScanThread(threading.Thread):
    def __init__(self,param):
        super(ScanThread,self).__init__()
        self.param=param
        self.TCPserver={21:'FTP',22:'SSH',23:'Telnet',25:'SMTP',80:'HTTP',110:'POP3'}

    def run(self):
        self.ping(self.param)
        self.scanPort(self.param)

    def ping(self,param):
        print os.popen('ping '+param+' -c 4').read()
        print '======================================'
         
    def scanPort(self,param):
        ip=socket.gethostbyname(param)
        result=[]
        socket.setdefaulttimeout(1)
        for p in range(65535):
            try:
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,p))
                result.append(p)
                s.close()
            except Exception:
                pass
        print 'IP: '+param+' Open ports:'
        for p in result:
            if p in self.TCPserver:
                print '[*] '+str(p)+' '+self.TCPserver[p]
            else:
                print '[*] '+str(p)+' Unknown'
        print '======================================'
        
def usage():
    print 'Usage: ./scan.py [IP or name]|[options]'
    print 'eg:    ./scan.py 192.168.0.12-100'
    print 'opt:   -h help'
         
def main():
    if len(sys.argv)!=2 or sys.argv[1]=='-h':
        usage()
    else:
        if re.search(r'-',sys.argv[1]):
            ip=re.split(r'-|\.',sys.argv[1])
            head='.'.join(ip[:3])
            for i in xrange(string.atoi(ip[3]),string.atoi(ip[4])+1):
                ScanThread('.'.join([head,str(i)])).start()
        else:
            ScanThread(sys.argv[1]).start()
             
if __name__=='__main__':
    main()