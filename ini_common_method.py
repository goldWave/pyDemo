# coding = utf-8

import os
from time import ctime, sleep
import threading

dir_all_file = "D:\\licecap\\all_file.txt"
dir_i_file = "D:\\licecap\\i_file.txt"
dir_checked = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism"

def findAllCheckFile_i() -> list:
	""" 获取所有的 cpp h 之类的文件列表 """
	_allFiles = list()
	if os.path.exists(dir_i_file):
		with open(dir_i_file, 'r', encoding='utf-8') as f:
			allLines = f.readlines()
			for x in allLines:
				x = x.strip('\n')
				_allFiles.append(x)
		return _allFiles

	index = 0
	for root, lists, files in os.walk(dir_checked):
		for file in files:
			if os.path.splitext(file)[1] in ['.i']:
				# print(root + "=====" + file)
				_allFiles.append(root+"\\"+file)

	with open(dir_i_file, 'w', encoding='utf-8') as fp:
		fp.truncate()
		for x in _allFiles:
			fp.write(x)
			fp.write('\n')

	return _allFiles

def findAllCheckFile() -> list:
	""" 获取所有的 .i 之类的文件列表 """
	_allFiles = list()
	if os.path.exists(dir_all_file):
		with open(dir_all_file, 'r', encoding='utf-8') as f:
			allLines = f.readlines()
			for x in allLines:
				x = x.strip('\n')
				_allFiles.append(x)
		return _allFiles

	index = 0
	for root, lists, files in os.walk(dir_checked):
		for file in files:
			if os.path.splitext(file)[1] in ['.h','.hpp','.c','.cpp', '.ui'] and file.startswith('moc') == False and file.startswith('qrc') == False:
				# print(root + "=====" + file)
				_allFiles.append(root+"\\"+file)

	with open(dir_all_file, 'w', encoding='utf-8') as fp:
		fp.truncate()
		for x in _allFiles:
			fp.write(x)
			fp.write('\n')

	return _allFiles

def getINIKeyValues(dir) -> list:
	""" 获取所有的  ini 文件的key 列表"""
	with open (dir, 'r', encoding='UTF-8') as f:
		lines = f.readlines()
		_list = list()
		for line in lines:
			_ma = line.split("=\"")
			if len(_ma) > 1:
				# origin = "\"" + _ma[1];
				# _dict[_ma[0]] = origin
				_list.append(_ma[0])
		return _list

def openAndCheckUsedData1(fileList, keyList, isMacro=False, printProgress=False) -> list:
	"""
	fileList = 所有文件的路径
	keyList = 查找的key
	isMacro = key 是否是宏
	return 没有使用的key
	"""
	key_channel_header = 'Channels.'
	allCount = len(fileList)
	# _notUsed = keyList
	for file in fileList:
		# print(file)
		with open(file, 'r', encoding='utf-8') as f:
			allLine = f.readlines()
			strLine = ",".join(allLine)
			strLine = strLine.replace('" "', '');
			for i in range(len(keyList) - 1, -1, -1):
				_key = keyList[i]
				if isMacro:
					if _key in strLine:
						keyList.remove(_key)

				else:
					_copyKey = _key
					if _copyKey.startswith("key_channel_header") and ('CHANNELS_TR(' + _copyKey.replace(key_channel_header,'') + ')') in strLine:
						keyList.remove(_key)
					elif ('"' + _key + '"' in strLine) or ('<string>'+_key+'</string>' in strLine) or ('\"'+_key+'\"' in strLine):
						keyList.remove(_key)

	return keyList.copy()

def openAndCheckUsedData(fileList, keyList, isMacro=False, printProgress=False) -> list:
	"""
	fileList = 所有文件的路径
	keyList = 查找的key
	isMacro = key 是否是宏
	return 没有使用的key
	"""
	keyDic = {}
	for x in keyList:
		keyDic[x] = 0
	
	# allCount = len(fileList)
	
	def threadOpen(_file, isMacro, printProgress):
		global _index
		global allCount
		# for file in fileList:
		sem.acquire()
		if printProgress == True:
			# print(str(index) + "/" + str(allCount) +"  "+ _file)
			# _index = _index + 1
			print(_file)
		key_channel_header = 'Channels.'

		# print('DONE AT--start:', ctime())
		with open(_file, 'r', encoding='utf-8') as f:
			# print('DONE AT--open:', ctime())
			allLine = f.readlines()
			strLine = ",".join(allLine)
			strLine = strLine.replace('" "', '');
			# with open("D:\\licecap\\tttt.txt", 'r+', encoding='utf-8') as f1:
			# 	f1.write(strLine)

			# print('DONE AT--join:', ctime())
			for _key in keyDic:
				if keyDic[_key] > 0:
					continue
				# _key = keyList[i]
				if isMacro:
					if _key in strLine:
						# keyList.remove(_key)
						lock.acquire()
						keyDic[_key] = keyDic[_key] + 1
						lock.release()
				else:
					_copyKey = _key
					if _copyKey.startswith("key_channel_header") and ('CHANNELS_TR(' + _copyKey.replace(key_channel_header,'') + ')') in strLine:
						lock.acquire()
						keyDic[_key] = keyDic[_key] + 1
						lock.release()
					elif ('"' + _key + '"' in strLine) or ('<string>'+_key+'</string>' in strLine) or ('\"'+_key+'\"' in strLine):
						# keyList.remove(_key)
						lock.acquire()
						keyDic[_key] = keyDic[_key] + 1
						lock.release()
		# if printProgress == True:
		# 	print('DONE AT--over:', ctime())
		sem.release()



	sem=threading.Semaphore(10)
	lock=threading.Lock()   #将锁内的代码串行化
	# _notUsed = keyList
	_index = 1
	l=[]
	for _file in fileList:
		t=threading.Thread(target=threadOpen,args=(_file,isMacro,printProgress,))
		t.start()
		l.append(t)

	for t in l:
		t.join()

	_fileList = []	
	for _key in keyDic:
		if keyDic[_key] == 0:
			_fileList.append(_key)		
	return _fileList.copy()


def removeMacroFileNotUsedKey(_path, keyList):
	"""传入宏文件路径，和 需要删除的宏key"""

	def _isCoantainKey(line, key) -> bool:
		if line.startswith("#define "):
			_ma = line.replace("#define ","")
			_ma = _ma.split(" ")
			if len(_ma) > 1:
				if _ma[0] == key:
					return True
		return False

	with open (_path, 'r+', encoding='UTF-8') as f:
		lines = f.readlines()
		_list = list()
		f.seek(0)
		f.truncate()

		for line in lines:
			_isContain = False
			for key in keyList:
				if _isCoantainKey(line, key):
					_isContain = True
					break
			if _isContain == True:
				continue

			f.write(line)	

def deleteKeysInINIFiles(fileList, keyList):
	"""
	fileList = 所有文件的路径
	keyList = 删除的key
	"""

	def _isCoantainKey(line, key) -> bool:
		_ma = line.split("=\"")
		if len(_ma) > 1:
			if _ma[0] == key:
				return True
		return False

	for file in fileList:
		with open(file, 'r+', encoding='utf-8') as f:
			lines = f.readlines()
			f.seek(0)
			f.truncate()

			for line in lines:
				_isContain = False
				for key in keyList:
					if _isCoantainKey(line, key):
						_isContain = True
						break
				if _isContain == True:
					continue

				f.write(line)
