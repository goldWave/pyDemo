# coding = utf-8

r"""
将所有ini文件 的key 的差异性 写进 excel 文件

"""

from ini_common_method import *
import os

s_ini_paths_only = ["en-US.ini", "ja-JP.ini", "id-ID.ini","ko-KR.ini","pt-BR.ini"]
# s_ini_paths_only = ["en-US.ini","ja-JP.ini"]

dir_common_pre = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\"
s_ini_paths = [dir_common_pre + x for x in s_ini_paths_only]

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

def writeDiffToExcel():
	#多个ini 互相比较，将 差异 的地方输出到 excel
	_mores = CheckDiff(s_ini_paths)
	_name = ["KEYS"]
	for x in s_ini_paths:
		_name.append(x.split("\\")[-1])
	_dics = list()
	_dics.append(getINIKeyValuesDict(s_ini_paths[0]))
	_dics.append(getINIKeyValuesDict(s_ini_paths[3]))
	writeCompareKeyToExcel("D:\\languageCache\\compare_language.xls", _name, _mores, _dics)

def removeMoreEnglishKey():
	#和english 比较，将多出的字符串删除掉
	_mores = CheckDiff(s_ini_paths)
	# print(_mores[1])
	_del = s_ini_paths[1]
	deleteKeysInINIFiles([_del], _mores[1])

if __name__ == '__main__':

	writeDiffToExcel()
	# removeMoreEnglishKey()
