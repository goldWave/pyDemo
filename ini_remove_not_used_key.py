# coding = utf-8

import os
from ini_common_method import getINIKeyValues
from ini_common_method import findAllCheckFile
from ini_common_method import openAndCheckUsedData
from ini_common_method import deleteKeysInINIFiles


s_ini_paths = ["C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\en-US.ini", "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\id-ID.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\ko-KR.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\pt-BR.ini"]

if __name__ == '__main__':
	#keys 
	_allKeys = getINIKeyValues(s_ini_paths[3])

	for i in range(len(_allKeys) - 1, -1, -1):
		_key = _allKeys[i]
		if _key.startswith('Channels.'):
			_allKeys.remove(_key)
	_li = findAllCheckFile()

	#long long time to 检查key 是否被使用
	_notUsed_key = openAndCheckUsedData(_li, _allKeys, False)

	#删除 未使用的key
	deleteKeysInINIFiles(s_ini_paths, _notUsed_key)
