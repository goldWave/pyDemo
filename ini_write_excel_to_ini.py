import xlrd, os
from ini_common_method import getKeyValueFromExcel
from ini_common_method import writeINIKeyToExistFile

# dir_all_file = "D:\\licecap\\all_file.txt"
dir_common_pre = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale"
s_key_paths = [{"EN":"en-US.ini"},{"KR":"ko-KR.ini"},{"IND":"id-ID.ini"},{"POR":"pt-BR.ini"}]
s_excelPath = "D:\\Download\\第四轮翻译_0428.xlsx"

def getDicKey(_dic) -> str:
	for k in _dic:
		return k
	return ""

if __name__ == '__main__':
	for _index in range(len(s_key_paths)):
		print(_index)
		_name = getDicKey(s_key_paths[_index])
		_dic = getKeyValueFromExcel(s_excelPath, "Sheet1", _name)
		# print(_dic)
		print("\n\n\n\n")
		_path = dir_common_pre + '\\' + s_key_paths[_index][getDicKey(s_key_paths[_index])]
		# print(_path)
		writeINIKeyToExistFile(_path, _dic)

