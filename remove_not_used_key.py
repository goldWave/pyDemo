# coding = utf-8

import os

# dir = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\en-US.ini"
dir = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\ko-KR.ini"

# dir_new_local = "D:\\licecap\\en-US.ini"
dir_new_local = "D:\\licecap\\ko-KR.ini"

dir_checked = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism"
dir_all_file = "D:\\licecap\\all_file.txt"

dir_not_uesd = "D:\\licecap\\not_uesd.txt"

class JBCheckDupicate(object):
	def __init__(self):
		super(JBCheckDupicate, self).__init__()
		
		self.dict={}
		self._allOriginal=""
		self._allFiles=[]
		self._allKeys={}
		self._allKeysList=[]

	def getValue(self):
		with open (dir, 'r', encoding='UTF-8') as f:
			lines = f.readlines()
			self._allOriginal = lines
			for line in lines:
				_ma = line.split("=\"")
				if len(_ma) > 1 and _ma[0].startswith('Channels.') == False:
					self._allKeys[_ma[0]]=0
				# 	origin = "\"" + _ma[1];
				# 	self.dict[_ma[0]] = origin
			# print(self._allFiles)

	def findAllCheckFile(self):

		if os.path.exists(dir_all_file):
			with open(dir_all_file, 'r', encoding='utf-8') as f:
				allLines = f.readlines()
				for x in allLines:
					x = x.strip('\n')
					self._allFiles.append(x)
			return

		index = 0
		for root, lists, files in os.walk(dir_checked):
			for file in files:
				if os.path.splitext(file)[1] in ['.h','.hpp','.c','.cpp', '.ui'] and file.startswith('moc') == False and file.startswith('qrc') == False:
					# print(root + "=====" + file)
					self._allFiles.append(root+"\\"+file)

		with open(dir_all_file, 'w', encoding='utf-8') as fp:
			fp.truncate()
			for x in self._allFiles:
				fp.write(x)
				fp.write('\n')

	def openAndCheckData(self):
		# print(self._allKeys)
		# return
		allCount = len(self._allFiles)
		index=0
		for file in self._allFiles:
			# print(file)
			with open(file, 'r', encoding='utf-8') as f:
				allLine = f.readlines()
				for (keySin,value) in self._allKeys.items():
					if value > 0:
						continue
					strLine = ",".join(allLine)
					if strLine.find('"' + keySin + '"') > 0 or strLine.find('<string>'+keySin+'</string>') > 0 or strLine.find('\"'+keySin+'\"') > 0:
						self._allKeys[keySin] = self._allKeys[keySin] + 1

			index = index + 1
			print(str(index) + '/' + str(allCount) + file)

if __name__ == '__main__':
	classTr = JBCheckDupicate()
	classTr.getValue()
	if os.path.exists(dir_not_uesd) == False:
		classTr.findAllCheckFile()
		classTr.openAndCheckData()
		# print(classTr._allKeys)

		with open(dir_not_uesd, 'w', encoding='utf-8') as f:
			for (key,value) in classTr._allKeys.items():
				if value == 0:
					f.write(key)
					f.write('\n')
			print('file not used key is write to file:' + dir_not_uesd)

	with open(dir_not_uesd, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			classTr._allKeysList.append(line.strip('\n'))

	with open (dir_new_local, 'w', encoding='UTF-8') as f:
		pass

	with open (dir_new_local, 'w+', encoding='UTF-8') as f:
		for line in classTr._allOriginal:
			_isFound = False
			for key in classTr._allKeysList:
				if line.startswith(key+'='):
					_isFound = True
			if _isFound == False:
				f.write(line)
	print("new file is :", dir_new_local)