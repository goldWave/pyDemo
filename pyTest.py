# encoding=utf8
# -*- coding: utf-8 -*-
#!/usr/bin/env python3.8
 


# # x = ["123456", 9]
# # x += [4444]
# # x.append(3333)
# # x.remove(9)
# # print(len(x), x, x[0][3])

# # x = int(input("Please enter an integer: "))

# # print("value:", x)
# # if x < 0:
# # 	print('Negative changed to zero')
# # elif x == 0:
# # 	print('Zero')
# # elif x == 1:
# # 	print('Single')
# # else:
# # 	print('More')

# # words=['sdfds', 'cat', 'dog']

# # for w in words[:]:
# # 	for x in w:
# # 		# print(x, len(x))
# # 		if x=='c':
# # 			words.insert(0, 'x')
# # 			pass


# # print(words)

# # for x in range(4,8, 2):
# # 	print(x)
# # 	pass

# # a = ['May', 'have', 'one', 'little', 'lamda']
# # for x in range(len(a)):
# # 	print(x, a[x])
# # 	for x in range(1,10):
# # 		pass


# # 		# print(list[range(11)])

# # for n in range(2, 10):
# # 	for x in range(2, n):
# # 		if n % x == 0:
# # 			print(n, 'equals', x , '*', n/x)
# # 			break
# # 	else:
# # 		print(n , 'is a prime number')

# # def fib(n):
# # 	"""print a finbonacci series up to n"""
# # 	a, b = 0, 1
# # 	# c=areturn a
# # 	c = []
# # 	while a < n:
# # 		# print(a, end=' ')
# # 		c.append(a)
# # 		a,b = b, a+b
	
# # 		pass
# # 	# print()
# # 	return c

# # f = fib

# # # f(111)

# # print(f(1111))

# # def ask_ok(prompt, retries=4, complaint='yes or no, Please'):
# # 	while True:
# # 		ok=input(prompt)
# #` 		if ok in ('y', 'ye', 'yes'):
# # 			return True
# # 		if ok in ('n', 'no', 'nop'):
# # 			return False
# # 		retries -= 1;
# # 		if retries < 0:
# # 			raise OSError("not right  value of ok")
# # 		print(prompt)
# # 	pass

# # ask_ok("ooooo:", 2, "try")
# # i = 4
# # def f(arg=i):
# # 	i = 8
# # 	print(i)
# # 	pass
# # f()
# # print(i)
# # f()

# # x = list(range(2,5))
# # def parret(vlitage, state="a stiff", action="voom"):
# # 	print(vlitage)
# # 	pass

# # d = {"aasaa", "bbbbbb", "cccccc", "dddddd"}

# # parret(**d)

# # def parrot(voltage, state='a stiff', action='voom'):
# #     print("----", action)
# #     print(voltage)
# #     print("]]]]]]]", state, "!")
# # d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# # parrot(**d)

# # def make_a(n):
# # 	return lambda x: x+n
# # 	pass

# # # f =  make_a(42)
# # # print(f(33))

# # print(make_a(make_a(3)))

# # pairs = [(2, 'two'), (1, 'one'), (3, 'three'), (1000, 'four')]
# # pairs.sort(key=lambda pair: pair[1])
# # # pairs.sort()
# # print(pairs)

# # def dogS():
# # 	"""DDDOsdf啥的积分雷克萨进度
    
# # 	飞洒冷风机色拉可激发了上来减肥沙发色分看见爱上饭
# # 	fesjfaelsa费劲儿索拉卡就分手飞洒而非加上了房价撒了房价来看工地上干活的三个号多少
# # 	"""
# # 	pass


# # print(dogS.__doc__)

# # suquares = [x**2 for x in range(10)]
# # suquares = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# # print(suquares)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# # re =  [[row[i] for row in matrix] for i in range(4)]
# # print(re)

# # for row in matrix:
# # 	print(row)
# # 	pass


# # transposed = []
# # for i in range(4):
# #     transposed.append([row[i] for row in matrix])
# # print(transposed)

