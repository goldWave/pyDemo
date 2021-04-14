# coding = utf-8

from ini_common_method import findAllCheckFile
from ini_common_method import getINIKeyValues
import os

s_ini_paths = ["C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\en-US.ini", "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\id-ID.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\ko-KR.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\pt-BR.ini"]


def compare(_list) -> list:
	_more = list()
	_dele = list()
	if len(_list) != 2 :
		print("count is incorrect, exit")
		return

	for x in _list[0]:
		_isContain = False
		for y in _list[1]:
			if x == y:
				_isContain = True
				break
		if _isContain == False:
			_more.append(x)

	for x in _list[1]:
		_isContain = False
		for y in _list[0]:
			if x == y:
				_isContain = True
				break
		if _isContain == False:
			_dele.append(x)

	print("-------this is delet \n")
	print(_dele)
	print("\n\n\n\n\n\n-------this is more \n")
	print(_more)
	return _more

	
class CheckDiff(object):
	"""docstring for CheckDiff"""
	def __init__(self, arg):
		super(CheckDiff, self).__init__()
		self._list = arg
		self._moreList = list()
		_allDics = list()
		for x in self._list:
			_allDics.append(getINIKeyValues(x))
		
		self._moreList = compare(_allDics)
	
		

if __name__ == '__main__':
	c_check = CheckDiff([s_ini_paths[0], s_ini_paths[1]])
	# print(c_check._moreList)
	# _li = findAllCheckFile()
	# print(_li)