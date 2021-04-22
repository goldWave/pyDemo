# coding = utf-8

import os
from ini_common_method import getINIKeyValues

s_ini_paths = ["C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\en-US.ini", "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\id-ID.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\ko-KR.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\pt-BR.ini"]



if __name__ == '__main__':
	""" 
	检查 ini 文件是否存在相同的key
	"""
	for x in s_ini_paths:
		print("\n\n\n\n\n" +x + "\n -----\n")
		_lists = getINIKeyValues(x)

		_keys = _lists[0]
		_values = _lists[1]
		for i in range(0,len(_keys)):
			_cou = 0
			for j in range(0,len(_keys)):
				if _keys[i] == _keys[j]:
					_cou = _cou + 1;
				if _cou >= 2:
					print(_keys[i] + "=" + _values[i])
					break
		