# print([row[1] for row in matrix])

# d = ["aasaa", "bbbbbb", "cccccc", "dddddd"]
# # del d[0]
# del d
# print(d)

# t = "1212", 123,  "lfkdf 元组 "
# # # t[0] = "f"
# # u = t, (1, 3,5)
# # # print(u[0][0])

# # a = ("fff", )
# # print(a)

# x , y , z = t

# print(x)

# []列表  ,元祖  set{}集合 {df:fdf}字典

# a = {'abc', 'apple', 'sss', 'apple'}
# print(a)

# print('abc' in a)

# b = set("abcdee")
# c = set("abjkljjj")
# print(b)
# print(c)

# print(b-c)
# print(b&c)
# print(b|c)
# print(b^c)

# a = {'a':1, 'b':2}
# print(a)
# a['a'] = 4
# b = list(a.keys())
# print(b)

# for k , i in a.items():
# 	print(k, i)
# 	pass


# for k, v in enumerate(a):
# 	print(k, v)
# 	pass

# fibo.fib(1000)
# fibo.fib2(100)

# from fibo import fib, fib2
# import sys, fibo, builtins

# print(dir(fibo))
# print(sys)
# print(dir())
# print(builtins)
# sys.stdout

# s = "hello, world 中文"
# print(str(s))

# print(repr(s))

# h = s + "\n"
# print(h)
# print(str(h))
# print(repr(h))

# for x in range(1, 11):
	# print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
	# print(repr(x*x*x).rjust(5))
	# print(repr(x*x*x).zfill(4))
	# print('{0:3d}'.format(x))

# print(f"this is test demo {s!s}")

# asi = "\\u594b\\u6597" #奋斗

# print('{1} who say {0}'.format(s, "fefdsjlfk"))
# print('We are the {} who {xxx!a} say {}'.format(s, "fefdsjlfk", xxx="fdsj奋斗"))
# print("chinese {!s}".format(asi))
# print(asi.encode().decode('unicode_escape'))



# import math

# print('pi is {:.114f}'.format(math.pi))

# table = {'a1': 444, 'a2': 666}
# print("a1, {a1}, {a2}".format(**table))


# f = open('testRead.txt', 'w')
# # print(f.read())
# # for line in f:
# # 	print(f.readline(), end='')
# # print(f.read())
# # t = f.read()
# t = "e是eeee"
# print(t, "----------------")
# if f.writable():
# 	print('this' , f.writable())
# 	f.write(str(t))
# 	pass

# f = open('testRead.txt', 'rb+')
# print(f.write(b'0123456789abcdef'))
# print(f.seek(5))
# print(f.seek(-3, 2))
# f.close()
# print(f.read(2))

# 10/0



# def scope_test():
# 	spam = "test"
# 	def do_local():
# 		spam = "local"
# 	def do_nonlocal():
# 		nonlocal spam
# 		spam = "nonlocal"
# 	def  do_global():
# 		global spam
# 		spam = "global"


# 	# do_local()
# 	# print(spam)

# 	# do_nonlocal()
# 	# print("non", spam)

# 	do_global()
# 	print(spam)

# scope_test()
# print(spam)


# class testClass(object):
# 	"""docstring for testClass"""
# 	def __init__(self):
# 		super(testClass, self).__init__()
# 		# self.arg = arg

# 	__spam = "jimbo"
# 	def pTest():
# 		print("hello, world!!")
# 		pass

# class Top(testClass):

# 	pass



# testClass.pTest()
# testClass.spam = "jjjjjj"
# print(testClass.spam)
# print("================")
# x = testClass()
# print(x.spam)
# # x.pTestf



# a = testClass()
# b = Top()

# # a.spam = "aaaa"
# # b.spam = "bbbb"

# testClass.spam = "tttt"

# print(a.spam)
# print(b.spam)
# print(issubclass(Top, testClass))

# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # private copy of original update() method

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
# 	        self.items_list.append(item)

# class EmptyC:
# 	pass

