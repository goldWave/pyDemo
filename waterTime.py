# -*- coding: utf-8 -*-

import os
import exifread
from PIL import Image, ImageFont, ImageDraw
import re
import datetime

# Src_path="test"
Src_path="ming"
time_key="EXIF DateTimeOriginal"

def exifread_infos(photo):
	f = open(photo, 'rb')
	tags = exifread.process_file(f)

	dateStr=""
	if time_key in tags:
		dateStr = tags[time_key].printable
	else:
		a = os.path.basename(photo).split('.')[0]
		try:
			#微信图片_20210126154236
			d = re.sub('微信图片_([0-9]+)$', r'\1', a)
			dateStr = datetime.datetime.strptime(d, '%Y%m%d%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
		except:
			try:
				#2020-11-09 214158
				dateStr = datetime.datetime.strptime(a, '%Y-%m-%d %H%M%S').strftime('%Y-%m-%d %H:%M:%S')
			except:
				pass
	f.close()

	return dateStr


def add_watermark(fimename, text, newpath):

	im=Image.open(fimename).convert('RGBA')
	if len(text)<1:
		return im

	 # 新建一个空白图片,尺寸与打开图片一样
	txt=Image.new("RGBA", im.size, (0,0,0,0))
	# 操作新建的空白图片>>将新建的图片添入画板
	d=ImageDraw.Draw(txt)

	width, height=im.size
	size=int(0.04*width)
	myfont=ImageFont.truetype("C:/windows/Fonts/ARIAL.TTF", size=size) #80 4032*3024
	fillcolor = '#fbfafe'

	d_width, d_height=0.5*width, 0.92*height
	# d.text((d_width, d_height), text, font=myfont, fill=fillcolor)
	#左下角
	d.text((0.1*width, 0.92*height), text, font=myfont, fill=fillcolor)
	# image.save(newpath)
	out=Image.alpha_composite(im, txt)

	#jpg 不含aplpha 通道，所以先转成没有alpha再保存
	out=out.convert('RGB') 
	return out

def saveTargetData(out, tarPath):
	out.save(tarPath, quality=99)


def is_img(x):
	pattern = re.compile(".jpg|.png|.jpeg")
	# pattern = re.compile(".heic")
	_a=pattern.findall(x)
	return len(_a)>0

def main():
	listDir = os.listdir(Src_path)
	out_ = Src_path + "/out"
	if (not os.path.exists(out_)):
		os.mkdir(out_)

	for item in listDir:
		_is_img=is_img(item)
		if(not _is_img):
			continue

		src=Src_path+"/"+item
		time = exifread_infos(src)
		newpath = out_+'/'+item
		waterImage = add_watermark(src, time,newpath)
		saveTargetData(waterImage, newpath)


if __name__ == '__main__':
	main()