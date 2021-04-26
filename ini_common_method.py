# coding = utf-8

import os, time
from time import ctime, sleep
import threading
import xlrd
import xlwt
import multiprocessing as mp

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

def getINIKeys(dir) -> list:
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

def getINIKeyValues(dir) -> list:
	""" 获取所有的  ini 文件的key value 的双重数组"""
	_keys = list()
	_values = list()
	with open (dir, 'r', encoding='UTF-8') as f:
		lines = f.readlines()
		for line in lines:
			_ma = line.split("=\"")
			if len(_ma) > 1:
				_keys.append(_ma[0])
				_values.append("\"" + _ma[1])
	return _keys, _values


def openAndCheckUsedData_Single(fileList, keyList, isMacro=False, printProgress=False) -> list:
	"""
	fileList = 所有文件的路径
	keyList = 查找的key
	isMacro = key 是否是宏
	return 没有使用的key
	"""
	keyDic = {}
	for x in keyList:
		keyDic[x] = 0
		
	def threadOpen(_file, isMacro, printProgress):
		global _index
		global allCount
		# sem.acquire()
		if printProgress == True:
			print(_file)
		key_channel_header = 'Channels.'
		t0 = time.time()
		with open(_file, 'r', encoding='utf-8') as f:
			allLine = f.readlines()
			strLine = ",".join(allLine)
			strLine = strLine.replace('" "', '');
			word_b = set(strLine.split())
			for _key in keyDic:  #800 * 3
				# t0 = time.time()
				if keyDic[_key] > 0:
					continue
				if isMacro:
					if _key in strLine:
						keyDic[_key] = keyDic[_key] + 1
				else:
					_copyKey = _key
					if _copyKey.startswith("key_channel_header") and ('CHANNELS_TR(' + _copyKey.replace(key_channel_header,'') + ')') in strLine:
						keyDic[_key] = keyDic[_key] + 1
						# "key" or  <string>key</string> or \"key\"
					elif _key in strLine:
						if ('"' + _key + '"' in strLine) or ('<string>'+_key+'</string>' in strLine) or ('\"'+_key+'\"' in strLine):
							keyDic[_key] = keyDic[_key] + 1
		# if printProgress == True:
		# 	t1 = time.time()
		# 	print(str((t1-t0)*1000) + " ms")


	_index = 1
	for _file in fileList:
		threadOpen(_file, isMacro, printProgress)

	_fileList = []	
	for _key in keyDic:
		if keyDic[_key] == 0:
			_fileList.append(_key)		
	return _fileList.copy()

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
		sem.acquire()
		if printProgress == True:
			print(_file)
		key_channel_header = 'Channels.'

		# print('DONE AT--start:', ctime())
		with open(_file, 'r', encoding='utf-8') as f:
			if printProgress == True:
				print(_file + "\t"+ str(threading.get_ident()))
			allLine = f.readlines()
			strLine = ",".join(allLine)
			strLine = strLine.replace('" "', '');
			# print('DONE AT--join:', ctime())
			for _key in keyDic:
				if keyDic[_key] > 0:
					continue
				if isMacro:
					if _key in strLine:
						lock.acquire()
						keyDic[_key] = keyDic[_key] + 1
						lock.release()
				else:
					_copyKey = _key
					if _copyKey.startswith("key_channel_header") and ('CHANNELS_TR(' + _copyKey.replace(key_channel_header,'') + ')') in strLine:
						lock.acquire()
						keyDic[_key] = keyDic[_key] + 1
						lock.release()
					elif _key in strLine:
						if ('"' + _key + '"' in strLine) or ('<string>'+_key+'</string>' in strLine) or ('\"'+_key+'\"' in strLine):
							lock.acquire()
							keyDic[_key] = keyDic[_key] + 1
							lock.release()
		sem.release() 

	sem=threading.Semaphore(8)
	lock=threading.Lock()   #将锁内的代码串行化
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

def threadOpen_1(_file, isMacro, printProgress, keyDic, lock):
		# sem.acquire()
		# if printProgress == True:
		# print(_file)
		key_channel_header = 'Channels.'

		with open(_file, 'r', encoding='utf-8') as f:
			if printProgress == True:
				print(_file + "\t"+ str(threading.get_ident()))
			allLine = f.readlines()
			strLine = ",".join(allLine)
			strLine = strLine.replace('" "', '');
			# print('DONE AT--join:', ctime())
			for _key in keyDic.keys():
				if keyDic[_key] > 0:
					continue
				if isMacro:
					if _key in strLine:
						lock.acquire()
						keyDic[_key] = keyDic[_key] + 1
						lock.release()
				else:
					_copyKey = _key
					if _copyKey.startswith("key_channel_header") and ('CHANNELS_TR(' + _copyKey.replace(key_channel_header,'') + ')') in strLine:
						lock.acquire()
						keyDic[_key] = keyDic[_key] + 1
						lock.release()
					elif _key in strLine:
						if ('"' + _key + '"' in strLine) or ('<string>'+_key+'</string>' in strLine) or ('\"'+_key+'\"' in strLine):
							lock.acquire()
							# print("-------" + _key)
							keyDic[_key] = keyDic[_key] + 1
							lock.release()
		# sem.release()