# jo = EmptyC()
# jo.c = "eeee"
# jo.b = 33

# print(jo.__class__)

# for x in range(1,10):
# 	print(x, end='\t')
# 	pass

# print(sum(i+2 for i in range(10)))

# import os

# print(os.__doc__)
# print("-------------------")

# print(os.getcwd())
# os.chdir('C:\\Users\\jimbo\\Documents\\document\\pyTest.py')
# os.chdir('..\\')
# os.system('mkdir today')

# help(os)
# print(dir(os))

# import shutil

# shutil.copyfile('pyTest.py', 'py2.py')
# shutil.move('py2.py', '../py.py')

# import glob, os
# os.chdir('C:\\Users\\jimbo\\source\\prism_old\\livecast\\src')
# x = glob.glob('**/*.xib', recursive=True)
# print(x)


# from urllib.request import urlopen
# for line in urlopen("http://www.baidu.com"):
# 	line = line.decode('utf-8')
# 	if "<script>" in line:
# 		print(line)
# 	pass

# from datetime import date
# now =  date.today()
# print(now)
# now2 = now.strftime("%m-%d_%Y")
# print(now2)

# bir = date(1933, 4, 14)
# print(bir)

# from datetime import timedelta

# delta = timedelta(
# 	days=0,
# 	seconds=27,
# 	microseconds=10,
# 	milliseconds=29000,
# 	minutes=5,
# 	hours=8,
# 	weeks=1
# 	)
# print(delta)

# import zlib
# # s = b'this is good boy hha blala fdsfjla dsjflkjsjlf  jfkdlsafj  lfkdjsalflk j flsjdkajs '
# s = b'1 *'
# print(len(s))

# # t = zlib.compress(s)
# # print(len(t))
# # print(t)
# # d = zlib.decompress(t)
# # print(d)
# print(zlib.crc32(s))
# # 2452822132
# # 3871838783
# # 3097649048
# # 4279777642
# # 3858958379

# import time, os.path
# from string import Template

# photoFiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# print(photoFiles)

# class BatchRename(Template)
# 	delimiter = '%'

# fmt = input('enter rename style (%d-date %n-seqnum %f-formate): ')

# import threading, zipfile

# import weakref, gc
# class A:
#     def __init__(self, value):
#         self.value = value
#     def __repr__(self):
#         return str(self.value)
# a = A(10)                   # create a reference
# # d = weakref.WeakValueDictionary()
# d = {}
# d['primary'] = a            # does not create a reference
# d['primary']                # fetch the object if it is still alive
# del a                       # remove the one reference
# gc.collect()                # run garbage collection right away
# print(a)                # entry was automatically removed

# from array import array
# a = array('H', [4000, 10, 700, 22222])
# a = [4000, 10, 700, 22222]
# print(sum(a))
# print(a[1:3])

# d = ['a1', 'a2', 'a3']
# d.append('a4')
# print(d[0])

# print(0.1+0.1+0.1==0.3)

# import os

# import glob, os
# dir = "C:\\Users\\jimbo\\source\\prism_old\\livecast"
# os.chdir(dir)
# files = glob.glob('**/*.xib', recursive=True)

# for file in files:
# 	print(file)
# 	pass
# print(len(files))

# dir = "C:\\Users\\jimbo\\Documents\\document\\test.xib.xml"
# dir2 = "C:\\Users\\jimbo\\Documents\\document\\test2.xib.xml"

# with open (dir, 'r') as f:
# 	lines = f.readlines()
# 	deleteLine = input("<capability name=\"documents saved in the Xcode 8 format\" minToolsVersion=\"8.0\"/>")
# 	# f.seek(0)
# 	for line in lines:
# 		# if deleteLine not in line:
# 		# 	f.write(line)
# 		print(line) 
	# f.truncate()

# <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>

# import glob, os, sys
# def findXib(topFile):
# 	os.chdir(topFile)
# 	files = glob.glob('**/*.xib', recursive=True)
# 	for file in files:
# 		rWriteData(topFile+ '\\' + file)
# 	pass

