# coding = utf-8

from ini_common_method import findAllCheckFile
from ini_common_method import getINIKeys
from ini_common_method import writeCompareKeyToExcel
import os

s_ini_paths = ["C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\en-US.ini", "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\id-ID.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\ko-KR.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\pt-BR.ini"]


def compare(_base, _list) -> list:
	_more = list()
	if len(_list) < 0:
		print("count is incorrect, exit")
		return []

	_allCount = len(_list)
	for _baseKey in _base:
		_count = 0;
		for _subList in _list:
			for _subKey in _subList:
				if _baseKey == _subKey:
					_count = _count + 1
					break
		if _count != _allCount:
			_more.append(_baseKey)
	return _more

	
def CheckDiff(_paths) -> list:
	_allKeys = list()
	for x in _paths:
		_allKeys.append(getINIKeys(x))

	_mores = list()
	for x in _allKeys:
		_mores.append(compare(x, _allKeys))

	return _mores
	
if __name__ == '__main__':

	_mores = CheckDiff(s_ini_paths)
	_name = []
	for x in s_ini_paths:
		_name.append(x.split("\\")[-1])
	
	writeCompareKeyToExcel("D:\\licecap\\compare.xls", _name, _mores)