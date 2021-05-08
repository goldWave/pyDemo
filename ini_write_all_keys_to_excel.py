r"""
将所有ini文件 的key value 混合比对 写进 excel 文件

"""

import os
from ini_common_method import *

s_ini_paths_only = ["en-US.ini", "ja-JP.ini", "id-ID.ini","ko-KR.ini","pt-BR.ini"]
# s_ini_paths_only = ["en-US.ini","ja-JP.ini"]
# s_ini_paths_only = ["en-US.ini"]

dir_common_pre = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\"
s_ini_paths = [dir_common_pre + x for x in s_ini_paths_only]


def writeDiffToExcel():
	#多个ini 互相比较，将 差异 的地方输出到 excel
	_name = ["KEYS"]
	for x in s_ini_paths:
		_name.append(x.split("\\")[-1])

	_dics = []
	for x in s_ini_paths:
		_dics.append(getINIKeyValuesDict(x))

	_mores = [_dic.keys() for _dic in _dics]
	print(len(_mores[0]))
	writeCompareKeyToExcel("D:\\languageCache\\all_language.xls", _name, _mores, _dics, _isWriteAll=True)

if __name__ == '__main__':
	writeDiffToExcel()