# def rWriteData(dir):
# 	print(dir)
# 	with open(dir, 'r+', encoding="utf-8") as f:
# 		deleteLine = "<capability name=\"documents saved in the Xcode 8 format\" minToolsVersion=\"8.0\"/>"
# 		lines = f.readlines()
# 		# print(lines)
# 		f.seek(0)
# 		for line in lines:
# 			if deleteLine not in line:
# 				if deleteLine in line:
# 					newData = line.remove(deleteLine)
# 					line = line.replace(line, newData)
# 					f.write(line)
# 				else:
# 					f.write(line)
# 			pass
# 		f.truncate()
# 		f.close()
# 		pass

# tFile = "C:\\Users\\jimbo\\source\\prism_old\\livecast"
# dirXib = "C:\\Users\\jimbo\\Documents\\document\\test.xib.xml"
# dir2 = "C:\\Users\\jimbo\\Documents\\document\\test2.xib.xml"
# findXib(tFile)

# def fibnq(n):
# 	total = 0
# 	lastValue = 0
# 	for i in range(n+1):
# 		if i == 1:
# 			lastValue = 1
# 		temp = total
# 		total = total + lastValue
# 		lastValue = temp
# 		print(total)
# 	# print(total)
# fibnq(10)

# import os
# a = [d for d in os.listdir('.')]
# print(a)

# import urllib
# from urllib.request import urlopen
# # response=urllib.urlopen('www.baidu.com')
# response=urlopen('https://www.baidu.com')
# # req=urllib.request('www.baidu.com')
# # response = urllib.urlopen(req)
# # content = response.read()
# print(response)

# import requests
# # r = requests.get("https://www.baidu.com")
# # print(r.status_code)

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.status_code)

# import requests, sys
# from bs4 import BeautifulSoup

# if __name__ == '__main__':
# 	# target = "http://www.biqukan.com/1_1094/5403177.html"
# 	target = 'https://www.biqukan.com/1_1094/'
# 	server = 'https://www.biqukan.com'
# 	response = requests.get(url=target)
# 	response.encoding = response.apparent_encoding
# 	originTxt = response.text
# 	bf = BeautifulSoup(originTxt)
# 	# texts = bf.find('div', class_ = 'showtxt')
# 	# finTxt = texts.text.replace('\xa0'*8,'')
# 	# print(bf.h1.text)
# 	# print(texts.text)
# 	# print(bf.text)
# 	texts1 = bf.find(class_ = 'listmain')
# 	bf2 = BeautifulSoup(str(texts1))
# 	for each in bf2.find_all('a'):
# 		print(each.string, server + each.get('href'))
	# print(a)

# def yang_hui_tac(n):
# 	li = []
# 	for i in range(0,n):
# 		item = [0]*(i+1)
# 		li.append(item)
# 		for j in range(0, i+1):
# 			if i < j:
# 				continue
# 			if i == 0 and j == 0:
# 				li[i][j] = j+1
# 			else:
# 				first = 0
# 				last = 0
# 				if (j-1) >= 0:
# 					first = li[i-1][j-1]
# 				if j < len(li[i-1]):
# 					last = li[i-1][j]

# 				li[i][j] = first + last

# 		print(li[i])

# 	count
# 	# for x in len(li):
		

# # yang_hui_tac(6)

# def f(x):
# 	return x * x

# r = list(map(f, [1,3,5]))

# # print(r)

# def to_lower(x):
# 	return x.lower()

# a = list(map(to_lower, ["Add", "ddd", "DDTTTd"]))
# print(isinstance(a, list))

# print(dir(glob))

# import sys

# def fn(self, name='world'):
# 	print('hello, ', name)

# Hello = type('hello', (object, sys,), dict(hello=fn))
# h = Hello()
# print(h.hello())

# class Animal(object):   #编写Animal类
#     def run(self):
#         print("Animal is running...")

# class Dog(Animal):  #Dog类继承Amimal类，没有run方法
#     pass

