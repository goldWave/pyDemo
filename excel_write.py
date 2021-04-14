import xlwt 

def createExcel():
	# 创建一个workbook 设置编码
	workbook = xlwt.Workbook(encoding = 'utf-8')
	# 创建一个worksheet
	worksheet = workbook.add_sheet('My Worksheet')

	# 写入excel
	# 参数对应 行, 列, 值
	worksheet.write(0,0, label = 'theeeis is test')

	# 保存
	workbook.save('../Excel_test.xls')

if __name__ == '__main__':
	createExcel()