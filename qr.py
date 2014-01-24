#!usr/bin/env python
# encoding:utf-8
import qrcode,sys

def qr(data,path='qr.png'):
	qr=qrcode.QRCode(
		version=5,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=4,
		)
	qr.add_data(data)
	qr.make()
	img=qr.make_image(fit=True)
	img.save(path)

def usage():
	print 'Usage:{0} data path'.format(sys.argv[0])
	print "eg:%s 'some words' 'a.png'" % sys.argv[0]

if __name__=='__main__':
	if len(sys.argv)<3:
		usage()
	else:
		qr(sys.argv[1],sys.argv[2])