# class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
#     def run(self):
#         print('Cat is running...')
#     pass




# class Car(object):  #Car类不继承，有自己的run方法
#     def run(self):
#         print('Car is running...')

# class Stone(object):  #Stone类不继承，也没有run方法
#     def run(self):
#         print('stone is running...')
    

# def run_twice(animal):
#     animal.run()
#     animal.run()

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())
# run_twice(Car())
# run_twice(Stone())



# try:
# 	v = 'abd'.Add('ddd')	
# except Exception as e:
# 	# raise e
# 	print("====",e)

# print(v)


# import pdb

# a = 'd'
# b = a + 'v'
# pdb.set_trace()  #加断点
# c = 8

# import os
# print([x for x in os.listdir('.') if os.path.isdir(x)])


# import json
# with open("C:\\Users\\jimbo\\Desktop\\vlive_test\\boardList.json", 'r', encoding="utf-8") as f:
# 	con = f.read()
# 	# print(con)
# 	j = json.loads(con)
# 	print(j[2]["groupTitle"])

# import os

# print('process (%s) start...' % os.getpid())
# pid = os.fork()
# print("parent=(%s) . child:(%s)" % (os.getpid, pid))


# from multiprocessing import Process
# import os, time

# def run_proc(name):
# 	print("Run child process %s (%s)" % (name, os.getpid()))

# if __name__ == '__main__':
# 	print("parent process %s." % os.getpid())
# 	for x in range(1,10):
# 		p = Process(target=run_proc, args=(x,))
# 		print("Child process will start.")
# 		p.start()
# 		p.join()
# 	print("child process ended")

# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
# 	print("Run task %s (%s)..." % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*8)
# 	end = time.time()
# 	# print("Task %s runs %0.2f seconds" % (name, (end-start)))
# 	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__ == '__main__':
# 	print("Parent process %s" % os.getpid())
# 	p = Pool(5)

# 	for i in range(6):
# 		p.apply_async(long_time_task, args=(i,))
# 		print(i)
# 	print("Waiting for all subprocesses done...")
# 	p.close()
# 	p.join()
# 	print("All subprocesses done.")


# import subprocess

# print("$ nslookup www.python.org")
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)


# 有问题pr 进程
# from multiprocessing import Process, Queue
# import os, time, random

# def write(q):
# 	print("Process to write: %s" % os.getpid())
# 	for value in ['A', 'B', 'C']:
# 		print('Put %s to queue...' % value)
# 		q.put(value)
# 		time.sleep(random.random())

# def readA(q):
# 	print('Process to read %s' % os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue' % value)

# if __name__ == '__main__':
# 	q = Queue()
# 	pw = Process(target=write, args=(q,))
# 	pr = Process(target=readA, args=(q,))
# 	pr.start()
# 	pw.start()
	

# 	pw.join()
# 	print('pw over')
# 	pr.terminate()





# import threading, queue

# q = queue.Queue()

# def worker():
#     while True:
#         item = q.get()
#         print(f'Working on {item}')
#         print(f'Finished {item}')
#         q.task_done()

# # turn-on the worker thread
# threading.Thread(target=worker, daemon=True).start()

# # send thirty task requests to the worker
# for item in range(30):
#     q.put(item)
# print('All task requests sent\n', end='')

# # block until all tasks are done
# q.join()
# print('All work completed')


# import time, threading, random

# balance = 0
# lock=threading.Lock()

# def changeIt(n):
# 	lock.acquire()
# 	global balance
# 	balance = balance + n
# 	time.sleep(random.random())
# 	balance = balance - n
# 	lock.release()
# 	print(threading.current_thread().name, balance)

# 	# print(balance)

# def runThread(n):
# 	for i in range(20):
# 		changeIt(n)

# t1 = threading.Thread(target=runThread, args=(5,), name="t1")
# t2 = threading.Thread(target=runThread, args=(8,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(balance)



# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

# import time,datetime,timezone
# datetime.datetime.now
# print(datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=timestamp))

