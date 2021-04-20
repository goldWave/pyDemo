# coding = utf-8

import os
from ini_common_method import getINIKeyValues
from ini_common_method import findAllCheckFile
from ini_common_method import findAllCheckFile_i
from ini_common_method import openAndCheckUsedData
from ini_common_method import openAndCheckUsedData1
from ini_common_method import deleteKeysInINIFiles
from time import ctime, sleep

s_ini_paths = ["C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\en-US.ini", "C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\id-ID.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\ko-KR.ini","C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\main\\data\\locale\\pt-BR.ini"]

if __name__ == '__main__':
	# #keys 
	_allKeys = getINIKeyValues(s_ini_paths[3])

	for i in range(len(_allKeys) - 1, -1, -1):
		_key = _allKeys[i]
		# if _key.startswith('Channels.'):
		# 	_allKeys.remove(_key)
	_li = findAllCheckFile()

	_list_i = findAllCheckFile_i()

	#long long time to 检查key 是否被使用
	print('DONE AT--over:', ctime())
	# _notUsed_key = ['Basic.Settings.Advanced.Hotkeys.NeverDisableHotkeys']
	# _notUsed_key = ['Basic.Settings.Output.Simple.Warn.Lossless.Title','Basic.Settings.Output.Simple.Encoder.Software','Basic.Settings.Output.Simple.Encoder.Hardware.QSV','Basic.Settings.Output.Simple.Encoder.Hardware.AMD','Basic.Settings.Output.Simple.Encoder.Hardware.NVENC','Basic.Settings.Output.Simple.Encoder.SoftwareLowCPU','Basic.Settings.Output.VideoBitrate','Basic.Settings.Output.AudioBitrate,Basic.Settings.Output.Reconnect']
	# _notUsed_key = ['Basic.Settings.Output.Simple.Encoder.Software', 'Basic.Settings.Output.Simple.Encoder.Hardware.QSV', 'Basic.Settings.Output.Simple.Encoder.Hardware.AMD', 'Basic.Settings.Output.Simple.Encoder.Hardware.NVENC', 'Basic.Settings.Output.Simple.Encoder.SoftwareLowCPU', 'Basic.Settings.Output.Adv.FFmpeg.SaveFilter.Common', 'Basic.Settings.Output.Adv.FFmpeg.SaveFilter.All', 'Basic.Settings.Video.DisableAeroWindows', 'Basic.Settings.Audio.MultiChannelWarning.Enabled']
	# _notUsed_key = ['Channels.add','Channels.URLCopiedToClipboard','Channels.ONline','Channels.OFFline']
	_notUsed_key = openAndCheckUsedData(_li, _allKeys, False)
	print('DONE AT--over:', ctime())
	print("\n-------------------------\n\n")
	# print(_notUsed_key)
	# return
	# _list_i=['C:\\Users\\Administrator\\source\\PRISMLiveStudio\\src\\prism\\build\\main\\PRISMLiveStudio.dir\\Debug\\window-basic-auto-config-test.i']
	_notUsed_key = openAndCheckUsedData(_list_i, _notUsed_key, False, printProgress=True)
	print("\n-------------------------\n\n")
	print(_notUsed_key)
	#删除 未使用的key
	deleteKeysInINIFiles(s_ini_paths, _notUsed_key)
