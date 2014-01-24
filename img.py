#! usr/bin/env python
# coding:utf-8
import Image,sys,ImageFilter,ImageEnhance,random,ImageDraw,ImageFont

def img_info(im):
	print 'Info:',im.info
	for i in im.info:
		print '%s:%s' % (i,im.info[i])
	print 'Size:',im.size
	print 'Mode:',im.mode
	print 'Format:',im.format

def paste(im):
	a,b=im.size
	l=200
	area=((a-l)/2,(b-l)/2,(a+l)/2,(b+l)/2)
	tmp=im.crop(area)
	tmp=tmp.transpose(Image.ROTATE_180)
	im.paste(tmp,area)
	im.show()

def split(im):
	im=im.convert('RGB')
	r,g,b=im.split()
	r.show()
	g.show()
	b.show()
	tmp=Image.merge('RGB',(b,g,r))#将b,r两个通道进行翻转
	tmp.show()

def split2(im):
	im=im.convert('RGB')
	r,g,b=im.split()
	r=r.point(lambda i:i*299/1000)
	g=g.point(lambda i:i*578/1000)
	b=b.point(lambda i:i*144/1000)
	tmp=Image.merge('RGB',(r,g,b))
	tmp.show()

def blend(img1,img2,alpha):
	out=img1.resize(img2.size)
	Image.blend(out,img2,alpha).show()

def other(im):
	#out=im.rotate(45)
	#out=im.filter(ImageFilter.DETAIL)
	out=ImageEnhance.Contrast(im)
	out.enhance(1.5).show('50% more contrast')

def hideInfo(im,info):
	if im.mode!='RGBA':
		im=im.convert('RGBA')
	if info.mode!='L' and info.mode!='1':
		info=info.convert('L')
	im.putalpha(info)
	return im

def getInfo(im):
	im.split()[3].show()

def putpalette(im):
	im=im.convert('L')
	im.putpalette([random.randint(0,255) for i in xrange(100)])
	im.show()

def transform():
	#im.transform(size,method,data)
	#method:
	#EXTENT 剪一个矩形出来(用以剪切，拉伸，压缩等操作)
	#AFFINE 几何防射转换
	#QUAD 将一个四边形映射到一个矩形
	#MESH 将多个四边形映射到一个操作
	
	#im.transpose(method)
	#method:
	#FLIP_LEFT_RIGHT 左右倒置
	#FLIP_TOP_BOTTOM 上下倒置
	#ROTATE_90 旋转90度(逆时针)
	pass

def draw(im):
	draw=ImageDraw.Draw(im)
	a,b=im.size
	color=(255,0,0)
	draw.line(((0,0),(a-1,b-1)),fill=color)
	draw.line(((0,b-1),(a-1,0)),fill=(0,255,0))
	draw.arc((0,0,a-1,b-1),0,360,fill=(0,0,255))
	ft=ImageFont.truetype('1.ttf',22)
	draw.text((110, 90),'Eular',fill=(0,0,0),font=ft)
	del draw
	im.show()

def usage():
	print 'Usage: %s path' % sys.argv[0]

def main(path,path2=''):
	im=Image.open(path)
	if path2:
		im2=Image.open(path2)
	#img_info(im)
	#paste(im)
	#split(im)
	#split2(im)
	#other(im)
	#blend(im,im2,0.6)
	#out=hideInfo(im,im2)
	#putpalette(im)
	draw(im)

if __name__=='__main__':
	if len(sys.argv)<2:
		usage()
	else:
		main(*sys.argv[1:])