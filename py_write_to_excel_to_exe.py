# coding = utf-8

r"""
将所有ini文件 的key value 混合比对 写进 excel 文件
打包命令：pyinstaller -F py_write_to_excel.py
"""

import os
import argparse
import xlrd
import xlwt

s_ini_paths_only = ["en-US.ini", "ja-JP.ini", "id-ID.ini","ko-KR.ini","pt-BR.ini"]
# dir_common_pre = "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\"
# s_ini_paths = [dir_common_pre + x for x in s_ini_paths_only]
# s_write_path_excel = "D:\\languageCache\\all_language.xls"

def getINIKeyValues(dir) -> list:
    """ 获取所有的  ini 文件的key value 的双重数组"""
    _keys = list()
    _values = list()
    if (not os.path.exists(dir)):
        return [], []
        
    with open (dir, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            _ma = line.split("=\"")
            if len(_ma) > 1:
                _keys.append(_ma[0])
                _values.append("\"" + _ma[1])
    return _keys, _values

def getINIKeyValuesDict(dir) -> dict:
    """ 获取所有的  ini 文件的key value 的 字典"""
    _lists = getINIKeyValues(dir)
    _keyValueDict = {}
    _keys = _lists[0]
    _values = _lists[1]
    for i in range(0,len(_keys)):
        _keyValueDict[_keys[i]] = _values[i]
    return _keyValueDict

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

def writeCompareKeyToExcel(_dir, _names, _keys, _templateDics = [], _isWriteAll = False):
    
    # _ignoreKey = getExcelIgnoreKeys()
    _ignoreKey = []
    if _isWriteAll == False:
        for i in range(0,len(_templateDics)):
            _str = "str" + str(i)
            _names.append(_str)

    _set = set()
    for x in _keys:
        for _subKey in x:
            _set.add(_subKey)
    if _isWriteAll == False:
        for x in _ignoreKey:
            if x in _set:
                _set.remove(x)

    _set = sorted(_set)
    print("写入key数量：" + str(len(_set)))
    # for x in _set:
    #   print(x)
    if os.path.exists(_dir):
        os.remove(_dir)
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('First')

    # 设置冻结窗口
    # 设置冻结为真
    worksheet.set_panes_frozen('1')
    # 水平冻结
    worksheet.set_horz_split_pos(1)
    # 垂直冻结
    worksheet.set_vert_split_pos(1)
    worksheet.col(0).width = 12000 

    # 写入excel
    # 参数对应 Y, X, 值
    _allIndex  = 0
    #写入所有 key
    _wirteDic = {}
    for x in _set:
        _allIndex = _allIndex+1
        worksheet.write(_allIndex,0, label = x)
        _wirteDic[str(_allIndex)] = str(x)
        
    st_white_center = xlwt.easyxf('pattern: pattern solid;')
    alignment = xlwt.Alignment()
    st_white_center.pattern.pattern_fore_colour = 1 #1 白色
    alignment.horz = xlwt.Alignment.HORZ_CENTER #水平居中
    st_white_center.alignment = alignment

    #写入 每列的 名字
    for i  in range(0,len(_names)):
        worksheet.write(0,i, _names[i], st_white_center)

        _width = 3000;
        if i == 0:
            _width = 10000

        if _isWriteAll == True and i != 0:
            _width = 12000
        else:
            if i >= len(_names) - 2 :
                _width = 30000

        worksheet.col(i).width = _width

    def is_contain_key(_list, _key) -> bool:
        for x in _list:
            if x == _key:
                return True
        return False

    st_white_left = xlwt.easyxf()
    alignment = xlwt.Alignment()
    st_white_left.pattern.pattern_fore_colour = 1 #1 白色
    alignment.horz = xlwt.Alignment.HORZ_LEFT
    # alignment.wrap = 1 #自动换行
    st_white_left.alignment = alignment

    st_orange_center = xlwt.easyxf('pattern: pattern solid;')
    st_orange_center.pattern.pattern_fore_colour = 51 #51 是橘黄色
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER #水平居中
    st_orange_center.alignment = alignment

    # Y轴
    for _index in range(1,_allIndex+1):
        #key 的字符串
        _key = _wirteDic[str(_index)]

        if _isWriteAll == True:
            # X轴
            for i in range(0,len(_templateDics)):
                _templateDic = _templateDics[i]
                if _key in _templateDic.keys():
                    worksheet.write(_index, i + 1, _templateDic[_key][1:-2], st_white_left)
                else:
                    worksheet.write(_index, i + 1, "", st_orange_center)
            continue

        #取对应行数的key是否存在
        for i in range(0,len(_keys)):
            if is_contain_key(_keys[i], _key) == False:
                worksheet.write(_index,i+1, "X", st_orange_center)

        #添加英文和其他文字的的实际参考字符串
        for i in range(0,len(_templateDics)):
            _templateDic = _templateDics[i]
            if _key in _templateDic.keys():
                worksheet.write(_index, len(_keys) + i + 1, _templateDic[_key][1:-2], st_white_left)

    badBG = xlwt.Pattern()
    badBG.pattern = badBG.SOLID_PATTERN
    badBG.pattern_fore_colour = 3

    badFontStyle = xlwt.XFStyle()
    badFontStyle.pattern = badBG
    # 保存Excel_test
    workbook.save(_dir)

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