# import os, io
# import struct

# with open("C:\\Users\\Administrator\\Documents\\pyTest\\test.dat", "rb") as f:
# 	data = f.read()
# 	print(struct.calcsize('@20s2d'))
# 	_list = struct.unpack('@20s2d',data)

# 	print(_list)
# 	#>>> (b'this is text.\x00\xbc#\xff\xff\xff\xff', 99.4444, 33.2490905)
# 	name = _list[0].split(b'\x00', 1)[0] #\x00 是16进制的 \0的意思
# 	print(name)
# 	#>>> b'this is text.'
# 	print(name.decode())
# 	#>>> this is text.

# print(a)
# a.decode(chare)
# print('fdsj奋斗')
# print(b'\xc2\xb5'.decode('utf-8'))

# print(a.decode('utf-8'))
# b = a.encode('ascii', errors='ignore').decode("utf-8")
# print(b)

# from googletrans import Translator
# translator = Translator()
# print(translator.translate('星期日').text)

# import sort

# input_num = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
# # print("原始数据： " , input_num)
# a = sort.bubble_sort(input_num)
# print(a)


# a = '	return QString::fromUtf8(Str("Basic.Settings.Output.Simple.Encoder." "Software"));'

# if ('" "' in a):
# 	a = a.replace('" "', '');

# print(a)

# -*-coding:utf-8-*-
# from time import ctime, sleep
# import threading
# # import numpy as np
# import collections
 
# loops = ['广州', '北京']
# t_list = ['01', '02', '03']
# cldas_sum = collections.deque()
 
 
# class MyThread(threading.Thread):
#     def __init__(self, func, args, name=''):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.func = func
#         self.args = args
#         self.result = self.func(*self.args)
 
#     def get_result(self):
#         try:
#             return self.result
#         except Exception:
#             return None
 
 
# def loop(nloop):
#     for j in t_list:
#         cldas_values = []
#         for k in range(4):
#             cldas_value = nloop + str(k)
#             cldas_values.append(cldas_value)
#         cldas_values.append(j)
#         cldas_values.append(nloop)
#         cldas_sum.append(cldas_values)
#         print(id(cldas_values))
#     #print(cldas_sum)
#     return cldas_sum
 
 
# def main():
#     print('start at', ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t = MyThread(loop, (loops[i],), loop.__name__)
#         threads.append(t)
#     for i in nloops:   # start threads 此处并不会执行线程，而是将任务分发到每个线程，同步线程。等同步完成后再开始执行start方法
#         threads[i].start()
#     for i in nloops:   # jion()方法等待线程完成
#         threads[i].join()
#     print(threads[1].get_result())
#     # print('DONE AT:', ctime())
 
 
# if __name__ == '__main__':
#     main()

#     st = '3333'
#     st1 = st
#     st = "eee"
#     print(st + st1)


# from multiprocessing import Manager,Process,Lock
# import os
# def work(d,lock):
#     # with lock: #不加锁而操作共享的数据,肯定会出现数据错乱
#     d['count']-=1
#     print(d)

# if __name__ == '__main__':
#     lock=Lock()
#     with Manager() as m:
#         dic=m.dict({'count':100})
#         p_l=[]
#         for i in range(100):
#             p=Process(target=work,args=(dic,lock))
#             p_l.append(p)
#             p.start()
#         for p in p_l:
#             p.join()
#         print(dic)
#         #{'count': 94}

# import multiprocessing as mp
# import time
# from ini_common_method import *

# def get_testKeys(_list) -> list:
# 	""" 获取所有的 cpp h 之类的文件列表 """
# 	s_path_test = "D:\\languageCache\\test_keys.txt"
# 	_allKeys = list()
# 	if os.path.exists(s_path_test):
# 		with open(s_path_test, 'r', encoding='utf-8') as f:
# 			allLines = f.readlines()
# 			for x in allLines:
# 				x = x.strip('\n')
# 				_allKeys.append(x)
# 		return _allKeys
# 	print("1")
# 	with open(s_path_test, 'w', encoding='utf-8') as fp:
# 		fp.truncate()
# 		for x in _list:
# 			fp.write(x)
# 			fp.write('\n')

