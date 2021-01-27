# -*- coding: utf-8 -*-

import os, io
import exifread
from PIL import Image, ImageFont, ImageDraw
import re
import datetime
import time
import whatimage
import pyheif
import piexif

# Src_path="test"
Src_path="/Users/jimbo/Documents/waterPhoto"
time_key="EXIF DateTimeOriginal"

def exifread_infos(photo):
	f = open(photo, 'rb')
	tags = exifread.process_file(f)

	dateStr=""
	if time_key in tags:
		dateStr = tags[time_key].printable
	else:
		iName = os.path.basename(photo).split('.')[0]
		if "mmexport" in iName:
			timeStamp = re.sub('mmexport([0-9]+)$', r'\1', iName)
			iTime = int(timeStamp)
			timeArray = time.localtime(iTime/1000)
			dateStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		elif "微信图片_" in iName:
			d = re.sub('微信图片_([0-9]+)$', r'\1', iName)
			dateStr = datetime.datetime.strptime(d, '%Y%m%d%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
		else:
			try:
				#2020-11-09 214158
				dateStr = datetime.datetime.strptime(iName, '%Y-%m-%d %H%M%S').strftime('%Y-%m-%d %H:%M:%S')
			except:
				print(photo)
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

def is_heic_img(x):
	pattern = re.compile(".heic")
	# pattern = re.compile(".heic")
	_a=pattern.findall(x)
	return len(_a)>0

def read_image_file_rb(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return file_data

def convertHECIToJpg(path):
	//"/Users/jimbo/Desktop/test/IMG_2549.HEIC.heic"
	heif_file = pyheif.read(path)
	# Creation of image 
	image = Image.frombytes(heif_file.mode,heif_file.size,heif_file.data,"raw",heif_file.mode,heif_file.stride,)
	# Retrive the metadata
	for metadata in heif_file.metadata or []:
		if metadata['type'] == 'Exif':
			exif_dict = piexif.load(metadata['data'])

	# PIL rotates the image according to exif info, so it's necessary to remove the orientation tag otherwise the image will be rotated again (1° time from PIL, 2° from viewer).
	exif_dict['0th'][274] = 0
	exif_bytes = piexif.dump(exif_dict)
	file_path_jpeg="/Users/jimbo/Desktop/test/IMG_2549.jpg"
	image.save(file_path_jpeg, "JPEG", exif=exif_bytes)
	

def main():
	listDir = os.listdir(Src_path)
	out_ = Src_path + "/out"
	if (not os.path.exists(out_)):
		os.mkdir(out_)

	for item in listDir:
		_is_img=is_img(item)
		_is_heic=is_heic_img(item)
		if(not _is_img or _is_heic):
			continue

		#continnuce
		src=Src_path+"/"+item
		if _is_heic:
			convertHECIToJpg(src)
			pass

		time = exifread_infos(src)
		newpath = out_+'/'+item
		waterImage = add_watermark(src, time,newpath)
	# 	saveTargetData(waterImage, newpath)
 #    print('file_path = ', file_path) 
	# data = read_image_file_rb('/Users/jimbo/Desktop/test/IMG_2549.HEIC.heic')
 #    print('data = ', data)
	





if __name__ == '__main__':
	main()