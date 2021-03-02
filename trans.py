# coding = utf-8

import os

dir = "D:\\licecap\\en-US.ini"
dir2 = "D:\\licecap\\en-US_1.txt"
dir_trans_key = "D:\\licecap\\translate_f.txt"
dir_trans_all = "D:\\licecap\\translate_all.txt"


class JBTrans(object):
	"""docstring for JBTrans"""
	def __init__(self):
		super(JBTrans, self).__init__()
		
		self._list=[]
		self._allOriginal=""

	def wirteToFile(self):
		with open(dir2, 'w', encoding='utf-8') as fp:
			fp.truncate()
			fp.writelines(self._list)

	def getValue(self):
		with open (dir, 'r', encoding='UTF-8') as f:
			lines = f.readlines()
			self._allOriginal = lines
			for line in lines:
				# a = line.decode()
				_ma = line.split("=\"")
				if len(_ma) > 1:
					origin = "\"" + _ma[1];
					self._list.append(origin)

	def replaceKey(self):
		if not os.path.exists(dir_trans_key):
			print("not contain transltate key file return")
			return

		with open(dir_trans_key, 'r', encoding='UTF-8') as f:
			_keyLines = f.readlines()
			with open(dir_trans_all, 'w', encoding='utf-8') as fAll:
				i = 0
				for v in self._allOriginal:
					_ma = v.split('="')
					if len(_ma) > 1:
						lineString = _ma[0] + "=" + _keyLines[i]
						fAll.write(lineString)
						print(lineString)
						i=i+1
					else:
						fAll.write(v)

if __name__ == '__main__':
	classTr = JBTrans()
	classTr.getValue()
	classTr.wirteToFile()
	classTr.replaceKey()

