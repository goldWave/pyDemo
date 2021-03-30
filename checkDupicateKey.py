# coding = utf-8

import os

dir = "D:\\licecap\\en-US.ini"
# dir_checked = "C:\\Users\\Administrator\\source\\PRISMLiveStudio"
dir_checked = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main"
dir_all_file = "D:\\licecap\\all_file.txt"

class JBCheckDupicate(object):
	def __init__(self):
		super(JBCheckDupicate, self).__init__()
		
		self.dict={}
		self._allOriginal=""
		self._allFiles=[]
		self._allKeys=[]

	def getValue(self):
		with open (dir, 'r', encoding='UTF-8') as f:
			lines = f.readlines()
			self._allOriginal = lines
			for line in lines:
				_ma = line.split("=\"")
				if len(_ma) > 1:
					origin = "\"" + _ma[1];
					self.dict[_ma[0]] = origin

	def chckDupicate(self):
		_duplValue={}
		for x,v in self.dict.items():
			if v in _duplValue:
				continue

			_duplValue[v]=True
			allString=[x]

			for x1,v1 in self.dict.items():
				if x != x1 and v == v1:
					allString.append(x1)
			
			if len(allString) > 1:
				self._allKeys.append(allString)

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
				if os.path.splitext(file)[1] in ['.h','.hpp','.c','.cpp'] and file.startswith('moc') == False:
					# print(root + "=====" + file)
					self._allFiles.append(root+"\\"+file)

		with open(dir_all_file, 'w', encoding='utf-8') as fp:
			fp.truncate()
			for x in self._allFiles:
				fp.write(x)
				fp.write('\n')

	def openAndCheckData(self):
		index = 0
		for file in self._allFiles:
			index = index + 1
			print(index)
			with open(file, 'r+', encoding='utf-8') as f:
				allLine = f.readlines()
				f.seek(0)
				f.truncate()
				for singleLine in allLine: #所有行数
					for keyD in self._allKeys: #二元数组
						for keySin in keyD: #单独的key
							if singleLine.find('"' + keySin + '"') > 0 and keyD[0] != keySin:
								# print(keySin + "--------" +singleLine)
								singleLine = singleLine.replace(keySin, keyD[0])
					f.write(singleLine)

if __name__ == '__main__':
	classTr = JBCheckDupicate()
	classTr.getValue()
	classTr.chckDupicate()
	classTr.findAllCheckFile()
	classTr.openAndCheckData()


