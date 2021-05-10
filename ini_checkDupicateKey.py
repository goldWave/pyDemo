# coding = utf-8

import os,glob
from ini_common_method import getINIKeyValues

# s_ini_paths_only = ["en-US.ini", "id-ID.ini","ko-KR.ini","pt-BR.ini", "ja-JP.ini"]
dir_common_pre = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\"
# s_ini_paths = [dir_common_pre + x for x in s_ini_paths_only]
s_ini_paths = glob.glob(dir_common_pre + "*.ini", recursive=False)


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
				if _keys[i].lower() == _keys[j].lower():
					_cou = _cou + 1;
				if _cou >= 2:
					print(_keys[i] + "=" + _values[i])
					break
		
