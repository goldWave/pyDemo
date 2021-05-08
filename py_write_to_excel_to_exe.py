# coding = utf-8

r"""
将所有ini文件 的key value 混合比对 写进 excel 文件

打包命令: pyinstaller -F "D:\pythonDemo\pysrc\py_write_to_excel_to_exe.py" "D:\pythonDemo\pysrc\ini_common_method.py"


使用方法: D:\destion\dist\py_write_to_excel_to_exe.exe  -O "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\" -D "D:\destion\dist\languages.xls"

param: -O ini 文件的上级目录，地址后面必须以 \\ 结尾 
param: -D 输出的excel 的地址。
"""

import os
import argparse
from ini_common_method import *

s_ini_paths_only = ["en-US.ini", "ja-JP.ini", "id-ID.ini","ko-KR.ini","pt-BR.ini"]
# dir_common_pre = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\"
# s_ini_paths = [dir_common_pre + x for x in s_ini_paths_only]
# s_write_path_excel = "D:\\languageCache\\all_language.xls"

def writeDiffToExcel():
    #多个ini 互相比较，将 差异 的地方输出到 excel
    global s_ini_paths
    global s_write_path_excel

    _name = ["KEYS"]
    for x in s_ini_paths:
        _name.append(x.split("\\")[-1])

    _dics = []
    for x in s_ini_paths:
        _dics.append(getINIKeyValuesDict(x))

    _mores = [_dic.keys() for _dic in _dics]
    writeCompareKeyToExcel(s_write_path_excel, _name, _mores, _dics, _isWriteAll=True)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("-O", type=str, default="", help='origin inis path')
    parser.add_argument("-D", type=str, default='',help='destination file')
    args = parser.parse_args()

    dir_common_pre = args.O
    s_write_path_excel = args.D
    if dir_common_pre == "" or s_write_path_excel == "":
        sys.stderr("-----origin inis path or destination file is empty-------")
        exit()

    s_ini_paths = [dir_common_pre + x for x in s_ini_paths_only]

    writeDiffToExcel()
    print("写入成功，地址：" + s_write_path_excel)
    print("done.")