def openAndCheckUsedData_Process(fileList, keyList, isMacro=False, printProgress=False) -> list:
	"""
	fileList = 所有文件的路径
	keyList = 查找的key
	isMacro = key 是否是宏
	return 没有使用的key
	这里主要的 耗时在 大字符串 搜索 子字符串里面，是cpu 密集型，所有用多进程
	而python 的锁导致多线程 访问cpu需要串行，所有多线程并没有进行时间优化
	"""
	_keyDic = {}
	for x in keyList:
		_keyDic[x] = 0
	
	_co = mp.cpu_count()
	# print(_co)
	p = mp.Pool(_co*2)
	m = mp.Manager()
	dic=m.dict(_keyDic)
	_lock = m.Lock()

	for _file in fileList:
		p.apply_async(threadOpen_1,args=(_file,isMacro,printProgress,dic, _lock,))

	p.close()
	p.join()

	_fileList = []	
	for _key in dic:
		if dic[_key] == 0:
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


def getKeyValueFromExcel(_ex_path, _sheetName, _ValueKey, _keyName="KEY") -> dict:
	""" 
	获取 excel  表的键值对
	_ex_path： excel 路径
	_sheetName： sheet naame
	_ValueKey： 需要取值的value 的第一行名字
	_keyName： key 的第一行名字
	"""
	# print(_ex_path)
	workbook = xlrd.open_workbook(_ex_path)
	sheet1_object = workbook.sheet_by_name(sheet_name=_sheetName)
	
	# 获取sheet1中的有效行数
	nrows = sheet1_object.nrows
	_backDic = dict()
	# 获取sheet1中的有效列数
	ncols = sheet1_object.ncols
	_keyIndex = -1
	_valueIndex = -1
	for _clos in range(0,ncols):
		cell_info = sheet1_object.cell_value(rowx=0, colx=_clos)
		if cell_info == _keyName:
			_keyIndex = _clos
		elif cell_info == _ValueKey:
			_valueIndex = _clos


	if _keyIndex == -1 or _valueIndex == -1:
		print("-------------error  index not found--------------")
		return _backDic

	for _index in range(1,nrows):
		_key = sheet1_object.cell_value(rowx=_index, colx=_keyIndex)
		_value = sheet1_object.cell_value(rowx=_index, colx=_valueIndex)
		if _key == "" or _value == "":
			continue
		_backDic[_key] = _value
	return _backDic

def writeINIKeyToExistFile(dir, _dic):
	""" 
	将 key value 写进已经存在的 ini 文件中
	dir： ini 路径
	_dic： 需要写入的 key value 的字典
	"""
	with open (dir, 'r+', encoding='UTF-8') as f:
		lines = f.readlines()
		f.seek(0)
		f.truncate()
		for line in lines:
			_ma = line.split("=\"")
			# print(_ma)
			# print(len(_ma))
			if len(_ma) > 1:
				_key = _ma[0]
				_replaceValue = ""
				if _dic.__contains__(_key):
					_replaceValue = _dic[_key]
				
				if _replaceValue != "":
					# print(_key)
					line = _key + '="' + _replaceValue + '"\n'
					_dic.pop(_key)
			f.write(line)

		for k,v in _dic.items():
			line = k + '="' + v + '"\n'
			f.write(line)


def writeCompareKeyToExcel(_dir, _names, _keys):
	_set = set()
	for x in _keys:
		for _subKey in x:
			_set.add(_subKey)
	_set = sorted(_set)
	for x in _set:
		print(x)
	if os.path.exists(_dir):
		os.remove(_dir)
	# 创建一个workbook 设置编码
	workbook = xlwt.Workbook(encoding = 'utf-8')
	# 创建一个worksheet
	worksheet = workbook.add_sheet('First')

	# 设置冻结窗口
	# 设置冻结为真
	worksheet.set_panes_frozen('1')
	# 水平冻结
	worksheet.set_horz_split_pos(1)
	# 垂直冻结
	worksheet.set_vert_split_pos(1)
	worksheet.col(0).width = 12000 

	# 写入excel
	# 参数对应 行, 列, 值
	_allIndex  = 0
	worksheet.write(0,0, label = 'KEY')

	#写入所有 key
	_wirteDic = {}
	for x in _set:
		_allIndex = _allIndex+1
		worksheet.write(_allIndex,0, label = x)
		_wirteDic[str(_allIndex)] = str(x)

	#写入 每列的 名字
	for i  in range(0,len(_names)):
		st = xlwt.easyxf('pattern: pattern solid;')
		alignment = xlwt.Alignment()
		st.pattern.pattern_fore_colour = 1 #1 白色
		alignment.horz = xlwt.Alignment.HORZ_CENTER #水平居中
		st.alignment = alignment
		worksheet.write(0,i+1, _names[i], st)
		worksheet.col(i+1).width = 3000

	def is_contain_key(_list, _key) -> bool:
		for x in _list:
			if x == _key:
				return True
		return False

	#行数
	for _index in range(1,_allIndex+1):
		#key 的字符串
		_key = _wirteDic[str(_index)]

		#取对应行数的key是否存在
		for i in range(0,len(_keys)):
			if is_contain_key(_keys[i], _key) == False:
				st = xlwt.easyxf('pattern: pattern solid;')
				st.pattern.pattern_fore_colour = 51 #51 是橘黄色
				alignment = xlwt.Alignment()
				alignment.horz = xlwt.Alignment.HORZ_CENTER #水平居中
				st.alignment = alignment
				worksheet.write(_index,i+1, "X", st)

	badBG = xlwt.Pattern()
	badBG.pattern = badBG.SOLID_PATTERN
	badBG.pattern_fore_colour = 3

	badFontStyle = xlwt.XFStyle()
	badFontStyle.pattern = badBG
	# 保存Excel_test
	workbook.save(_dir)