# 	return _list

# def job(_dic, l): #传入锁
# 	print("---- job")
# 	# l.acquire()  #锁住共享变量
# 	# for _ in range(10):
# 	#     time.sleep(0.1)
# 	#     v.value += num
# 	#     print(v.value)
# 	print(_dic)
# 	# _allKeys = 
# 	# for x in _dic.keys():
# 	# 	# time.sleep(0.1)
# 	# 	# v.value += num
# 	# 	print(x)
# 	# l.release()  #释放共享变量

# def multicore():
# 	pass

# if __name__ == '__main__':
# 	_list = get_testKeys([])
# 	_list = _list[0:10]
# 	_keyDic = {}
# 	for x in _list:
# 		_keyDic[x] = 0

# 	l = mp.Lock() #定义锁
# 	p = mp.Pool(2)
# 	with mp.Manager() as MG:
		
# 		mydict=MG.dict(_keyDic)#主进程与子进程共享这个字典
# 		# print(mydict)
# 		# p1 = mp.Process(target=job, args=(mydict, l)) 
# 		# p2 = mp.Process(target=job, args=(mydict, l))
# 		# p1.start()
# 		# p2.start()
# 		# p1.join()
# 		# p2.join()
# 		# print(mydict)
# 		for i in range(5):
# 			p.apply_async(job, args=(mydict, 'l',)) 

# 		# p.apply_async(job, args=(mydict, l,)) 
# 		# p.apply_async(job, args=(mydict, l,))
# 		p.close()
# 		p.join()
# 		print("--")


# if __name__ == '__main__':
# 	print("Parent process %s" % os.getpid())
# 	

# 	for i in range(6):
# 		p.apply_async(long_time_task, args=(i,))
# 		print(i)
# 	print("Waiting for all subprocesses done...")
# 	p.close()
# 	p.join()
# 	print("All subprocesses done.")

import os, time, glob, sys
# from ini_common_method import *

# def get_all_compare_keys(_dir):
# 	_allFiles = list()
# 	if os.path.exists(_dir):
# 		with open(_dir, 'r', encoding='utf-8') as f:
# 			allLines = f.readlines()
# 			for x in allLines:
# 				x = x.strip('\n')
# 				_allFiles.append(x)
# 		return _allFiles

# _allKeys = get_all_compare_keys('D:\\languageCache\\cache.txt')
# _notKeys = get_all_compare_keys('D:\\languageCache\\temp_not_used.txt')
# writeKeyNotUsed_excel('D:\\languageCache\\not_used.xls', _allKeys, _notKeys)


# _path = "C:\\Users\\Administrator\\Desktop\\1\\100168.txt"
# _succpath = "C:\\Users\\Administrator\\Desktop\\1\\succ.txt"
# _is = []

# with open(_path, 'r', encoding='utf-8') as f:
# 	allLines = f.readlines()
# 	for x in allLines:
# 		x1 = x.replace('\n','')
# 		# print(x1)
# 		if x1 == '':
# 			continue
# 		a = int(x)
# 		_is.append(a)

# _is.sort()
# # print(_is)


# _succs = []
# with open(_succpath, 'r', encoding='utf-8') as f:
# 	allLines = f.readlines()
# 	for x in allLines:
# 		x1 = x.replace('\n','')
# 		# print(x1)
# 		if x1 == '':
# 			continue
# 		a = int(x)
# 		_succs.append(a)


# _coms = []
# _succCount = 0;
# _allCount = 0;
# for x in _is:
# 	_allCount += 1
# 	if x in  _succs:
# 		if _allCount <= 105:
# 			_succCount += 1
# 		_coms.append((x, "     成功"))
# 	else:
# 		_coms.append((x, "     失败xxxxxx"))

# print("_succCount:" + str(+_succCount))

# for x in _coms:
# 	print(x)